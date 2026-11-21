"""
SQLite Database Layer for site-klonu
Handles bank accounts, admin authentication, settings, and payment notifications.
"""
import hashlib
import json
import os
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "data.db"


def get_db():
    conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def hash_password(password: str) -> str:
    # SHA-256 with salt
    salt = "site_klonu_secure_salt_2026"
    return hashlib.sha256((password + salt).encode("utf-8")).hexdigest()


def init_db():
    conn = get_db()
    cur = conn.cursor()

    # 1. Admin Users
    cur.execute("""
        CREATE TABLE IF NOT EXISTS admin_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # 2. Bank Accounts
    cur.execute("""
        CREATE TABLE IF NOT EXISTS bank_accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bank_id TEXT UNIQUE NOT NULL,
            bank_name TEXT NOT NULL,
            iban TEXT NOT NULL,
            holder_name TEXT NOT NULL,
            is_active INTEGER DEFAULT 1,
            display_order INTEGER DEFAULT 0,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # 3. Settings
    cur.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        )
    """)

    # 4. Payments
    cur.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            bank_id TEXT,
            bank_name TEXT,
            amount REAL,
            holder_name TEXT,
            iban TEXT,
            status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Seed default admin if none exists
    cur.execute("SELECT id FROM admin_users WHERE username = 'admin'")
    if not cur.fetchone():
        cur.execute(
            "INSERT INTO admin_users (username, password_hash) VALUES (?, ?)",
            ("admin", hash_password("admin123"))
        )

    # Seed default settings
    default_settings = {
        "default_bank": "denizbank",
        "default_holder": "Levent Tanrıver",
        "countdown_seconds": "280"
    }
    for k, v in default_settings.items():
        cur.execute("INSERT OR IGNORE INTO settings (key, value) VALUES (?, ?)", (k, v))

    # Seed bank accounts from iban_config.json
    config_path = ROOT / "iban_config.json"
    if config_path.is_file():
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                cfg = json.load(f)
            holder = cfg.get("accountHolder", "Levent Tanrıver")
            banks = cfg.get("banks", {})
            order = 0
            for b_id, b_data in banks.items():
                order += 1
                b_name = b_data.get("name", b_id.upper())
                b_iban = b_data.get("iban", "")
                b_holder = b_data.get("holder", holder)
                cur.execute(
                    """INSERT OR IGNORE INTO bank_accounts (bank_id, bank_name, iban, holder_name, is_active, display_order)
                       VALUES (?, ?, ?, ?, 1, ?)""",
                    (b_id, b_name, b_iban, b_holder, order)
                )
        except Exception as e:
            print("Error seeding bank accounts:", e)

    conn.commit()
    conn.close()


def verify_admin(username, password) -> bool:
    conn = get_db()
    cur = conn.cursor()
    pwd_hash = hash_password(password)
    cur.execute(
        "SELECT id FROM admin_users WHERE username = ? AND password_hash = ?",
        (username, pwd_hash)
    )
    row = cur.fetchone()
    conn.close()
    return bool(row)


def update_admin_password(username, new_password) -> bool:
    conn = get_db()
    cur = conn.cursor()
    pwd_hash = hash_password(new_password)
    cur.execute(
        "UPDATE admin_users SET password_hash = ? WHERE username = ?",
        (pwd_hash, username)
    )
    changed = cur.rowcount > 0
    conn.commit()
    conn.close()
    return changed


def get_all_banks():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM bank_accounts ORDER BY display_order ASC, bank_name ASC")
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


def get_active_bank(bank_id=None):
    conn = get_db()
    cur = conn.cursor()

    # Kullanıcı belirli bir bankayı seçtiğinde, o bankanın KENDİ IBAN ve Hesap Sahibini getir
    if bank_id:
        cur.execute("SELECT * FROM bank_accounts WHERE bank_id = ? AND is_active = 1", (bank_id,))
        row = cur.fetchone()
        if row:
            conn.close()
            return dict(row)

    # Seçim yoksa varsayılan bankayı veya ilk aktif bankayı getir
    cur.execute("SELECT value FROM settings WHERE key = 'default_bank'")
    s_row = cur.fetchone()
    def_id = s_row["value"] if s_row else "denizbank"

    cur.execute("SELECT * FROM bank_accounts WHERE bank_id = ? AND is_active = 1", (def_id,))
    default_row = cur.fetchone()
    if default_row:
        conn.close()
        return dict(default_row)

    cur.execute("SELECT * FROM bank_accounts WHERE is_active = 1 ORDER BY display_order ASC LIMIT 1")
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None


def sync_config_file():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM bank_accounts ORDER BY display_order ASC")
        banks = [dict(r) for r in cur.fetchall()]
        cur.execute("SELECT key, value FROM settings")
        settings = {r["key"]: r["value"] for r in cur.fetchall()}
        conn.close()
        
        cfg = {
            "accountHolder": settings.get("default_holder", "Levent Tanrıver"),
            "defaultBank": settings.get("default_bank", "denizbank"),
            "banks": {
                b["bank_id"]: {
                    "name": b["bank_name"],
                    "iban": b["iban"],
                    "holder": b["holder_name"]
                }
                for b in banks
            }
        }
        config_path = ROOT / "iban_config.json"
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(cfg, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("sync_config_file error:", e)


def update_bank(bank_id, iban, holder_name, is_active=1, bank_name=None):
    conn = get_db()
    cur = conn.cursor()
    if bank_name:
        cur.execute("""
            UPDATE bank_accounts
            SET iban = ?, holder_name = ?, is_active = ?, bank_name = ?, updated_at = CURRENT_TIMESTAMP
            WHERE bank_id = ?
        """, (iban, holder_name, int(is_active), bank_name, bank_id))
    else:
        cur.execute("""
            UPDATE bank_accounts
            SET iban = ?, holder_name = ?, is_active = ?, updated_at = CURRENT_TIMESTAMP
            WHERE bank_id = ?
        """, (iban, holder_name, int(is_active), bank_id))

    conn.commit()
    conn.close()
    sync_config_file()
    return True


def add_bank(bank_id, bank_name, iban, holder_name, is_active=1):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO bank_accounts (bank_id, bank_name, iban, holder_name, is_active)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(bank_id) DO UPDATE SET
            bank_name = excluded.bank_name,
            iban = excluded.iban,
            holder_name = excluded.holder_name,
            is_active = excluded.is_active,
            updated_at = CURRENT_TIMESTAMP
    """, (bank_id, bank_name, iban, holder_name, int(is_active)))

    conn.commit()
    conn.close()
    sync_config_file()
    return True


