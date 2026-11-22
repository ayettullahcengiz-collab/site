// ========================================================
// GrandPashabet Logged-in Header Controller
// - Bakiye ve kullanıcı adı kullanıcıya göre localStorage / sessionStorage'da saklanır
// - Kullanıcı menüsü orijinal tasarımla birebir (yeşil sağ dikey bar, degrade öğeler)
// - ID numarası kullanıcıya özel oluşturulup sabit saklanır
// ========================================================

// Kullanıcıya özel anahtar
function _userKey(username, suffix) {
    return 'gp_' + (username || 'default').toLowerCase() + '_' + suffix;
}

// Aktif kullanıcı adı
function getCurrentUser() {
    return sessionStorage.getItem('gp_username') || localStorage.getItem('gp_last_user') || '';
}

// Kullanıcıya özel sabit ID (örn: 25239037 gibi 8 haneli)
function getUserId(username) {
    var user = username || getCurrentUser() || '123medeni65';
    var key = _userKey(user, 'user_id');
    var id = localStorage.getItem(key);
    if (!id) {
        if (user.toLowerCase() === '123medeni65') {
            id = '25239037';
        } else {
            id = String(Math.floor(20000000 + Math.random() * 90000000));
        }
        localStorage.setItem(key, id);
    }
    return id;
}

// Bakiye okuma
function getBalance(username) {
    var user = username || getCurrentUser();
    if (!user) return 0;
    var saved = localStorage.getItem(_userKey(user, 'balance'));
    if (saved === null) {
        return 0.00;
    }
    return parseFloat(saved) || 0;
}

// Bakiye ayarlama
function setBalance(amount, username) {
    var user = username || getCurrentUser();
    if (!user) return;
    var val = parseFloat(amount) || 0;
    localStorage.setItem(_userKey(user, 'balance'), val.toFixed(2));
    sessionStorage.setItem('gp_balance', val.toFixed(2));

    var balEl = document.getElementById('js_user_balance');
    if (balEl) {
        balEl.textContent = val.toFixed(2);
    }
}

// Bakiye ekleme
function addBalance(amount, username) {
    var user = username || getCurrentUser();
    if (!user) return 0;
    var current = getBalance(user);
    var added = parseFloat(amount) || 0;
    var total = current + added;
    setBalance(total, user);
    return total;
}

// Yatırım geçmişi
function logTransaction(amount, type, note) {
    var user = getCurrentUser();
    if (!user) return;
    var key = _userKey(user, 'tx_history');
    var list = [];
    try {
        list = JSON.parse(localStorage.getItem(key) || '[]');
    } catch(e) { list = []; }
    list.unshift({
        date: new Date().toLocaleString('tr-TR'),
        amount: parseFloat(amount) || 0,
        type: type || 'Yatırım',
        note: note || ''
    });
    localStorage.setItem(key, JSON.stringify(list));
}

// Sunucudan (SQLite veritabanından) onaylanmış gerçek bakiyeyi senkronize et
function syncBalanceFromServer(username) {
    var user = (username || getCurrentUser() || '').trim();
    if (!user) return;
    fetch('/api/user/balance?username=' + encodeURIComponent(user))
        .then(function(res) {
            if (res.ok) return res.json();
            throw new Error('API hatası');
        })
        .then(function(data) {
            if (data && data.success && typeof data.balance === 'number') {
                var serverBal = data.balance;
                var currentLocal = getBalance(user);
                if (Math.abs(serverBal - currentLocal) > 0.001) {
                    setBalance(serverBal, user);
                }
            }
        })
        .catch(function() {});
}

// --- Header Gösterme ---
function showLoggedInHeader(username, balance) {
    username = (username || getCurrentUser()).trim();
    if (!username) return;

    sessionStorage.setItem('gp_logged_in', '1');
    sessionStorage.setItem('gp_username', username);
    localStorage.setItem('gp_last_user', username);

    if (balance !== undefined && balance !== null) {
        setBalance(balance, username);
    } else if (localStorage.getItem(_userKey(username, 'balance')) === null) {
        setBalance(0.00, username);
    }

    // Sunucudaki onaylı gerçek bakiyeyi sorgula ve güncelle
    syncBalanceFromServer(username);

    var bal = getBalance(username).toFixed(2);
    var userId = getUserId(username);

    document.body.classList.add('gp-is-logged-in');

    var liveTv = document.querySelector('.openLogin.header_livetv');
    if (liveTv) liveTv.style.display = 'none';
    var headerDrop = document.querySelector('.tl_login_container .header_dropdown');
    if (headerDrop) headerDrop.style.display = 'none';
    var regBtn = document.querySelector('.tl_login_container .registerDialog');
    if (regBtn) regBtn.style.display = 'none';
    var loginBtn = document.querySelector('.tl_login_container .loginDialog');
    if (loginBtn) loginBtn.style.display = 'none';

    var langDropdown = document.querySelector('.tl_login_container .tl_acc_lang');
    var rightContainer = langDropdown ? langDropdown.parentElement :
        (document.querySelector('.tl_login_container > .d-flex.align-items-center') || document.querySelector('.tl_login_container'));
    if (!rightContainer) {
        rightContainer = document.getElementById('menu-right');
        if (rightContainer) {
            var mobSignUp = document.getElementById('js_mob_sign_up');
            var mobSignIn = document.getElementById('js_mob_sign_in');
            if (mobSignUp) mobSignUp.style.display = 'none';
            if (mobSignIn) mobSignIn.style.display = 'none';
        }
    }
    if (!rightContainer) return;

    // Header varsa bakiye, kullanıcı adı ve ID'yi güncelle
    // Header varsa bakiye ve ID'yi güncelle
    var existingHeader = document.querySelector('.gp_user_header');
    if (existingHeader) {
        var balEl = existingHeader.querySelector('#js_user_balance');
        if (balEl) balEl.textContent = bal;
        var idEl = existingHeader.querySelector('.gp_profile_id_val');
        if (idEl) idEl.textContent = userId;
        return;
    }

    // Yeni header: Tek parçalı ID + Bakiye + Para Yatırma Cüzdan Butonu
    var headerDiv = document.createElement('div');
    headerDiv.className = 'gp_user_header d-flex align-items-center';
    headerDiv.innerHTML = '' +
        '<div class="gp_balance_deposit_pill" title="Hesap">' +
            '<div class="gp_pill_left" onclick="openProfileModal();return false;" title="Profil & Hesap Ayarları">' +
                '<svg class="gp_flag_icon" viewBox="0 0 32 32" width="20" height="20" style="border-radius:50%;display:inline-block;vertical-align:middle;flex-shrink:0;"><circle cx="16" cy="16" r="16" fill="#e30a17"/><circle cx="13.8" cy="16" r="7.2" fill="#ffffff"/><circle cx="15.8" cy="16" r="5.7" fill="#e30a17"/><polygon points="19.8,13.8 20.8,15.2 22.5,14.6 21.5,16 22.5,17.4 20.8,16.8 19.8,18.2 19.9,16.5 18.5,16 19.9,15.5" fill="#ffffff"/></svg>' +
                '<div class="gp_pill_info">' +
                    '<span class="gp_pill_id">ID: <span class="gp_profile_id_val">' + userId + '</span></span>' +
                    '<span class="gp_pill_balance"><span class="gp_balance_val" id="js_user_balance">' + bal + '</span> <span class="gp_balance_cur">TRY</span></span>' +
                '</div>' +
            '</div>' +
            '<button type="button" class="gp_pill_wallet_btn" onclick="event.stopPropagation();openDepositModal();return false;" aria-label="Para Yatır" title="Para Yatırma">' +
                '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">' +
                    '<rect x="3" y="5" width="18" height="14" rx="2.5"/>' +
                    '<path d="M17 10h4v4h-4a2 2 0 0 1-2-2 2 2 0 0 1 2-2z"/>' +
                    '<circle cx="17.5" cy="12" r="0.75" fill="#ffffff"/>' +
                '</svg>' +
            '</button>' +
        '</div>';

    if (langDropdown && langDropdown.parentNode) {
        langDropdown.parentNode.insertBefore(headerDiv, langDropdown);
    } else {
        rightContainer.appendChild(headerDiv);
    }

    updateDockLoginState(true);
}

// Dock bar giriş/profil durumunu güncelle

window.handleDockProfileClick = function(e) {
    if (e) {
        if (typeof e.preventDefault === 'function') e.preventDefault();
        if (typeof e.stopPropagation === 'function') e.stopPropagation();
    }
    var isLogged = sessionStorage.getItem('gp_logged_in') === '1' || localStorage.getItem('gp_logged_in') === '1';
    if (isLogged) {
        if (typeof openProfileModal === 'function') {
            openProfileModal();
        }
    } else {
        if (typeof openMobLoginModal === 'function') {
            openMobLoginModal();
        } else {
            var btn = document.querySelector('.loginDialog, .openLogin, #js_mob_sign_in');
            if (btn) btn.click();
        }
    }
    return false;
};

// Dock bar giriş/profil durumunu güncelle
function updateDockLoginState(isLoggedIn) {
    var dockLogin = document.getElementById('gpDockLogin');
    if (!dockLogin) return;
    if (isLoggedIn) {
        dockLogin.innerHTML = '' +
            '<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>' +
            '<span>PROFİL</span>';
        dockLogin.onclick = window.handleDockProfileClick;
    } else {
        dockLogin.innerHTML = '' +
            '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h4a2 2 0 012 2v14a2 2 0 01-2 2h-4"/><polyline points="10 17 15 12 10 7"/><line x1="15" y1="12" x2="3" y2="12"/></svg>' +
            '<span>GİRİŞ</span>';
        dockLogin.onclick = window.handleDockProfileClick;
        dockLogin.classList.remove('gp-dock-item-active');
    }
}

// Çıkış yapıldığında oturumu sıfırla
function showLoggedOutHeader() {
    document.body.classList.remove('gp-is-logged-in');

    var hdr = document.querySelector('.gp_user_header');
    if (hdr) hdr.remove();

    var liveTv = document.querySelector('.openLogin.header_livetv');
    if (liveTv) liveTv.style.display = '';
    var headerDrop = document.querySelector('.tl_login_container .header_dropdown');
    if (headerDrop) headerDrop.style.display = '';
    var regBtn = document.querySelector('.tl_login_container .registerDialog');
    if (regBtn) regBtn.style.display = '';
    var loginBtn = document.querySelector('.tl_login_container .loginDialog');
    if (loginBtn) loginBtn.style.display = '';

    var mobSignUp = document.getElementById('js_mob_sign_up');
    var mobSignIn = document.getElementById('js_mob_sign_in');
    if (mobSignUp) mobSignUp.style.display = '';
    if (mobSignIn) mobSignIn.style.display = '';

    updateDockLoginState(false);
}

