html_path = r'.\index.html'

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Orijinal Mobil Header (Birebir Ekran Görüntündeki Gibi)
# Sol: Megafon + 'Dilediğiniz zaman tarayıcını...' duyurusu
# Alt Satır: Sol: Hareketli GrandPashabet Altın Yıldız Logosu, Sağ: Kayıt Ol ve Giriş Yap butonları
mobile_exact_header = '''
<div class="header__wrap_block" style="position: sticky; top: 0; z-index: 1000; background: #161c0e; border-bottom: 1px solid rgba(255,255,255,0.06); width: 100%;">
    <!-- 1. Satır: Megafon ve Duyuru -->
    <div style="padding: 6px 14px 2px 14px; display: flex; align-items: center; gap: 8px; font-size: 11px; color: #a1a1aa;">
        <span style="font-size: 13px; color: #f6c343; filter: drop-shadow(0 0 4px rgba(246,195,67,0.4));">📢</span>
        <div style="flex: 1; overflow: hidden; white-space: nowrap; text-overflow: ellipsis;">
            <span style="color: #a3a3a3; font-weight: 500;">Dilediğiniz zaman tarayıcınızı güncelleyebilir, kesintisiz erişim sağlayabilirsiniz.</span>
        </div>
    </div>

    <!-- 2. Satır: Orijinal Hareketli Logo + Kayıt Ol / Giriş Yap Butonları -->
    <div id="header" style="padding: 6px 14px 10px 14px; display: flex; align-items: center; justify-content: space-between; gap: 8px;">
        <!-- Sol: Hareketli Logo -->
        <a href="/" style="display: flex; align-items: center; text-decoration: none;">
            <img src="images/cdn/logoBigGif.gif" alt="GRANDPASHABET" style="height: 34px; width: auto; max-width: 170px; object-fit: contain; filter: drop-shadow(0 0 6px rgba(246,195,67,0.3));">
        </a>

        <!-- Sağ: Kayıt Ol & Giriş Yap Butonları -->
        <div id="menu-right" style="display: flex; align-items: center; gap: 8px; margin-left: auto;">
            <a href="#register" style="background: linear-gradient(180deg, #87a805 0%, #445401 100%); color: #ffffff; border-radius: 6px; padding: 6px 14px; font-size: 11px; font-weight: 700; text-decoration: none; border: 1px solid #a3cc06; box-shadow: 0 2px 6px rgba(135,168,5,0.3); white-space: nowrap;">
                Kayıt Ol
            </a>
            <a href="#login" style="background: #1f2714; color: #d4d4d8; border: 1px solid #3d4f24; border-radius: 6px; padding: 6px 14px; font-size: 11px; font-weight: 700; text-decoration: none; white-space: nowrap;">
                Giriş Yap
            </a>
        </div>
    </div>
</div>
'''

# Eski eklenen masaustu headerini bul ve kaldir
p_start = html.find('<div class="header__wrap_block"')
if p_start != -1:
    p_end = html.find('<div class="main-wrapper">', p_start)
    if p_end != -1:
        html = html[:p_start] + mobile_exact_header + '\n' + html[p_end:]
        print('Masaüstü butonları ve menüsü tamamen silindi, birebir orijinal mobil header takıldı!')
    else:
        print('main-wrapper bulunamadı!')
else:
    print('header__wrap_block bulunamadı!')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Bitti!')