def delete_bank(bank_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM bank_accounts WHERE bank_id = ?", (bank_id,))
    conn.commit()
    conn.close()
    sync_config_file()
    return True


def set_default_bank(bank_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM bank_accounts WHERE bank_id = ?", (bank_id,))
    bank = cur.fetchone()
    if bank:
        cur.execute("INSERT INTO settings (key, value) VALUES ('default_bank', ?) ON CONFLICT(key) DO UPDATE SET value = excluded.value", (bank_id,))
    conn.commit()
    conn.close()
    sync_config_file()
    return True


def apply_to_all_banks(iban=None, holder_name=None, source_bank_id=None, set_default=False):
    conn = get_db()
    cur = conn.cursor()
    updates = []
    params = []
    if iban and iban.strip():
        updates.append("iban = ?")
        params.append(iban.strip())
    if holder_name and holder_name.strip():
        updates.append("holder_name = ?")
        params.append(holder_name.strip())
    
    if updates:
        updates.append("updated_at = CURRENT_TIMESTAMP")
        cur.execute(f"UPDATE bank_accounts SET {', '.join(updates)}", params)
        if holder_name and holder_name.strip():
            cur.execute("INSERT INTO settings (key, value) VALUES ('default_holder', ?) ON CONFLICT(key) DO UPDATE SET value = excluded.value", (holder_name.strip(),))
    
    if source_bank_id and set_default:
        cur.execute("INSERT INTO settings (key, value) VALUES ('default_bank', ?) ON CONFLICT(key) DO UPDATE SET value = excluded.value", (source_bank_id,))
        
    conn.commit()
    conn.close()
    sync_config_file()
    return True


def get_settings():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT key, value FROM settings")
    s = {r["key"]: r["value"] for r in cur.fetchall()}
    conn.close()
    return s


def update_setting(key, value):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO settings (key, value) VALUES (?, ?) ON CONFLICT(key) DO UPDATE SET value = excluded.value", (key, value))
    conn.commit()
    conn.close()
    sync_config_file()
    return True


def add_payment(username, bank_id, bank_name, amount, holder_name, iban):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO payments (username, bank_id, bank_name, amount, holder_name, iban, status)
        VALUES (?, ?, ?, ?, ?, ?, 'pending')
    """, (username, bank_id, bank_name, float(amount), holder_name, iban))
    new_id = cur.lastrowid
    conn.commit()
    conn.close()
    return new_id


def get_payments(limit=100):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM payments ORDER BY id DESC LIMIT ?", (limit,))
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


def update_payment_status(payment_id, status):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE payments SET status = ? WHERE id = ?", (status, payment_id))
    conn.commit()
    conn.close()
    return True


def get_user_balance(username):
    if not username:
        return 0.0
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT COALESCE(SUM(amount), 0.0) as balance
        FROM payments
        WHERE LOWER(username) = LOWER(?) AND status = 'approved'
    """, (str(username).strip(),))
    row = cur.fetchone()
    bal = float(row["balance"]) if row and row["balance"] is not None else 0.0
    conn.close()
    return bal


def get_stats():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) as total_banks, SUM(CASE WHEN is_active=1 THEN 1 ELSE 0 END) as active_banks FROM bank_accounts")
    b_stats = cur.fetchone()

    cur.execute("SELECT COUNT(*) as total_payments, SUM(amount) as total_volume, SUM(CASE WHEN status='approved' THEN amount ELSE 0 END) as approved_volume, SUM(CASE WHEN status='pending' THEN 1 ELSE 0 END) as pending_count FROM payments")
    p_stats = cur.fetchone()

    conn.close()
    return {
        "total_banks": b_stats["total_banks"] or 0,
        "active_banks": b_stats["active_banks"] or 0,
        "total_payments": p_stats["total_payments"] or 0,
        "total_volume": p_stats["total_volume"] or 0.0,
        "approved_volume": p_stats["approved_volume"] or 0.0,
        "pending_count": p_stats["pending_count"] or 0
    }


# Initialize DB immediately on load
init_db()