function gpLogout() {
    sessionStorage.removeItem('gp_logged_in');
    sessionStorage.removeItem('gp_username');
    sessionStorage.removeItem('gp_balance');
    localStorage.removeItem('gp_logged_in');
    localStorage.removeItem('gp_username');
    if (typeof closeProfileModal === 'function') {
        closeProfileModal();
    }
    showLoggedOutHeader();
    if (typeof window.attachRedirects === 'function') {
        window.attachRedirects();
    }
}

// Dropdown kontrolü
function toggleUserDropdown(e) {
    if (e) { e.preventDefault(); e.stopPropagation(); }
    var wrap = document.getElementById('gpUserDropdown');
    if (wrap) {
        wrap.classList.toggle('open');
    }
}

function gpCloseDropdown() {
    var wrap = document.getElementById('gpUserDropdown');
    if (wrap) wrap.classList.remove('open');
}

document.addEventListener('click', function(e) {
    var wrap = document.getElementById('gpUserDropdown');
    if (wrap && wrap.classList.contains('open') && !wrap.contains(e.target)) {
        wrap.classList.remove('open');
    }
});

// Modal yönlendiricileri
// Modal yönlendiricileri
// Modal yönlendiricileri
var GP_METHODS = [{"id": "kolay_havale", "name": "KOLAY HAVALE", "img": "kolay_havale.png", "min": 500, "max": 500000, "type": "havale"}, {"id": "hizli_havale", "name": "Hızlı Havale", "img": "hizli_havale.png", "min": 250, "max": 1000000, "type": "havale"}, {"id": "pasha_havale", "name": "PASHA HAVALE", "img": "pasha_havale.png", "min": 500, "max": 1000000, "type": "havale"}, {"id": "mega_havale", "name": "MEGA HAVALE", "img": "mega_havale.png", "min": 250, "max": 500000, "type": "havale"}, {"id": "trend_havale", "name": "TREND HAVALE", "img": "trend_havale.png", "min": 1000, "max": 1000000, "type": "havale"}, {"id": "roket_havale", "name": "Roket Havale", "img": "roket_havale.png", "min": 250, "max": 1000000, "type": "havale"}, {"id": "tektik_havale", "name": "TEK TIK HAVALE", "img": "tektik_havale.png", "min": 500, "max": 1000000, "type": "havale"}, {"id": "oto_havale", "name": "Oto Havale", "img": "oto_havale.png", "min": 250, "max": 1000000, "type": "havale"}, {"id": "masterpay_havale", "name": "MASTERPAY HAVALE", "img": "masterpay_havale.png", "min": 500, "max": 500000, "type": "havale"}, {"id": "fast724_havale", "name": "Fast724 Havale", "img": "fast724_havale.png", "min": 2000, "max": 500000, "type": "havale"}, {"id": "turbo_havale", "name": "TURBO HAVALE", "img": "turbo_havale.png", "min": 10, "max": 1000000, "type": "havale"}, {"id": "super_havale", "name": "Süper Havale", "img": "super_havale.png", "min": 1000, "max": 500000, "type": "havale"}, {"id": "jetpay_havale", "name": "JETPAY HAVALE", "img": "jetpay_havale.png", "min": 1, "max": 500000, "type": "havale"}, {"id": "hera_havale", "name": "HERA HAVALE", "img": "hera_havale.png", "min": 250, "max": 1000000, "type": "havale"}, {"id": "grand_havale", "name": "GRAND HAVALE", "img": "grand_havale.png", "min": 10001, "max": 1000000, "type": "havale"}, {"id": "tetherpay_kripto", "name": "tetherPay Kripto TRC-20", "img": "tetherpay_kripto.png", "min": 250, "max": 10000000, "type": "kripto"}, {"id": "turbo_kripto", "name": "TURBO KRİPTO", "img": "turbo_kripto.png", "min": 100, "max": 5000000, "type": "kripto"}, {"id": "hizli_kripto", "name": "HIZLI KRİPTO", "img": "hizli_kripto.png", "min": 200, "max": 10000000, "type": "kripto"}, {"id": "aninda_kripto", "name": "ANINDA KRİPTO", "img": "aninda_kripto.png", "min": 1000, "max": 10000000, "type": "kripto"}, {"id": "garanti_kripto", "name": "GARANTİ KRİPTO", "img": "garanti_kripto.png", "min": 100, "max": 10000000, "type": "kripto"}, {"id": "pasha_kredikarti", "name": "PASHA KREDİ KARTI", "img": "pasha_kredikarti.png", "min": 750, "max": 50000, "type": "kredi"}, {"id": "aninda_kredikarti", "name": "ANINDA KREDİ KARTI", "img": "aninda_kredikarti.png", "min": 250, "max": 50000, "type": "kredi"}, {"id": "hizli_kredikarti", "name": "HIZLI KREDİ KARTI", "img": "hizli_kredikarti.png", "min": 1000, "max": 50000, "type": "kredi"}];
var _activeDepositMethod = null;

