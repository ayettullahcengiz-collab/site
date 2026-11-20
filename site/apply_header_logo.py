html_path = r'C:\Users\laure\.gemini\antigravity\scratch\GrandPashabetSite\site\index.html'

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Orijinal GrandPashabet Hareketli Header + Kayan Duyuru Bandi + Tepe Menuleri
header_rich_markup = '''
<div class="header__wrap_block" style="position: sticky; top: 0; z-index: 1000; background: #0f160a; border-bottom: 1px solid rgba(255,255,255,0.08); box-shadow: 0 4px 16px rgba(0,0,0,0.5);">
    
    <!-- 1. En Üst Kayan Duyuru Bandı (Marquee / Canlı Anons) -->
    <div style="background: #141c0d; border-bottom: 1px solid rgba(255,255,255,0.05); padding: 5px 12px; display: flex; align-items: center; gap: 10px; font-size: 11px; overflow: hidden; height: 28px;">
        <span style="font-size: 14px; flex-shrink: 0;">📢</span>
        <div style="flex: 1; overflow: hidden; white-space: nowrap;">
            <div style="display: inline-block; animation: marquee_anim 22s linear infinite; color: #a1a1aa; font-weight: 600;">
                ⭐ GrandPashabet Resmi Giriş Adresindesiniz! • Kesintisiz Canlı Bahis ve Casino Deneyimi • Güncel Giriş: grandpashabet9090.com • %300 15.000 TL Hoş Geldin Bonusu + 450 Freespin Fırsatını Kaçırmayın! • 7/24 Sesli ve Canlı Destek
            </div>
        </div>
    </div>

    <!-- 2. Ana Tepe Barı (Hareketli Logo + Promosyon/Destek Butonları + Kayıt/Giriş) -->
    <div id="header" style="padding: 8px 16px; display: flex; align-items: center; justify-content: space-between; gap: 12px; flex-wrap: wrap;">
        <!-- Sol Taraf: Hareketli GrandPashabet Logosu -->
        <div style="display: flex; align-items: center; gap: 14px;">
            <a href="/" style="display: flex; align-items: center; text-decoration: none;">
                <!-- Orijinal Hareketli Altın Işıltılı Logo GIF -->
                <img src="images/cdn/logoBigGif.gif" alt="GrandPashabet" style="height: 40px; width: auto; max-width: 210px; object-fit: contain; filter: drop-shadow(0 0 8px rgba(246,195,67,0.35));">
            </a>

            <!-- Promosyonlar & Sesli Destek Butonları -->
            <div style="display: flex; align-items: center; gap: 8px;" class="header-action-buttons">
                <a href="#promosyonlar" style="background: linear-gradient(180deg, #627b0b 0%, #3d4e04 100%); color: #ffffff; border: 1px solid #7ea10e; border-radius: 6px; padding: 6px 12px; font-size: 11px; font-weight: 800; text-decoration: none; display: flex; align-items: center; gap: 6px; box-shadow: 0 2px 6px rgba(0,0,0,0.3); white-space: nowrap;">
                    <span>📢</span> PROMOSYONLAR
                </a>
                <a href="#destek" style="background: linear-gradient(180deg, #627b0b 0%, #3d4e04 100%); color: #ffffff; border: 1px solid #7ea10e; border-radius: 6px; padding: 6px 12px; font-size: 11px; font-weight: 800; text-decoration: none; display: flex; align-items: center; gap: 6px; box-shadow: 0 2px 6px rgba(0,0,0,0.3); white-space: nowrap;">
                    <span>📞</span> SESLİ DESTEK
                </a>
            </div>
        </div>

        <!-- Sağ Taraf: Turnuva Rozeti & Kayıt Ol / Giriş Yap Butonları -->
        <div style="display: flex; align-items: center; gap: 10px;">
            <div style="display: flex; align-items: center; gap: 8px; border-right: 1px solid rgba(255,255,255,0.1); padding-right: 12px;" class="header-tournament-banner">
                <div style="width: 24px; height: 24px; border-radius: 50%; border: 1px solid #f6c343; display: flex; align-items: center; justify-content: center; font-size: 11px; color: #f6c343;">
                    ✓
                </div>
                <div style="display: flex; flex-direction: column; text-align: left;">
                    <span style="font-size: 10px; color: #f6c343; font-weight: 800; text-transform: uppercase;">GRAND SPOR</span>
                    <span style="font-size: 10px; color: #ffffff; font-weight: 700;">TURNUVASI</span>
                </div>
                <span style="background: #eab308; color: #000; font-size: 10px; font-weight: 900; padding: 2px 6px; border-radius: 4px; margin-left: 2px;">KATIL!</span>
            </div>

            <!-- Kayıt Ol / Giriş Yap Butonları -->
            <div id="menu-right" style="display: flex; align-items: center; gap: 8px;">
                <a href="#register" style="background: linear-gradient(180deg, #87a805 0%, #445401 100%); color: #ffffff; border-radius: 6px; padding: 7px 16px; font-size: 12px; font-weight: 800; text-decoration: none; border: 1px solid #a3cc06; box-shadow: 0 2px 8px rgba(135,168,5,0.4); white-space: nowrap;">
                    Kayıt Ol
                </a>
                <a href="#login" style="background: #182210; color: #d4d4d8; border: 1px solid #33441e; border-radius: 6px; padding: 7px 16px; font-size: 12px; font-weight: 700; text-decoration: none; white-space: nowrap;">
                    Giriş Yap
                </a>
            </div>
        </div>
    </div>

    <!-- 3. Kategori Alt Menü Şeridi (SPOR BAHİSLERİ, CANLI BAHİS, 3D SLOT vb.) -->
    <div style="background: #090e06; border-top: 1px solid rgba(255,255,255,0.05); padding: 0 16px; overflow-x: auto; scrollbar-width: none;">
        <div style="display: flex; align-items: center; gap: 18px; height: 38px; white-space: nowrap; font-size: 12px; font-weight: 800;">
            <a href="#spor" style="color: #60a5fa; text-decoration: none; border-bottom: 2px solid #3b82f6; height: 100%; display: flex; align-items: center;">SPOR BAHİSLERİ</a>
            <a href="#canli" style="color: #f6c343; text-decoration: none; height: 100%; display: flex; align-items: center;">CANLI BAHİS</a>
            <a href="#espor" style="color: #a1a1aa; text-decoration: none; height: 100%; display: flex; align-items: center;">E-SPOR</a>
            <a href="#slot" style="color: #a1a1aa; text-decoration: none; height: 100%; display: flex; align-items: center;">3D SLOT SALONU</a>
            <a href="#canlicasino" style="color: #a1a1aa; text-decoration: none; height: 100%; display: flex; align-items: center;">CANLI CASİNO</a>
            <a href="#hazine" style="color: #a1a1aa; text-decoration: none; height: 100%; display: flex; align-items: center; gap: 4px;">
                HAZİNE AVI <span style="background: #9333ea; color: #ffffff; font-size: 8px; font-weight: 900; padding: 1px 4px; border-radius: 3px;">PREMIUM</span>
            </a>
            <a href="#hizli" style="color: #a1a1aa; text-decoration: none; height: 100%; display: flex; align-items: center;">HIZLI OYUNLAR ▾</a>
            <a href="#sanal" style="color: #a1a1aa; text-decoration: none; height: 100%; display: flex; align-items: center;">SANAL BAHİSLER</a>
            <a href="#tv" style="color: #a1a1aa; text-decoration: none; height: 100%; display: flex; align-items: center;">TV OYUNLARI</a>
        </div>
    </div>
</div>

<style>
@keyframes marquee_anim {
    0% { transform: translateX(100%); }
    100% { transform: translateX(-100%); }
}
@media (max-width: 768px) {
    .header-action-buttons, .header-tournament-banner {
        display: none !important;
    }
}
</style>
'''

# Eski header__wrap_block kismini degistir
p_start = html.find('<div class="header__wrap_block">')
if p_start != -1:
    p_end = html.find('<div class="main-wrapper">', p_start)
    if p_end != -1:
        html = html[:p_start] + header_rich_markup + '\n' + html[p_end:]
        print('Header ve hareketli logo basariyla yerlestirildi!')
else:
    print('header__wrap_block bulunamadi!')

# Body padding-top duzenlemesi
html = html.replace('style="padding-top: 50px;"', 'style="padding-top: 0px;"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Bitti!')
