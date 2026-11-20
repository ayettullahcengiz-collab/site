html_path = r'C:\Users\laure\.gemini\antigravity\scratch\GrandPashabetSite\site\index.html'

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Orijinal GrandPashabet Mobil Giris Yap Modal Popupu
login_modal_html = '''
<!-- Orijinal GrandPashabet Mobil Giris Yap Popupu -->
<div id="custom_login_modal" style="display: none; position: fixed; inset: 0; z-index: 999999; background: rgba(0,0,0,0.85); backdrop-filter: blur(5px); align-items: center; justify-content: center; padding: 16px;">
    <div style="background: linear-gradient(180deg, #182210 0%, #0d1308 100%); border: 1px solid #3d4f24; border-radius: 16px; width: 100%; max-width: 380px; padding: 24px; box-shadow: 0 16px 40px rgba(0,0,0,0.7); position: relative; display: flex; flex-direction: column; gap: 16px;">
        <!-- Kapat Butonu -->
        <button id="close_login_modal" style="position: absolute; right: 14px; top: 14px; background: none; border: none; color: #a1a1aa; font-size: 20px; cursor: pointer; line-height: 1; padding: 4px;">✕</button>

        <!-- Baslik & Logo -->
        <div style="text-align: center; margin-bottom: 4px;">
            <img src="images/cdn/logoBigGif.gif" alt="GrandPashabet" style="height: 32px; width: auto; object-fit: contain; margin-bottom: 8px;">
            <div style="color: #ffffff; font-size: 17px; font-weight: 800;">Kullanıcı Girişi</div>
            <div style="color: #85994b; font-size: 11px; margin-top: 2px;">Hesabınıza giriş yaparak devam edin</div>
        </div>

        <!-- Form Alanlari -->
        <div style="display: flex; flex-direction: column; gap: 12px;">
            <div>
                <label style="display: block; color: #d4d4d8; font-size: 12px; font-weight: 700; margin-bottom: 6px;">Kullanıcı Adı veya E-posta</label>
                <input type="text" placeholder="Kullanıcı adınızı girin" style="width: 100%; box-sizing: border-box; background: #0c1106; border: 1px solid #283515; border-radius: 8px; padding: 10px 14px; color: #ffffff; font-size: 13px; outline: none;">
            </div>
            <div>
                <label style="display: block; color: #d4d4d8; font-size: 12px; font-weight: 700; margin-bottom: 6px;">Şifre</label>
                <input type="password" placeholder="Şifrenizi girin" style="width: 100%; box-sizing: border-box; background: #0c1106; border: 1px solid #283515; border-radius: 8px; padding: 10px 14px; color: #ffffff; font-size: 13px; outline: none;">
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; font-size: 11px;">
                <label style="color: #a1a1aa; display: flex; align-items: center; gap: 4px; cursor: pointer;">
                    <input type="checkbox" checked style="accent-color: #87a805;"> Beni Hatırla
                </label>
                <a href="#sifremi-unuttum" style="color: #f6c343; text-decoration: none; font-weight: 600;">Şifremi Unuttum</a>
            </div>
        </div>

        <!-- Giris Butonu -->
        <button type="button" style="background: linear-gradient(180deg, #87a805 0%, #445401 100%); color: #ffffff; border: 1px solid #a3cc06; border-radius: 8px; padding: 12px; font-size: 14px; font-weight: 800; cursor: pointer; box-shadow: 0 4px 12px rgba(135,168,5,0.4); text-transform: uppercase;">
            Giriş Yap
        </button>

        <!-- Kayit Ol Yonlendirme -->
        <div style="text-align: center; font-size: 12px; color: #a1a1aa; margin-top: 4px;">
            Hesabınız yok mu? <a href="#kayit-ol" style="color: #f6c343; font-weight: 700; text-decoration: none;">Hemen Kayıt Ol</a>
        </div>
    </div>
</div>

<script>
(function() {
    function openModal() {
        var m = document.getElementById('custom_login_modal');
        if (m) m.style.display = 'flex';
    }
    function closeModal() {
        var m = document.getElementById('custom_login_modal');
        if (m) m.style.display = 'none';
    }

    // Modal kapatma butonu ve disariya tiklayinca kapatma
    var closeBtn = document.getElementById('close_login_modal');
    if (closeBtn) closeBtn.onclick = closeModal;

    var modal = document.getElementById('custom_login_modal');
    if (modal) {
        modal.onclick = function(e) {
            if (e.target === modal) closeModal();
        };
    }

    // Ust Bar Giris Yap butonu
    var topSignIn = document.getElementById('js_mob_sign_in');
    if (topSignIn) topSignIn.onclick = function(e) { e.preventDefault(); openModal(); };

    // Alt Menudeki Butonlar: CARK, HAZINE AVI, BONUSLAR, GIRIS
    var bottomItems = document.querySelectorAll('.cw_mob_mav_fixed_bot_item');
    bottomItems.forEach(function(item) {
        var text = item.textContent || '';
        if (text.indexOf('ÇARK') !== -1 || text.indexOf('HAZİNE') !== -1 || text.indexOf('BONUS') !== -1 || text.indexOf('GİRİŞ') !== -1) {
            item.style.cursor = 'pointer';
            item.removeAttribute('href');
            item.onclick = function(e) {
                e.preventDefault();
                openModal();
            };
        }
    });
})();
</script>
'''

if '</body>' in html:
    html = html.replace('</body>', login_modal_html + '\n</body>')
    print('Giris yap modal ve buton baglantilari basariyla eklendi!')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Bitti!')