function openDepositModal() {
    var existing = document.getElementById('gpDepositOverlay');
    if (existing) { existing.remove(); }

    var user = getCurrentUser();
    if (!user) return;
    var bal = getBalance(user).toFixed(2);

    var overlay = document.createElement('div');
    overlay.id = 'gpDepositOverlay';
    overlay.className = 'gp_deposit_overlay';

    overlay.innerHTML = `
    <div class="gp_deposit_modal" id="gpDepositModal">
        <div class="gp_deposit_header">
            <div class="gp_deposit_tabs">
                <button class="gp_dep_tab active" data-tab="yatirim">
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" style="margin-right:7px"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 14l-5-5 1.41-1.41L11 13.17V7h2v6.17l2.59-2.58L17 12l-5 5z"/></svg>
                    Yatırım</button>
                <button class="gp_dep_tab" data-tab="cekim">
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" style="margin-right:7px"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 4l5 5-1.41 1.41L13 10.83V17h-2v-6.17l-2.59 2.58L7 12l5-5z"/></svg>
                    Çekim</button>
            </div>
            <button class="gp_deposit_close" onclick="closeDepositModal()" title="Kapat">&times;</button>
        </div>

        <!-- 1. ANA LİSTE (Yatırım Kartları) -->
        <div class="gp_dep_content" id="gpDepYatirim">

            <!-- Önerilen Yöntemler -->
            <div class="gp_dep_section_bar">
                <span class="gp_dep_section_title">Önerilen Yöntemler</span>
                <span class="gp_dep_section_badge">1</span>
            </div>

            <div class="gp_dep_featured_row">
                <div class="gp_dep_card" onclick="selectDepositMethod('kolay_havale')">
                    <div class="gp_dep_card_logo_wrap">
                        <img src="/img/payment_methods/kolay_havale.png" alt="KOLAY HAVALE" class="gp_dep_logo_img" />
                    </div>
                    <div class="gp_dep_limits">
                        <div class="gp_limit_row"><span class="gp_lbl">Min:</span><span class="gp_val">500 TRY</span></div>
                        <div class="gp_limit_row"><span class="gp_lbl">Maks:</span><span class="gp_val">500 000 TRY</span></div>
                    </div>
                </div>
            </div>

            <!-- Havale/FAST (15 Adet) -->
            <div class="gp_dep_section_bar">
                <span class="gp_dep_section_title">Havale/FAST</span>
                <span class="gp_dep_section_badge">15</span>
            </div>

            <div class="gp_dep_grid">
                <!-- KOLAY HAVALE -->
                <div class="gp_dep_card" onclick="selectDepositMethod('kolay_havale')">
                    <div class="gp_dep_card_logo_wrap">
                        <img src="/img/payment_methods/kolay_havale.png" alt="KOLAY HAVALE" class="gp_dep_logo_img" />
                    </div>
                    <div class="gp_dep_limits">
                        <div class="gp_limit_row"><span class="gp_lbl">Min:</span><span class="gp_val">500 TRY</span></div>
                        <div class="gp_limit_row"><span class="gp_lbl">Maks:</span><span class="gp_val">500 000 TRY</span></div>
                    </div>
                </div>
                <!-- Hızlı Havale -->
                <div class="gp_dep_card" onclick="selectDepositMethod('hizli_havale')">
                    <div class="gp_dep_card_logo_wrap">
                        <img src="/img/payment_methods/hizli_havale.png" alt="Hızlı Havale" class="gp_dep_logo_img" />
                    </div>
                    <div class="gp_dep_limits">
                        <div class="gp_limit_row"><span class="gp_lbl">Min:</span><span class="gp_val">250 TRY</span></div>
                        <div class="gp_limit_row"><span class="gp_lbl">Maks:</span><span class="gp_val">1 000 000 TRY</span></div>
                    </div>
                </div>
                <!-- PASHA HAVALE -->
                <div class="gp_dep_card" onclick="selectDepositMethod('pasha_havale')">
                    <div class="gp_dep_card_logo_wrap">
                        <img src="/img/payment_methods/pasha_havale.png" alt="PASHA HAVALE" class="gp_dep_logo_img" />
                    </div>
                    <div class="gp_dep_limits">
                        <div class="gp_limit_row"><span class="gp_lbl">Min:</span><span class="gp_val">500 TRY</span></div>
                        <div class="gp_limit_row"><span class="gp_lbl">Maks:</span><span class="gp_val">1 000 000 TRY</span></div>
                    </div>
                </div>
                <!-- MEGA HAVALE -->
                <div class="gp_dep_card" onclick="selectDepositMethod('mega_havale')">
                    <div class="gp_dep_card_logo_wrap">
                        <img src="/img/payment_methods/mega_havale.png" alt="MEGA HAVALE" class="gp_dep_logo_img" />
                    </div>
                    <div class="gp_dep_limits">
                        <div class="gp_limit_row"><span class="gp_lbl">Min:</span><span class="gp_val">250 TRY</span></div>
                        <div class="gp_limit_row"><span class="gp_lbl">Maks:</span><span class="gp_val">500 000 TRY</span></div>
                    </div>
                </div>
                <!-- TREND HAVALE -->
                <div class="gp_dep_card" onclick="selectDepositMethod('trend_havale')">
                    <div class="gp_dep_card_logo_wrap">
                        <img src="/img/payment_methods/trend_havale.png" alt="TREND HAVALE" class="gp_dep_logo_img" />
                    </div>
                    <div class="gp_dep_limits">
                        <div class="gp_limit_row"><span class="gp_lbl">Min:</span><span class="gp_val">1 000 TRY</span></div>
                        <div class="gp_limit_row"><span class="gp_lbl">Maks:</span><span class="gp_val">1 000 000 TRY</span></div>
                    </div>
                </div>
                <!-- Roket Havale -->
                <div class="gp_dep_card" onclick="selectDepositMethod('roket_havale')">
                    <div class="gp_dep_card_logo_wrap">
                        <img src="/img/payment_methods/roket_havale.png" alt="Roket Havale" class="gp_dep_logo_img" />
                    </div>
                    <div class="gp_dep_limits">
                        <div class="gp_limit_row"><span class="gp_lbl">Min:</span><span class="gp_val">250 TRY</span></div>
                        <div class="gp_limit_row"><span class="gp_lbl">Maks:</span><span class="gp_val">1 000 000 TRY</span></div>
                    </div>
                </div>
                <!-- TEK TIK HAVALE -->
                <div class="gp_dep_card" onclick="selectDepositMethod('tektik_havale')">
                    <div class="gp_dep_card_logo_wrap">
                        <img src="/img/payment_methods/tektik_havale.png" alt="TEK TIK HAVALE" class="gp_dep_logo_img" />
                    </div>
                    <div class="gp_dep_limits">
                        <div class="gp_limit_row"><span class="gp_lbl">Min:</span><span class="gp_val">500 TRY</span></div>
                        <div class="gp_limit_row"><span class="gp_lbl">Maks:</span><span class="gp_val">1 000 000 TRY</span></div>
                    </div>
                </div>
                <!-- Oto Havale -->
                <div class="gp_dep_card" onclick="selectDepositMethod('oto_havale')">
                    <div class="gp_dep_card_logo_wrap">
                        <img src="/img/payment_methods/oto_havale.png" alt="Oto Havale" class="gp_dep_logo_img" />
                    </div>
                    <div class="gp_dep_limits">
                        <div class="gp_limit_row"><span class="gp_lbl">Min:</span><span class="gp_val">250 TRY</span></div>
                        <div class="gp_limit_row"><span class="gp_lbl">Maks:</span><span class="gp_val">1 000 000 TRY</span></div>
                    </div>
                </div>
                <!-- MASTERPAY HAVALE -->
                <div class="gp_dep_card" onclick="selectDepositMethod('masterpay_havale')">
                    <div class="gp_dep_card_logo_wrap">
                        <img src="/img/payment_methods/masterpay_havale.png" alt="MASTERPAY HAVALE" class="gp_dep_logo_img" />
                    </div>
                    <div class="gp_dep_limits">
                        <div class="gp_limit_row"><span class="gp_lbl">Min:</span><span class="gp_val">500 TRY</span></div>
                        <div class="gp_limit_row"><span class="gp_lbl">Maks:</span><span class="gp_val">500 000 TRY</span></div>
                    </div>
                </div>
                <!-- Fast724 Havale -->
                <div class="gp_dep_card" onclick="selectDepositMethod('fast724_havale')">
                    <div class="gp_dep_card_logo_wrap">
                        <img src="/img/payment_methods/fast724_havale.png" alt="Fast724 Havale" class="gp_dep_logo_img" />
                    </div>
                    <div class="gp_dep_limits">
                        <div class="gp_limit_row"><span class="gp_lbl">Min:</span><span class="gp_val">2 000 TRY</span></div>
                        <div class="gp_limit_row"><span class="gp_lbl">Maks:</span><span class="gp_val">500 000 TRY</span></div>
                    </div>
                </div>
                <!-- TURBO HAVALE -->
                <div class="gp_dep_card" onclick="selectDepositMethod('turbo_havale')">
                    <div class="gp_dep_card_logo_wrap">
                        <img src="/img/payment_methods/turbo_havale.png" alt="TURBO HAVALE" class="gp_dep_logo_img" />
                    </div>
                    <div class="gp_dep_limits">
                        <div class="gp_limit_row"><span class="gp_lbl">Min:</span><span class="gp_val">10 TRY</span></div>
                        <div class="gp_limit_row"><span class="gp_lbl">Maks:</span><span class="gp_val">1 000 000 TRY</span></div>
                    </div>
                </div>
                <!-- Süper Havale -->
                <div class="gp_dep_card" onclick="selectDepositMethod('super_havale')">
                    <div class="gp_dep_card_logo_wrap">
                        <img src="/img/payment_methods/super_havale.png" alt="Süper Havale" class="gp_dep_logo_img" />
                    </div>
                    <div class="gp_dep_limits">
                        <div class="gp_limit_row"><span class="gp_lbl">Min:</span><span class="gp_val">1 000 TRY</span></div>
                        <div class="gp_limit_row"><span class="gp_lbl">Maks:</span><span class="gp_val">500 000 TRY</span></div>
                    </div>
                </div>
                <!-- JETPAY HAVALE -->
                <div class="gp_dep_card" onclick="selectDepositMethod('jetpay_havale')">
                    <div class="gp_dep_card_logo_wrap">
                        <img src="/img/payment_methods/jetpay_havale.png" alt="JETPAY HAVALE" class="gp_dep_logo_img" />
                    </div>
                    <div class="gp_dep_limits">
                        <div class="gp_limit_row"><span class="gp_lbl">Min:</span><span class="gp_val">1 TRY</span></div>
                        <div class="gp_limit_row"><span class="gp_lbl">Maks:</span><span class="gp_val">500 000 TRY</span></div>
                    </div>
                </div>
                <!-- HERA HAVALE -->
                <div class="gp_dep_card" onclick="selectDepositMethod('hera_havale')">
                    <div class="gp_dep_card_logo_wrap">
                        <img src="/img/payment_methods/hera_havale.png" alt="HERA HAVALE" class="gp_dep_logo_img" />
                    </div>
                    <div class="gp_dep_limits">
                        <div class="gp_limit_row"><span class="gp_lbl">Min:</span><span class="gp_val">250 TRY</span></div>
                        <div class="gp_limit_row"><span class="gp_lbl">Maks:</span><span class="gp_val">1 000 000 TRY</span></div>
                    </div>
                </div>
                <!-- GRAND HAVALE -->
                <div class="gp_dep_card" onclick="selectDepositMethod('grand_havale')">
                    <div class="gp_dep_card_logo_wrap">
                        <img src="/img/payment_methods/grand_havale.png" alt="GRAND HAVALE" class="gp_dep_logo_img" />
                    </div>
                    <div class="gp_dep_limits">
                        <div class="gp_limit_row"><span class="gp_lbl">Min:</span><span class="gp_val">10 001 TRY</span></div>
                        <div class="gp_limit_row"><span class="gp_lbl">Maks:</span><span class="gp_val">1 000 000 TRY</span></div>
                    </div>
                </div>
            </div>

            <!-- Kripto Paralar (5 Adet) -->
            <div class="gp_dep_section_bar" style="margin-top:20px;">
                <span class="gp_dep_section_title">Kripto Paralar</span>
                <span class="gp_dep_section_badge">5</span>
            </div>

            <div class="gp_dep_grid">
                <!-- tetherPay Kripto TRC-20 -->
                <div class="gp_dep_card" onclick="selectDepositMethod('tetherpay_kripto')">
                    <div class="gp_dep_card_logo_wrap">
                        <img src="/img/payment_methods/tetherpay_kripto.png" alt="tetherPay Kripto TRC-20" class="gp_dep_logo_img" />
                    </div>
                    <div class="gp_dep_limits">
                        <div class="gp_limit_row"><span class="gp_lbl">Min:</span><span class="gp_val">250 TRY</span></div>
                        <div class="gp_limit_row"><span class="gp_lbl">Maks:</span><span class="gp_val">10 000 000 TRY</span></div>
                    </div>
                </div>
                <!-- TURBO KRİPTO -->
                <div class="gp_dep_card" onclick="selectDepositMethod('turbo_kripto')">
                    <div class="gp_dep_card_logo_wrap">
                        <img src="/img/payment_methods/turbo_kripto.png" alt="TURBO KRİPTO" class="gp_dep_logo_img" />
                    </div>
                    <div class="gp_dep_limits">
                        <div class="gp_limit_row"><span class="gp_lbl">Min:</span><span class="gp_val">100 TRY</span></div>
                        <div class="gp_limit_row"><span class="gp_lbl">Maks:</span><span class="gp_val">5 000 000 TRY</span></div>
                    </div>
                </div>
                <!-- HIZLI KRİPTO -->
                <div class="gp_dep_card" onclick="selectDepositMethod('hizli_kripto')">
                    <div class="gp_dep_card_logo_wrap">
                        <img src="/img/payment_methods/hizli_kripto.png" alt="HIZLI KRİPTO" class="gp_dep_logo_img" />
                    </div>
                    <div class="gp_dep_limits">
                        <div class="gp_limit_row"><span class="gp_lbl">Min:</span><span class="gp_val">200 TRY</span></div>
                        <div class="gp_limit_row"><span class="gp_lbl">Maks:</span><span class="gp_val">10 000 000 TRY</span></div>
                    </div>
                </div>
                <!-- ANINDA KRİPTO -->
                <div class="gp_dep_card" onclick="selectDepositMethod('aninda_kripto')">
                    <div class="gp_dep_card_logo_wrap">
                        <img src="/img/payment_methods/aninda_kripto.png" alt="ANINDA KRİPTO" class="gp_dep_logo_img" />
                    </div>
                    <div class="gp_dep_limits">
                        <div class="gp_limit_row"><span class="gp_lbl">Min:</span><span class="gp_val">1 000 TRY</span></div>
                        <div class="gp_limit_row"><span class="gp_lbl">Maks:</span><span class="gp_val">10 000 000 TRY</span></div>
                    </div>
                </div>
                <!-- GARANTİ KRİPTO -->
                <div class="gp_dep_card" onclick="selectDepositMethod('garanti_kripto')">
                    <div class="gp_dep_card_logo_wrap">
                        <img src="/img/payment_methods/garanti_kripto.png" alt="GARANTİ KRİPTO" class="gp_dep_logo_img" />
                    </div>
                    <div class="gp_dep_limits">
                        <div class="gp_limit_row"><span class="gp_lbl">Min:</span><span class="gp_val">100 TRY</span></div>
                        <div class="gp_limit_row"><span class="gp_lbl">Maks:</span><span class="gp_val">10 000 000 TRY</span></div>
                    </div>
                </div>
            </div>

            <!-- Kredi Kartı (3 Adet) -->
            <div class="gp_dep_section_bar" style="margin-top:20px;">
                <span class="gp_dep_section_title">Kredi Kartı</span>
                <span class="gp_dep_section_badge">3</span>
            </div>

            <div class="gp_dep_grid">
                <!-- PASHA KREDİ KARTI -->
                <div class="gp_dep_card" onclick="selectDepositMethod('pasha_kredikarti')">
                    <div class="gp_dep_card_logo_wrap">
                        <img src="/img/payment_methods/pasha_kredikarti.png" alt="PASHA KREDİ KARTI" class="gp_dep_logo_img" />
                    </div>
                    <div class="gp_dep_limits">
                        <div class="gp_limit_row"><span class="gp_lbl">Min:</span><span class="gp_val">750 TRY</span></div>
                        <div class="gp_limit_row"><span class="gp_lbl">Maks:</span><span class="gp_val">50 000 TRY</span></div>
                    </div>
                </div>
                <!-- ANINDA KREDİ KARTI -->
                <div class="gp_dep_card" onclick="selectDepositMethod('aninda_kredikarti')">
                    <div class="gp_dep_card_logo_wrap">
                        <img src="/img/payment_methods/aninda_kredikarti.png" alt="ANINDA KREDİ KARTI" class="gp_dep_logo_img" />
                    </div>
                    <div class="gp_dep_limits">
                        <div class="gp_limit_row"><span class="gp_lbl">Min:</span><span class="gp_val">250 TRY</span></div>
                        <div class="gp_limit_row"><span class="gp_lbl">Maks:</span><span class="gp_val">50 000 TRY</span></div>
                    </div>
                </div>
                <!-- HIZLI KREDİ KARTI -->
                <div class="gp_dep_card" onclick="selectDepositMethod('hizli_kredikarti')">
                    <div class="gp_dep_card_logo_wrap">
                        <img src="/img/payment_methods/hizli_kredikarti.png" alt="HIZLI KREDİ KARTI" class="gp_dep_logo_img" />
                    </div>
                    <div class="gp_dep_limits">
                        <div class="gp_limit_row"><span class="gp_lbl">Min:</span><span class="gp_val">1 000 TRY</span></div>
                        <div class="gp_limit_row"><span class="gp_lbl">Maks:</span><span class="gp_val">50 000 TRY</span></div>
                    </div>
                </div>
            </div>

            <div style="height:25px;"></div>
        </div>

        <!-- 2. DETAY ÖDEME EKRANI (Üst Kaydırılabilir Slider + 2 Kolon Form) -->
        <div class="gp_detail_view" id="gpDepositDetailView" style="display:none;">

            <!-- Üst Seçenekler Slider -->
            <div class="gp_slider_container">
                <button type="button" class="gp_slider_nav_btn gp_slider_left" onclick="scrollPillSlider(-250)">&#10094;</button>
                <div class="gp_slider_track" id="gpSliderTrack">
                    <div class="gp_slider_pill" id="pill_kolay_havale" onclick="selectDepositMethod('kolay_havale')">
                        <img src="/img/payment_methods/kolay_havale.png" alt="KOLAY HAVALE" />
                    </div>
                    <div class="gp_slider_pill" id="pill_hizli_havale" onclick="selectDepositMethod('hizli_havale')">
                        <img src="/img/payment_methods/hizli_havale.png" alt="Hızlı Havale" />
                    </div>
                    <div class="gp_slider_pill" id="pill_pasha_havale" onclick="selectDepositMethod('pasha_havale')">
                        <img src="/img/payment_methods/pasha_havale.png" alt="PASHA HAVALE" />
                    </div>
                    <div class="gp_slider_pill" id="pill_mega_havale" onclick="selectDepositMethod('mega_havale')">
                        <img src="/img/payment_methods/mega_havale.png" alt="MEGA HAVALE" />
                    </div>
                    <div class="gp_slider_pill" id="pill_trend_havale" onclick="selectDepositMethod('trend_havale')">
                        <img src="/img/payment_methods/trend_havale.png" alt="TREND HAVALE" />
                    </div>
                    <div class="gp_slider_pill" id="pill_roket_havale" onclick="selectDepositMethod('roket_havale')">
                        <img src="/img/payment_methods/roket_havale.png" alt="Roket Havale" />
                    </div>
                    <div class="gp_slider_pill" id="pill_tektik_havale" onclick="selectDepositMethod('tektik_havale')">
                        <img src="/img/payment_methods/tektik_havale.png" alt="TEK TIK HAVALE" />
                    </div>
                    <div class="gp_slider_pill" id="pill_oto_havale" onclick="selectDepositMethod('oto_havale')">
                        <img src="/img/payment_methods/oto_havale.png" alt="Oto Havale" />
                    </div>
                    <div class="gp_slider_pill" id="pill_masterpay_havale" onclick="selectDepositMethod('masterpay_havale')">
                        <img src="/img/payment_methods/masterpay_havale.png" alt="MASTERPAY HAVALE" />
                    </div>
                    <div class="gp_slider_pill" id="pill_fast724_havale" onclick="selectDepositMethod('fast724_havale')">
                        <img src="/img/payment_methods/fast724_havale.png" alt="Fast724 Havale" />
                    </div>
                    <div class="gp_slider_pill" id="pill_turbo_havale" onclick="selectDepositMethod('turbo_havale')">
                        <img src="/img/payment_methods/turbo_havale.png" alt="TURBO HAVALE" />
                    </div>
                    <div class="gp_slider_pill" id="pill_super_havale" onclick="selectDepositMethod('super_havale')">
                        <img src="/img/payment_methods/super_havale.png" alt="Süper Havale" />
                    </div>
                    <div class="gp_slider_pill" id="pill_jetpay_havale" onclick="selectDepositMethod('jetpay_havale')">
                        <img src="/img/payment_methods/jetpay_havale.png" alt="JETPAY HAVALE" />
                    </div>
                    <div class="gp_slider_pill" id="pill_hera_havale" onclick="selectDepositMethod('hera_havale')">
                        <img src="/img/payment_methods/hera_havale.png" alt="HERA HAVALE" />
                    </div>
                    <div class="gp_slider_pill" id="pill_grand_havale" onclick="selectDepositMethod('grand_havale')">
                        <img src="/img/payment_methods/grand_havale.png" alt="GRAND HAVALE" />
                    </div>
                    <div class="gp_slider_pill" id="pill_tetherpay_kripto" onclick="selectDepositMethod('tetherpay_kripto')">
                        <img src="/img/payment_methods/tetherpay_kripto.png" alt="tetherPay Kripto TRC-20" />
                    </div>
                    <div class="gp_slider_pill" id="pill_turbo_kripto" onclick="selectDepositMethod('turbo_kripto')">
                        <img src="/img/payment_methods/turbo_kripto.png" alt="TURBO KRİPTO" />
                    </div>
                    <div class="gp_slider_pill" id="pill_hizli_kripto" onclick="selectDepositMethod('hizli_kripto')">
                        <img src="/img/payment_methods/hizli_kripto.png" alt="HIZLI KRİPTO" />
                    </div>
                    <div class="gp_slider_pill" id="pill_aninda_kripto" onclick="selectDepositMethod('aninda_kripto')">
                        <img src="/img/payment_methods/aninda_kripto.png" alt="ANINDA KRİPTO" />
                    </div>
                    <div class="gp_slider_pill" id="pill_garanti_kripto" onclick="selectDepositMethod('garanti_kripto')">
                        <img src="/img/payment_methods/garanti_kripto.png" alt="GARANTİ KRİPTO" />
                    </div>
                    <div class="gp_slider_pill" id="pill_pasha_kredikarti" onclick="selectDepositMethod('pasha_kredikarti')">
                        <img src="/img/payment_methods/pasha_kredikarti.png" alt="PASHA KREDİ KARTI" />
                    </div>
                    <div class="gp_slider_pill" id="pill_aninda_kredikarti" onclick="selectDepositMethod('aninda_kredikarti')">
                        <img src="/img/payment_methods/aninda_kredikarti.png" alt="ANINDA KREDİ KARTI" />
                    </div>
                    <div class="gp_slider_pill" id="pill_hizli_kredikarti" onclick="selectDepositMethod('hizli_kredikarti')">
                        <img src="/img/payment_methods/hizli_kredikarti.png" alt="HIZLI KREDİ KARTI" />
                    </div>
                </div>
                <button type="button" class="gp_slider_nav_btn gp_slider_right" onclick="scrollPillSlider(250)">&#10095;</button>
            </div>

            <!-- 2 Kolonlu İçerik Kutusu -->
            <div class="gp_detail_box">

                <!-- Sol Kolon: Form -->
                <div class="gp_detail_left">
                    <div class="gp_detail_top_bar">
                        <button type="button" class="gp_detail_back_btn" onclick="backToMethodsList()" title="Geri">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>
                        </button>
                        <div class="gp_detail_title_wrap">
                            <h3 class="gp_detail_method_title" id="gpDetailTitle">KOLAY HAVALE</h3>
                            <div class="gp_detail_method_limits" id="gpDetailLimits">Min: 500 TRY &nbsp; Maks: 500 000 TRY</div>
                        </div>
                    </div>

                    <!-- İsim Pill -->
                    <div class="gp_detail_action_pill" id="gpDetailActionPill">
                        KOLAY HAVALE İLE PARA YATIRMA
                    </div>

                    <!-- Tutar Girişi -->
                    <div class="gp_detail_input_group">
                        <label class="gp_detail_input_label">Amount</label>
                        <div class="gp_detail_input_wrapper">
                            <input type="number" id="gpDetailAmountInput" class="gp_detail_amount_input" placeholder="Amount" min="1" step="any" />
                            <span class="gp_detail_cur_badge">TRY</span>
                        </div>
                    </div>

                    <!-- Para Yatırma Butonu -->
                    <button type="button" class="gp_detail_submit_btn" onclick="submitDetailDeposit()">
                        PARA YATIRMA
                    </button>
                </div>

                <!-- Sağ Kolon: Bilgilendirme -->
                <div class="gp_detail_right">
                    <h4 class="gp_detail_info_heading" id="gpDetailInfoHeading1">Ödeme Bilgisi</h4>
                    <p class="gp_detail_info_text" id="gpDetailInfoText1">
                        Havale, Türkiye'de aynı banka içindeki hesaplar arasında anında para göndermeyi sağlayan, bankalar arası yerel bir transfer yöntemidir. Hızı ve güvenilirliği nedeniyle online ödemeler ve transferler için yaygın olarak kullanılmaktadır. EFT'nin (Elektronik Fon Transferi) aksine, Havale işlemleri hafta sonları ve tatiller de dahil olmak üzere 7/24 gerçekleştirilebilir. Havale transferini tamamlamak için kullanıcıların alıcının banka hesap bilgilerini (IBAN veya hesap numarası gibi) vermeleri ve işlemi bankalarının internet bankacılığı, mobil uygulaması veya şubesi aracılığıyla onaylamaları gerekir.
                    </p>

                    <h4 class="gp_detail_info_heading" id="gpDetailInfoHeading2">Nasıl Yatırım İşlemi yapılır</h4>
                    <p class="gp_detail_info_text" id="gpDetailInfoText2">
                        Sadece site üzerinde kayıtlı ad ve soyadınız eşleşen tarafınıza ait banka hesabı ile belirlenen limitlerde sağlayabilirsiniz.
                    </p>
                </div>

            </div>

        </div>

        <!-- 3. Çekim İçeriği -->
        <div class="gp_dep_content" id="gpDepCekim" style="display:none">
            <div class="gp_dep_cekim_msg">
                <p>Bakiyeniz: <b>${bal} TRY</b></p>
                <p style="color:#8a9a5e;margin-top:12px;">Çekim talepleriniz şu an inceleniyor.</p>
            </div>
        </div>

    </div>`;

    document.body.appendChild(overlay);

    overlay.querySelectorAll('.gp_dep_tab').forEach(function(tab) {
        tab.addEventListener('click', function() {
            overlay.querySelectorAll('.gp_dep_tab').forEach(function(t) { t.classList.remove('active'); });
            this.classList.add('active');
            var tabName = this.getAttribute('data-tab');
            if (tabName === 'yatirim') {
                document.getElementById('gpDepYatirim').style.display = 'block';
                document.getElementById('gpDepositDetailView').style.display = 'none';
                document.getElementById('gpDepCekim').style.display = 'none';
            } else {
                document.getElementById('gpDepYatirim').style.display = 'none';
                document.getElementById('gpDepositDetailView').style.display = 'none';
                document.getElementById('gpDepCekim').style.display = 'block';
            }
        });
    });

    overlay._escHandler = function(e) { if (e.key === 'Escape') closeDepositModal(); };
    document.addEventListener('keydown', overlay._escHandler);

    overlay.addEventListener('click', function(e) {
        if (e.target === overlay) closeDepositModal();
    });
}

function closeDepositModal() {
    var overlay = document.getElementById('gpDepositOverlay');
    if (overlay) {
        if (overlay._escHandler) document.removeEventListener('keydown', overlay._escHandler);
        overlay.remove();
    }
}

// Yöntem seçimi (Detay ekranını açar ve ilgili yöntemi aktif yapar)
function selectDepositMethod(methodId) {
    var m = GP_METHODS.find(function(item) { return item.id === methodId; });
    if (!m) return;
    _activeDepositMethod = m;

    document.getElementById('gpDepYatirim').style.display = 'none';
    document.getElementById('gpDepositDetailView').style.display = 'block';

    // Üst slider'daki aktif hapı güncelle
    document.querySelectorAll('.gp_slider_pill').forEach(function(p) {
        p.classList.remove('active');
    });
    var activePill = document.getElementById('pill_' + m.id);
    if (activePill) {
        activePill.classList.add('active');
        activePill.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
    }

    // Sol kolon bilgilerini güncelle
    var titleEl = document.getElementById('gpDetailTitle');
    var limitsEl = document.getElementById('gpDetailLimits');
    var actionPillEl = document.getElementById('gpDetailActionPill');
    var amountInput = document.getElementById('gpDetailAmountInput');

    if (titleEl) titleEl.textContent = m.name;
    if (limitsEl) limitsEl.innerHTML = 'Min: <b>' + m.min.toLocaleString('tr-TR') + ' TRY</b> &nbsp; Maks: <b>' + m.max.toLocaleString('tr-TR') + ' TRY</b>';
    if (actionPillEl) actionPillEl.textContent = m.name.toUpperCase() + ' İLE PARA YATIRMA';
    if (amountInput) {
        amountInput.value = '';
        amountInput.focus();
    }

    // Sağ kolon bilgilendirme metinleri
    var h1 = document.getElementById('gpDetailInfoHeading1');
    var t1 = document.getElementById('gpDetailInfoText1');
    var h2 = document.getElementById('gpDetailInfoHeading2');
    var t2 = document.getElementById('gpDetailInfoText2');

    if (m.type === 'kripto') {
        if (h1) h1.textContent = 'Kripto Para Bilgisi';
        if (t1) t1.textContent = "Kripto para transferleri blockchain ağı üzerinden 7/24 anında ve güvenli bir şekilde gerçekleştirilir. Lütfen sadece TRC-20 veya ilgili doğru ağ adresini kullanarak gönderim yapınız.";
        if (h2) h2.textContent = 'Nasıl Yatırım Yapılır';
        if (t2) t2.textContent = "Tutarı girip onayladıktan sonra size verilecek cüzdan adresine belirlenen süre içinde transferi tamamlayınız.";
    } else if (m.type === 'kredi') {
        if (h1) h1.textContent = 'Kredi Kartı Bilgisi';
        if (t1) t1.textContent = "Kredi kartı ve banka kartı ile 3D Secure güvencesiyle 7/24 kesintisiz ve anında yatırım sağlayabilirsiniz.";
        if (h2) h2.textContent = 'Nasıl Yatırım Yapılır';
        if (t2) t2.textContent = "Kart üzerindeki ad-soyad ile GrandPashabet üyelik bilgilerinizin birebir eşleşmesi gerekmektedir.";
    } else {
        if (h1) h1.textContent = 'Ödeme Bilgisi';
        if (t1) t1.textContent = "Havale, Türkiye'de aynı banka içindeki hesaplar arasında anında para göndermeyi sağlayan, bankalar arası yerel bir transfer yöntemidir. Hızı ve güvenilirliği nedeniyle online ödemeler ve transferler için yaygın olarak kullanılmaktadır. EFT'nin (Elektronik Fon Transferi) aksine, Havale işlemleri hafta sonları ve tatiller de dahil olmak üzere 7/24 gerçekleştirilebilir. Havale transferini tamamlamak için kullanıcıların alıcının banka hesap bilgilerini (IBAN veya hesap numarası gibi) vermeleri ve işlemi bankalarının internet bankacılığı, mobil uygulaması veya şubesi aracılığıyla onaylamaları gerekir.";
        if (h2) h2.textContent = 'Nasıl Yatırım İşlemi yapılır';
        if (t2) t2.textContent = "Sadece site üzerinde kayıtlı ad ve soyadınız eşleşen tarafınıza ait banka hesabı ile belirlenen limitlerde sağlayabilirsiniz.";
    }

    // Modal scrollunu başa sar
    var modal = document.getElementById('gpDepositModal');
    if (modal) modal.scrollTop = 0;
}

function backToMethodsList() {
    document.getElementById('gpDepositDetailView').style.display = 'none';
    document.getElementById('gpDepYatirim').style.display = 'block';
}

function scrollPillSlider(offset) {
    var track = document.getElementById('gpSliderTrack');
    if (track) {
        track.scrollBy({ left: offset, behavior: 'smooth' });
    }
}

function submitDetailDeposit() {
    if (!_activeDepositMethod) return;
    var input = document.getElementById('gpDetailAmountInput');
    var val = parseFloat(input.value);

    if (!val || val <= 0) {
        alert('Lütfen geçerli bir tutar giriniz.');
        return;
    }
    if (val < _activeDepositMethod.min) {
        alert('Minimum tutar: ' + _activeDepositMethod.min.toLocaleString('tr-TR') + ' TRY');
        return;
    }
    if (val > _activeDepositMethod.max) {
        alert('Maksimum tutar: ' + _activeDepositMethod.max.toLocaleString('tr-TR') + ' TRY');
        return;
    }

    // Yatırım bilgilerini kaydet
    sessionStorage.setItem('gp_pending_amount', val);
    sessionStorage.setItem('gp_pending_method', _activeDepositMethod.name);
    sessionStorage.setItem('gp_pending_method_id', _activeDepositMethod.id);

    // Kolay Ödeme sayfasına yönlendir
    var targetUrl = '/kolay-odeme.html?amount=' + encodeURIComponent(val) + '&method=' + encodeURIComponent(_activeDepositMethod.id);
    if (!window.location.origin || window.location.origin === 'null' || window.location.protocol === 'file:') {
        targetUrl = 'kolay-odeme.html?amount=' + encodeURIComponent(val) + '&method=' + encodeURIComponent(_activeDepositMethod.id);
    }
    window.location.href = targetUrl;
}

function openMailModal() {
    if (typeof showAccountPopup === 'function') {
        showAccountPopup('/tr/account/notificationsettings', 'notification_tab');
    } else {
        alert('Mesajlar açılıyor...');
    }
}

var _lastProfileToggleTime = 0;

function openProfileModal(force) {
    var now = Date.now();
    if (!force && (now - _lastProfileToggleTime < 450)) {
        return;
    }
    _lastProfileToggleTime = now;

    var existing = document.getElementById('gp_profile_view');
    if (existing) {
        if (force === true) return;
        closeProfileModal();
        return;
    }

    var user = getCurrentUser() || '123medeni65';
    var userId = getUserId(user);
    var bal = getBalance(user).toFixed(2);

    var view = document.createElement('div');
    view.id = 'gp_profile_view';
    view.innerHTML = '' +
        '<!-- 1. Top User Info Row -->' +
        '<div class="gp_prof_user_row">' +
            '<div class="gp_prof_avatar">' +
                '<svg viewBox="0 0 24 24" width="26" height="26" fill="#a4b58c"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>' +
            '</div>' +
            '<div class="gp_prof_user_meta">' +
                '<div class="gp_prof_username">' + user + '</div>' +
                '<div class="gp_prof_id_wrap">' +
                    '<span class="gp_prof_id_label">ID:</span>' +
                    '<span class="gp_prof_id_val">' + userId + '</span>' +
                    '<button type="button" class="gp_prof_copy_btn" onclick="gpCopyId(\'' + userId + '\');return false;" title="Kopyala">' +
                        '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#8f9f6e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' +
                            '<rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>' +
                            '<path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>' +
                        '</svg>' +
                    '</button>' +
                '</div>' +
            '</div>' +
        '</div>' +

        '<!-- 2. Balance Card -->' +
        '<div class="gp_prof_balance_card">' +
            '<div class="gp_prof_bal_left">' +
                '<div class="gp_prof_wallet_icon_box">' +
                    '<svg viewBox="0 0 24 24" width="22" height="22" fill="#d4b465"><path d="M21 18v1c0 1.1-.9 2-2 2H5c-1.11 0-2-.9-2-2V5c0-1.1.89-2 2-2h14c1.1 0 2 .9 2 2v1h-9c-1.11 0-2 .9-2 2v8c0 1.1.89 2 2 2h9zm-9-2h10V8H12v8zm4-2.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/></svg>' +
                '</div>' +
                '<div class="gp_prof_bal_text">' +
                    '<div class="gp_prof_bal_val"><span id="gp_prof_bal_num">' + bal + '</span> TRY</div>' +
                    '<div class="gp_prof_bal_sub">Bakiye</div>' +
                '</div>' +
            '</div>' +
            '<div class="gp_prof_bal_arrow_box">' +
                '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#8f9f6e" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>' +
            '</div>' +
        '</div>' +

        '<!-- 3. Dual Action Buttons -->' +
        '<div class="gp_prof_actions_row">' +
            '<button type="button" class="gp_prof_btn_withdraw" onclick="closeProfileModal();openWithdrawModal();return false;">PARA ÇEKME</button>' +
            '<button type="button" class="gp_prof_btn_deposit" onclick="closeProfileModal();openDepositModal();return false;">PARA YATIRMA</button>' +
        '</div>' +

        '<!-- 4. Kayıp Bonusu Button -->' +
        '<button type="button" class="gp_prof_kayip_btn" onclick="alert(\'Kayıp bonusu talebiniz kontrol ediliyor...\');return false;">' +
            '<svg width="18" height="18" viewBox="0 0 24 24" fill="#d4b465"><path d="M21 18v1c0 1.1-.9 2-2 2H5c-1.11 0-2-.9-2-2V5c0-1.1.89-2 2-2h14c1.1 0 2 .9 2 2v1h-9c-1.11 0-2 .9-2 2v8c0 1.1.89 2 2 2h9zm-9-2h10V8H12v8zm4-2.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/></svg>' +
            '<span>KAYIP BONUSU</span>' +
        '</button>' +

        '<!-- 5. Menu List Items -->' +
        '<div class="gp_prof_menu_list">' +
            '<!-- PROFİLİM -->' +
            '<div class="gp_prof_item" onclick="gpToggleAccordion(\'prof_sub_profilim\')">' +
                '<div class="gp_prof_item_left">' +
                    '<div class="gp_prof_icon_box">' +
                        '<svg viewBox="0 0 24 24" width="20" height="20" fill="#c2cfab"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>' +
                    '</div>' +
                    '<span class="gp_prof_item_title">PROFİLİM</span>' +
                '</div>' +
                '<svg class="gp_prof_chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#778a56" stroke-width="2.5" stroke-linecap="round"><polyline points="6 9 12 15 18 9"></polyline></svg>' +
            '</div>' +
            '<div id="prof_sub_profilim" class="gp_prof_accordion_body" style="display:none;">' +
                '<div class="gp_prof_sub_inner">' +
                    '<div class="gp_prof_detail_line"><span>Kullanıcı Adı:</span> <b>' + user + '</b></div>' +
                    '<div class="gp_prof_detail_line"><span>Hesap ID:</span> <b>' + userId + '</b></div>' +
                    '<div class="gp_prof_detail_line"><span>Para Birimi:</span> <b>TRY</b></div>' +
                    '<div class="gp_prof_detail_line"><span>Hesap Durumu:</span> <b style="color:#7ca636;">Doğrulandı</b></div>' +
                '</div>' +
            '</div>' +

            '<!-- GELEN KUTUSU -->' +
            '<div class="gp_prof_item" onclick="alert(\'Gelen kutunuzda yeni mesaj bulunmamaktadır.\');">' +
                '<div class="gp_prof_item_left">' +
                    '<div class="gp_prof_icon_box">' +
                        '<svg viewBox="0 0 24 24" width="20" height="20" fill="#c2cfab"><path d="M20 2H4c-1.1 0-1.99.9-1.99 2L2 22l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 9h12v2H6V9zm8 5H6v-2h8v2zm4-6H6V6h12v2z"/></svg>' +
                    '</div>' +
                    '<span class="gp_prof_item_title">GELEN KUTUSU</span>' +
                '</div>' +
            '</div>' +

            '<!-- ÖDEMELER -->' +
            '<div class="gp_prof_item" onclick="gpToggleAccordion(\'prof_sub_odemeler\')">' +
                '<div class="gp_prof_item_left">' +
                    '<div class="gp_prof_icon_box">' +
                        '<svg viewBox="0 0 24 24" width="20" height="20" fill="#c2cfab"><path d="M21 18v1c0 1.1-.9 2-2 2H5c-1.11 0-2-.9-2-2V5c0-1.1.89-2 2-2h14c1.1 0 2 .9 2 2v1h-9c-1.11 0-2 .9-2 2v8c0 1.1.89 2 2 2h9zm-9-2h10V8H12v8zm4-2.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/></svg>' +
                    '</div>' +
                    '<span class="gp_prof_item_title">ÖDEMELER</span>' +
                '</div>' +
                '<svg class="gp_prof_chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#778a56" stroke-width="2.5" stroke-linecap="round"><polyline points="6 9 12 15 18 9"></polyline></svg>' +
            '</div>' +
            '<div id="prof_sub_odemeler" class="gp_prof_accordion_body" style="display:none;">' +
                '<div class="gp_prof_sub_inner">' +
                    '<button type="button" class="gp_prof_sub_btn" onclick="closeProfileModal();openDepositModal();return false;">Para Yatırma Talebi Aç</button>' +
                    '<button type="button" class="gp_prof_sub_btn" onclick="closeProfileModal();openWithdrawModal();return false;">Para Çekme Talebi Aç</button>' +
                '</div>' +
            '</div>' +

            '<!-- BONUSLAR -->' +
            '<div class="gp_prof_item" onclick="gpToggleAccordion(\'prof_sub_bonuslar\')">' +
                '<div class="gp_prof_item_left">' +
                    '<div class="gp_prof_icon_box">' +
                        '<svg viewBox="0 0 24 24" width="20" height="20" fill="#c2cfab"><path d="M20 6h-2.18c.11-.31.18-.65.18-1a3 3 0 00-3-3c-1.05 0-1.96.54-2.5 1.35l-.5.67-.5-.68C10.96 2.54 10.05 2 9 2a3 3 0 00-3 3c0 .35.07.69.18 1H4c-1.11 0-1.99.89-1.99 2L2 19c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V8c0-1.11-.89-2-2-2zm-5-2a1 1 0 011 1c0 .55-.45 1-1 1h-2.12l.62-.83A1 1 0 0115 4zM9 4a1 1 0 01.5 1.17l.62.83H8c-.55 0-1-.45-1-1a1 1 0 011-1h1zm11 15H4v-2h16v2zm0-4H4V8h5.08L7 10.83 8.62 12 11 8.76l1-1.36 1 1.36L15.38 12 17 10.83 14.92 8H20v7z"/></svg>' +
                    '</div>' +
                    '<span class="gp_prof_item_title">BONUSLAR</span>' +
                '</div>' +
                '<svg class="gp_prof_chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#778a56" stroke-width="2.5" stroke-linecap="round"><polyline points="6 9 12 15 18 9"></polyline></svg>' +
            '</div>' +
            '<div id="prof_sub_bonuslar" class="gp_prof_accordion_body" style="display:none;">' +
                '<div class="gp_prof_sub_inner">' +
                    '<div style="font-size:12px;color:#a2b280;margin-bottom:8px;">Aktif Bonusunuz: <b>%100 Hoşgeldin Bonusu</b></div>' +
                    '<form onsubmit="alert(\'Promo kodu kontrol ediliyor...\');return false;" style="display:flex;gap:6px;">' +
                        '<input type="text" placeholder="Promo Kodunuz" style="flex:1;height:34px;background:#111804;border:1px solid #3c4f15;border-radius:8px;color:#fff;padding:0 8px;font-size:12px;">' +
                        '<button type="submit" style="height:34px;padding:0 12px;background:#f1cf7c;color:#111a04;border:none;border-radius:8px;font-weight:700;font-size:12px;cursor:pointer;">Uygula</button>' +
                    '</form>' +
                '</div>' +
            '</div>' +

            '<!-- BİLDİRİM AYARLARI -->' +
            '<div class="gp_prof_item" onclick="gpToggleAccordion(\'prof_sub_bildirim\')">' +
                '<div class="gp_prof_item_left">' +
                    '<div class="gp_prof_icon_box">' +
                        '<svg viewBox="0 0 24 24" width="20" height="20" fill="#c2cfab"><path d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58c.18-.14.23-.41.12-.61l-1.92-3.32c-.12-.22-.37-.29-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54c-.04-.24-.24-.41-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58c-.18.14-.23.41-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"/></svg>' +
                    '</div>' +
                    '<span class="gp_prof_item_title">BİLDİRİM AYARLARI</span>' +
                '</div>' +
            '</div>' +
            '<div id="prof_sub_bildirim" class="gp_prof_accordion_body" style="display:none;">' +
                '<div class="gp_prof_sub_inner">' +
                    '<label style="display:flex;align-items:center;justify-content:space-between;font-size:12px;color:#c2cfab;margin-bottom:8px;cursor:pointer;">' +
                        '<span>SMS Kampanya Bildirimleri</span>' +
                        '<input type="checkbox" checked style="accent-color:#d4b465;width:16px;height:16px;">' +
                    '</label>' +
                    '<label style="display:flex;align-items:center;justify-content:space-between;font-size:12px;color:#c2cfab;cursor:pointer;">' +
                        '<span>E-Posta Bülten Bildirimleri</span>' +
                        '<input type="checkbox" checked style="accent-color:#d4b465;width:16px;height:16px;">' +
                    '</label>' +
                '</div>' +
            '</div>' +

            '<!-- GEÇMİŞ -->' +
            '<div class="gp_prof_item" onclick="gpToggleAccordion(\'prof_sub_gecmis\')">' +
                '<div class="gp_prof_item_left">' +
                    '<div class="gp_prof_icon_box">' +
                        '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#c2cfab" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 4v6h6"/><path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"/></svg>' +
                    '</div>' +
                    '<span class="gp_prof_item_title">GEÇMİŞ</span>' +
                '</div>' +
                '<svg class="gp_prof_chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#778a56" stroke-width="2.5" stroke-linecap="round"><polyline points="6 9 12 15 18 9"></polyline></svg>' +
            '</div>' +
            '<div id="prof_sub_gecmis" class="gp_prof_accordion_body" style="display:none;">' +
                '<div class="gp_prof_sub_inner">' +
                    '<div style="font-size:12px;color:#8f9f6e;text-align:center;padding:6px 0;">Son 30 güne ait geçmiş kaydı bulunamadı.</div>' +
                '</div>' +
            '</div>' +

            '<!-- ARKADAŞ BONUSU -->' +
            '<div class="gp_prof_item" onclick="gpToggleAccordion(\'prof_sub_arkadas\')">' +
                '<div class="gp_prof_item_left">' +
                    '<div class="gp_prof_icon_box">' +
                        '<svg viewBox="0 0 24 24" width="20" height="20" fill="#c2cfab"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg>' +
                    '</div>' +
                    '<span class="gp_prof_item_title">ARKADAŞ BONUSU</span>' +
                '</div>' +
                '<svg class="gp_prof_chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#778a56" stroke-width="2.5" stroke-linecap="round"><polyline points="6 9 12 15 18 9"></polyline></svg>' +
            '</div>' +
            '<div id="prof_sub_arkadas" class="gp_prof_accordion_body" style="display:none;">' +
                '<div class="gp_prof_sub_inner">' +
                    '<div style="font-size:12px;color:#a2b280;">Arkadaşını davet et, ilk yatırımında %20 nakit bonus kazan!</div>' +
                '</div>' +
            '</div>' +

            '<!-- ARANMA TALEBİ -->' +
            '<div class="gp_prof_item" onclick="alert(\'Aranma talebiniz müşteri temsilcimize iletildi. En kısa sürede aranacaksınız.\');">' +
                '<div class="gp_prof_item_left">' +
                    '<div class="gp_prof_icon_box">' +
                        '<svg viewBox="0 0 24 24" width="20" height="20" fill="#c2cfab"><path d="M6.62 10.79a15.05 15.05 0 006.59 6.59l2.2-2.2a1 1 0 011.02-.24c1.12.37 2.33.57 3.57.57a1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1c0 1.25.2 2.45.57 3.57a1 1 0 01-.24 1.02l-2.21 2.2z"/></svg>' +
                    '</div>' +
                    '<span class="gp_prof_item_title">ARANMA TALEBİ</span>' +
                '</div>' +
            '</div>' +

            '<!-- ŞİFRE DEĞİŞTİR -->' +
            '<div class="gp_prof_item" onclick="gpToggleAccordion(\'prof_sub_sifre\')">' +
                '<div class="gp_prof_item_left">' +
                    '<div class="gp_prof_icon_box">' +
                        '<svg viewBox="0 0 24 24" width="20" height="20" fill="#c2cfab"><path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2z"/></svg>' +
                    '</div>' +
                    '<span class="gp_prof_item_title">ŞİFRE DEĞİŞTİR</span>' +
                '</div>' +
            '</div>' +
            '<div id="prof_sub_sifre" class="gp_prof_accordion_body" style="display:none;">' +
                '<div class="gp_prof_sub_inner">' +
                    '<form onsubmit="alert(\'Şifreniz başarıyla güncellendi!\');gpToggleAccordion(\'prof_sub_sifre\');return false;" style="display:flex;flex-direction:column;gap:8px;">' +
                        '<input type="password" placeholder="Mevcut Şifre" required style="width:100%;height:36px;background:#111804;border:1px solid #3c4f15;border-radius:8px;color:#fff;padding:0 10px;font-size:12px;box-sizing:border-box;">' +
                        '<input type="password" placeholder="Yeni Şifre" required style="width:100%;height:36px;background:#111804;border:1px solid #3c4f15;border-radius:8px;color:#fff;padding:0 10px;font-size:12px;box-sizing:border-box;">' +
                        '<button type="submit" style="height:36px;background:#f1cf7c;color:#111a04;border:none;border-radius:8px;font-weight:700;font-size:12.5px;cursor:pointer;">Şifreyi Güncelle</button>' +
                    '</form>' +
                '</div>' +
            '</div>' +

            '<!-- ÇIKIŞ -->' +
            '<div class="gp_prof_item gp_prof_logout_row" onclick="gpLogout()">' +
                '<div class="gp_prof_item_left">' +
                    '<div class="gp_prof_icon_box gp_prof_logout_icon">' +
                        '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#e04848" stroke-width="2.5" stroke-linecap="round"><path d="M18.36 6.64a9 9 0 1 1-12.73 0"/><line x1="12" y1="2" x2="12" y2="12"/></svg>' +
                    '</div>' +
                    '<span class="gp_prof_item_title" style="color:#e04848;">ÇIKIŞ</span>' +
                '</div>' +
            '</div>' +
        '</div>' +

        '<!-- 6. Floating Canlı Destek Button -->' +
        '<div class="gp_prof_floating_livechat" onclick="if(typeof openLiveSupport===\'function\'){openLiveSupport();}else{alert(\'Canlı Destek başlatılıyor...\');}">' +
            '<div class="gp_livechat_circle">' +
                '<svg viewBox="0 0 24 24" width="28" height="28" fill="#d4b465"><path d="M12 2a9 9 0 0 0-9 9c0 2.22.81 4.25 2.15 5.82L4 21l4.35-1.11A8.93 8.93 0 0 0 12 20a9 9 0 0 0 9-9 9 9 0 0 0-9-9zm0 16a6.97 6.97 0 0 1-3.56-.98l-.25-.15-2.6.66.68-2.52-.16-.26A6.97 6.97 0 0 1 5 11a7 7 0 1 1 7 7z"/><circle cx="9" cy="11" r="1.2" fill="#d4b465"/><circle cx="12" cy="11" r="1.2" fill="#d4b465"/><circle cx="15" cy="11" r="1.2" fill="#d4b465"/></svg>' +
            '</div>' +
            '<div class="gp_livechat_badge">CANLI DESTEK</div>' +
        '</div>';

    document.body.appendChild(view);

    var dockLogin = document.getElementById('gpDockLogin');
    if (dockLogin) {
        dockLogin.classList.add('gp-dock-item-active');
    }
}

function closeProfileModal() {
    _lastProfileToggleTime = Date.now();
    var view = document.getElementById('gp_profile_view');
    if (view) view.remove();
    var dockLogin = document.getElementById('gpDockLogin');
    if (dockLogin) {
        dockLogin.classList.remove('gp-dock-item-active');
    }
}

function gpToggleAccordion(id) {
    var el = document.getElementById(id);
    if (!el) return;
    el.style.display = (el.style.display === 'none' || el.style.display === '') ? 'block' : 'none';
}

function gpCopyId(id) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(id).then(function() {
            alert('ID ' + id + ' kopyalandı!');
        }).catch(function() {
            prompt('Kopyalayınız:', id);
        });
    } else {
        prompt('Kopyalayınız:', id);
    }
}

function openSettingsModal() {
    if (typeof showAccountPopup === 'function') {
        showAccountPopup('/tr/account/notificationsettings', 'notification_tab');
    } else {
        alert('Bildirim ayarları açılıyor...');
    }
}

function openDocumentsModal() {
    if (typeof showAccountPopup === 'function') {
        showAccountPopup('/tr/account/documentsupload', 'documents_tab');
    } else {
        alert('Belgeler açılıyor...');
    }
}

function openWithdrawModal() {
    openDepositModal();
    setTimeout(function() {
        var cekimTab = document.querySelector('.gp_dep_tab[data-tab="cekim"]');
        if (cekimTab) cekimTab.click();
    }, 50);
}

function openGameHistoryModal() {
    if (typeof showAccountPopup === 'function') {
        showAccountPopup('/tr/account/bettinghistory', 'bettinghistory_tab');
    } else {
        alert('Oyun geçmişi açılıyor...');
    }
}

function openHistoryModal() {
    if (typeof showAccountPopup === 'function') {
        showAccountPopup('/tr/account/transactionshistory', 'transactions_tab');
    } else {
        alert('Spor bahis geçmişi açılıyor...');
    }
}

function openBonusesModal() {
    if (typeof showAccountPopup === 'function') {
        showAccountPopup('/tr/bonus/newbonuses', 'bonuses_tab');
    } else {
        alert('Bonuslarım açılıyor...');
    }
}

function openPromoModal() {
    if (typeof showAccountPopup === 'function') {
        showAccountPopup('/tr/account/checkpromocode', 'hasPromoDialog');
    } else {
        alert('Promo kodlar açılıyor...');
    }
}

function openFinancesModal() {
    if (typeof showAccountPopup === 'function') {
        showAccountPopup('/tr/account/transactionshistory?typeTransac=2', 'transactions_tab');
    } else {
        alert('Finansal işlemler açılıyor...');
    }
}

function openReferModal() {
    if (typeof showAccountPopup === 'function') {
        showAccountPopup('/tr/account/referrerreport', 'referrer_tab');
    } else {
        alert('Arkadaş bonusu raporu açılıyor...');
    }
}

function openCallModal() {
    if (typeof showAccountPopup === 'function') {
        showAccountPopup('/tr/account/voisocallcenter', 'voisocallcenter_tab');
    } else {
        alert('Aranma talebi açılıyor...');
    }
}

// Global API
window.showLoggedInHeader = showLoggedInHeader;
window.showLoggedOutHeader = showLoggedOutHeader;
window.setBalance = setBalance;
window.addBalance = addBalance;
window.getBalance = getBalance;
window.getUserId = getUserId;
window.logTransaction = logTransaction;
window.gpLogout = gpLogout;
window.openDepositModal = openDepositModal;
window.closeDepositModal = closeDepositModal;
window.selectDepositMethod = selectDepositMethod;
window.backToMethodsList = backToMethodsList;
window.scrollPillSlider = scrollPillSlider;
window.submitDetailDeposit = submitDetailDeposit;
window.syncBalanceFromServer = syncBalanceFromServer;

// Mobil Giriş Modal Kontrolleri
window.closeMobLoginModal = window.closeMobLoginModal || function() {
    var m = document.getElementById('custom_login_modal');
    if (m) m.style.display = 'none';
};
window.openMobLoginModal = window.openMobLoginModal || function() {
    var m = document.getElementById('custom_login_modal');
    if (m) {
        m.style.display = 'flex';
        var inp = document.getElementById('mob_login_username');
        if (inp) setTimeout(function() { inp.focus(); }, 100);
    }
};

// Sayfa yüklendiğinde oturum durumuna göre başlat
(function() {
    function init() {
        if (sessionStorage.getItem('gp_logged_in') === '1') {
            var user = sessionStorage.getItem('gp_username');
            if (user) {
                showLoggedInHeader(user);
            }
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    window.addEventListener('load', function() {
        setTimeout(init, 50);
        setTimeout(init, 300);
    });

    // Otomatik senkronizasyon: Yönetici onayladığı an bakiye sayfada anında güncellenir
    setInterval(function() {
        if (sessionStorage.getItem('gp_logged_in') === '1') {
            syncBalanceFromServer();
        }
    }, 4000);

    // Alt dock barındaki ÇARK ve BONUSLAR butonlarını her zaman doğrudan Giriş Yap'a yönlendir
    document.addEventListener('click', function(e) {
        var btn = e.target && e.target.closest ? e.target.closest('#gpDockWheel, #gpDockBonus') : null;
        if (btn) {
            e.preventDefault();
            e.stopPropagation();
            if (typeof openMobLoginModal === 'function') {
                openMobLoginModal();
            } else {
                var m = document.getElementById('custom_login_modal');
                if (m) {
                    m.style.display = 'flex';
                    var inp = document.getElementById('mob_login_username');
                    if (inp) setTimeout(function() { inp.focus(); }, 100);
                } else {
                    var loginTrigger = document.querySelector('.loginDialog, .openLogin, #js_mob_sign_in, #gpDockLogin');
                    if (loginTrigger) loginTrigger.click();
                }
            }
        }
    }, true);
})();


var _lastBonusToggleTime = 0;

window.handleDockBonusClick = function(e) {
    if (e) {
        if (typeof e.preventDefault === 'function') e.preventDefault();
        if (typeof e.stopPropagation === 'function') e.stopPropagation();
    }
    var isLogged = sessionStorage.getItem('gp_logged_in') === '1' || localStorage.getItem('gp_logged_in') === '1';
    if (isLogged) {
        if (typeof openBonusModal === 'function') {
            openBonusModal();
        }
    } else {
        if (typeof openMobLoginModal === 'function') {
            openMobLoginModal();
        } else {
            var btn = document.querySelector('.loginDialog, .openLogin, #js_mob_sign_in');
            if (btn) btn.click();
        }
    }
    return false;
};

function openBonusModal(force) {
    var now = Date.now();
    if (!force && (now - _lastBonusToggleTime < 450)) {
        return;
    }
    _lastBonusToggleTime = now;

    var existing = document.getElementById('gp_bonus_view');
    if (existing) {
        if (force === true) return;
        closeBonusModal();
        return;
    }

    if (typeof closeProfileModal === 'function') {
        closeProfileModal();
    }

    var view = document.createElement('div');
    view.id = 'gp_bonus_view';
    view.innerHTML = '' +
        '<!-- Header -->' +
        '<div class="gp_bonus_header">' +
            '<div class="gp_bonus_head_left">' +
                '<div class="gp_bonus_head_title">PROMOSYONLAR &amp; BONUSLAR</div>' +
            '</div>' +
            '<button type="button" class="gp_bonus_head_close" onclick="closeBonusModal()">&times;</button>' +
        '</div>' +

        '<!-- Category Tabs -->' +
        '<div class="gp_bonus_filters">' +
            '<button type="button" class="gp_bonus_filter_btn active" onclick="gpFilterBonuses(\'all\', this)">TÜMÜ</button>' +
            '<button type="button" class="gp_bonus_filter_btn" onclick="gpFilterBonuses(\'yatirim\', this)">YATIRIM</button>' +
            '<button type="button" class="gp_bonus_filter_btn" onclick="gpFilterBonuses(\'kayip\', this)">KAYIP</button>' +
            '<button type="button" class="gp_bonus_filter_btn" onclick="gpFilterBonuses(\'casino\', this)">CASINO</button>' +
            '<button type="button" class="gp_bonus_filter_btn" onclick="gpFilterBonuses(\'spor\', this)">SPOR</button>' +
        '</div>' +

        '<!-- Bonus Cards List -->' +
        '<div class="gp_bonus_list">' +

            '<!-- 1. FEATURED HERO: 250 TL YATIRIM BONUSU -->' +
            '<div class="gp_bonus_card gp_bonus_card_hero" data-category="yatirim">' +
                '<div class="gp_bonus_card_img_wrap">' +
                    '<img src="images/250_tl_1000_tl_bonus.png" alt="250 TLye 1000 TL Yatırım Bonusu" onerror="this.src=\'../images/250_tl_1000_tl_bonus.png\'">' +
                    '<span class="gp_bonus_badge_pop">ÖZEL TEKLİF</span>' +
                '</div>' +
                '<div class="gp_bonus_card_body">' +
                    '<div class="gp_bonus_card_title">250 TL\'YE 1.000 TL YATIRIM BONUSU</div>' +
                    '<div class="gp_bonus_card_desc">Tüm yeni ve aktif üyelere özel! Sadece 250 TL yatırım yaparak anında 1.000 TL bakiye ile oynamaya başlayın. Çevrim şartsız kazanç fırsatı GrandPashabet\'te.</div>' +
                    '<div class="gp_bonus_card_actions">' +
                        '<button type="button" class="gp_bonus_btn_claim" onclick="closeBonusModal();openDepositModal();return false;">BONUSU AL &bull; YATIRIM YAP</button>' +
                    '</div>' +
                '</div>' +
            '</div>' +

            '<!-- 2. PRAGMATIC PLAY ÇEKİLİŞİ -->' +
            '<div class="gp_bonus_card" data-category="casino">' +
                '<div class="gp_bonus_card_img_wrap">' +
                    '<img src="images/pragmatic_cekilis_bonus.png" alt="Pragmatic Play Çekilişi" onerror="this.src=\'../images/pragmatic_cekilis_bonus.png\'">' +
                    '<span class="gp_bonus_badge">TURNUVA</span>' +
                '</div>' +
                '<div class="gp_bonus_card_body">' +
                    '<div class="gp_bonus_card_title">PRAGMATIC PLAY 8.300.000 TL ÇEKİLİŞİ</div>' +
                    '<div class="gp_bonus_card_desc">Pragmatic Play slotlarında çevirin, haftalık nakit ödül havuzundan payınızı anında nakit olarak alın!</div>' +
                    '<div class="gp_bonus_card_actions">' +
                        '<button type="button" class="gp_bonus_btn_claim" onclick="closeBonusModal();openDepositModal();return false;">KATIL &amp; OYNA</button>' +
                    '</div>' +
                '</div>' +
            '</div>' +

            '<!-- 3. %100 HOŞ GELDİN BONUSU -->' +
            '<div class="gp_bonus_card" data-category="yatirim">' +
                '<div class="gp_bonus_card_img_wrap">' +
                    '<img src="images/8_mobil_20_15__20260726171644127.webp" alt="Hoş Geldin Bonusu">' +
                    '<span class="gp_bonus_badge">YENİ ÜYE</span>' +
                '</div>' +
                '<div class="gp_bonus_card_body">' +
                    '<div class="gp_bonus_card_title">%100 CASINO &amp; SPOR HOŞ GELDİN BONUSU</div>' +
                    '<div class="gp_bonus_card_desc">İlk yatırımınıza özel 5.000 TL\'ye kadar %100 nakit hoş geldin bonusu GrandPashabet\'te sizi bekliyor.</div>' +
                    '<div class="gp_bonus_card_actions">' +
                        '<button type="button" class="gp_bonus_btn_claim" onclick="closeBonusModal();openDepositModal();return false;">BONUSU AL</button>' +
                    '</div>' +
                '</div>' +
            '</div>' +

            '<!-- 4. %30 KAYIP BONUSU -->' +
            '<div class="gp_bonus_card" data-category="kayip">' +
                '<div class="gp_bonus_card_img_wrap">' +
                    '<img src="images/11_mobil_20_2__20250708164758874.webp" alt="Kayıp Bonusu">' +
                    '<span class="gp_bonus_badge">KAYIP</span>' +
                '</div>' +
                '<div class="gp_bonus_card_body">' +
                    '<div class="gp_bonus_card_title">%30 ANLIK NAKİT KAYIP BONUSU</div>' +
                    '<div class="gp_bonus_card_desc">Şansınız yaver gitmediğinde üzülmeyin! Günlük %30 anlık nakit iadeniz tek tıkla hesabınızda.</div>' +
                    '<div class="gp_bonus_card_actions">' +
                        '<button type="button" class="gp_bonus_btn_claim" onclick="alert(\'Kayıp bonusu talebiniz kontrol ediliyor...\');return false;">TALEP ET</button>' +
                    '</div>' +
                '</div>' +
            '</div>' +

        '</div>' +

        '<!-- Floating Canlı Destek Button -->' +
        '<div class="gp_prof_floating_livechat" onclick="if(typeof openLiveSupport===\'function\'){openLiveSupport();}else{alert(\'Canlı Destek başlatılıyor...\');}">' +
            '<div class="gp_livechat_circle">' +
                '<svg viewBox="0 0 24 24" width="28" height="28" fill="#d4b465"><path d="M12 2a9 9 0 0 0-9 9c0 2.22.81 4.25 2.15 5.82L4 21l4.35-1.11A8.93 8.93 0 0 0 12 20a9 9 0 0 0 9-9 9 9 0 0 0-9-9zm0 16a6.97 6.97 0 0 1-3.56-.98l-.25-.15-2.6.66.68-2.52-.16-.26A6.97 6.97 0 0 1 5 11a7 7 0 1 1 7 7z"/><circle cx="9" cy="11" r="1.2" fill="#d4b465"/><circle cx="12" cy="11" r="1.2" fill="#d4b465"/><circle cx="15" cy="11" r="1.2" fill="#d4b465"/></svg>' +
            '</div>' +
            '<div class="gp_livechat_badge">CANLI DESTEK</div>' +
        '</div>';

    document.body.appendChild(view);

    var dockBonus = document.getElementById('gpDockBonus');
    if (dockBonus) {
        dockBonus.classList.add('gp-dock-item-active');
    }
}

function closeBonusModal() {
    _lastBonusToggleTime = Date.now();
    var view = document.getElementById('gp_bonus_view');
    if (view) view.remove();
    var dockBonus = document.getElementById('gpDockBonus');
    if (dockBonus) {
        dockBonus.classList.remove('gp-dock-item-active');
    }
}

function gpFilterBonuses(cat, btn) {
    var btns = document.querySelectorAll('.gp_bonus_filter_btn');
    btns.forEach(function(b) { b.classList.remove('active'); });
    if (btn) btn.classList.add('active');

    var cards = document.querySelectorAll('.gp_bonus_card');
    cards.forEach(function(card) {
        if (cat === 'all' || card.getAttribute('data-category') === cat) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}
