html_path = r'.\index.html'

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Spor Branş Filtresi SVG İkonları
filter_bar_svg = '''
    <!-- Orijinal Spor Brans Butonlari (SVG Vektor Ikonlar) -->
    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 14px; overflow-x: auto; padding: 2px 0; scrollbar-width: none;">
        <!-- Futbol Aktif Buton -->
        <div style="background: #f6c343; color: #10160b; border-radius: 20px; padding: 6px 16px; font-size: 13px; font-weight: 800; display: flex; align-items: center; gap: 8px; cursor: pointer; white-space: nowrap;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#10160b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"></circle>
                <polygon points="12 8 8 11 9.5 15 14.5 15 16 11 12 8" fill="#10160b"></polygon>
            </svg>
            Futbol
        </div>
        <!-- Basketbol -->
        <div style="background: rgba(255,255,255,0.06); border-radius: 50%; width: 34px; height: 34px; display: flex; align-items: center; justify-content: center; cursor: pointer; flex-shrink: 0;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#d4d4d8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"></circle>
                <path d="M5 5a14 14 0 0 0 14 14"></path>
                <path d="M19 5a14 14 0 0 1-14 14"></path>
                <line x1="12" y1="2" x2="12" y2="22"></line>
                <line x1="2" y1="12" x2="22" y2="12"></line>
            </svg>
        </div>
        <!-- Tenis -->
        <div style="background: rgba(255,255,255,0.06); border-radius: 50%; width: 34px; height: 34px; display: flex; align-items: center; justify-content: center; cursor: pointer; flex-shrink: 0;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#d4d4d8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"></circle>
                <path d="M18 12a6 6 0 0 0-6-6"></path>
                <path d="M6 12a6 6 0 0 0 6 6"></path>
            </svg>
        </div>
        <!-- Voleybol -->
        <div style="background: rgba(255,255,255,0.06); border-radius: 50%; width: 34px; height: 34px; display: flex; align-items: center; justify-content: center; cursor: pointer; flex-shrink: 0;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#d4d4d8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"></circle>
                <path d="M12 12a10 10 0 0 0 10 0"></path>
                <path d="M12 12a10 10 0 0 0-5 8.66"></path>
                <path d="M12 12a10 10 0 0 0-5-8.66"></path>
            </svg>
        </div>
        <!-- Buz Hokeyi -->
        <div style="background: rgba(255,255,255,0.06); border-radius: 50%; width: 34px; height: 34px; display: flex; align-items: center; justify-content: center; cursor: pointer; flex-shrink: 0;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#d4d4d8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <ellipse cx="12" cy="12" rx="9" ry="4"></ellipse>
                <path d="M3 12v3c0 2.2 4 4 9 4s9-1.8 9-4v-3"></path>
            </svg>
        </div>
    </div>
'''

# 1. Popüler Canlı Maçlar - Attığın Ekran Görüntüsünün Birebir Kopyası
populer_canli_markup = f'''
<div class="sport_widgets" id="js-sport-Live-cont" style="padding: 0 4px;">
    {filter_bar_svg}

    <div style="display: flex; gap: 14px; overflow-x: auto; padding: 4px 0 16px 0; width: 100%; scrollbar-width: none;">
        <!-- Live Card 1: Arjantin vs Kosta Rika -->
        <div style="background: #11170d; border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; min-width: 320px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a1a1aa; font-weight: 600;">
                    <span style="display: inline-block; width: 14px; height: 10px; background: #3b82f6; border-radius: 2px;"></span> Milli Takımlar Dostluk Maçları. En İyi Takımlar
                </div>
                <span style="font-size: 14px; color: #71717a; cursor: pointer;">☆</span>
            </div>
            <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; font-weight: 700; color: #ef4444;">
                <span style="display: inline-block; width: 6px; height: 6px; background: #ef4444; border-radius: 50%;"></span>
                <span>(•) İlk Yarı</span>
                <span style="color: #71717a; font-size: 12px; margin-left: 2px;">📺</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; flex-direction: column; gap: 8px;">
                    <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;">
                        <img src="images/teams/argentina.png" style="width: 20px; height: 14px; object-fit: cover; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.5);">
                        <span>Arjantin</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;">
                        <img src="images/teams/costa_rica.png" style="width: 20px; height: 14px; object-fit: cover; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.5);">
                        <span>Kosta Rika</span>
                    </div>
                </div>
                <div style="display: flex; flex-direction: column; gap: 8px; font-size: 15px; font-weight: 900; color: #f6c343; text-align: right; padding-right: 4px;">
                    <span>4</span>
                    <span>0</span>
                </div>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; font-size: 11px; color: #a1a1aa; font-weight: 600;">
                <span>Toplam</span>
                <span style="color: #a1a1aa;">+200</span>
            </div>
            <div style="background: #182012; border-radius: 8px; padding: 7px 12px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                <div>Üst (6) <span style="color: #f6c343; font-weight: 800; margin-left: 12px;">1.8</span></div>
                <div>Alt (6) <span style="color: #f6c343; font-weight: 800; margin-left: 12px;">1.99</span></div>
            </div>
        </div>

        <!-- Live Card 2: Şili vs Kolombiya -->
        <div style="background: #11170d; border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; min-width: 320px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a1a1aa; font-weight: 600;">
                    <span style="display: inline-block; width: 14px; height: 10px; background: #3b82f6; border-radius: 2px;"></span> Milli Takımlar Dostluk Maçları. En İyi Takımlar
                </div>
                <span style="font-size: 14px; color: #71717a; cursor: pointer;">☆</span>
            </div>
            <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; font-weight: 700; color: #ef4444;">
                <span style="display: inline-block; width: 6px; height: 6px; background: #ef4444; border-radius: 50%;"></span>
                <span>(•) 1. Yarı 45'</span>
                <span style="color: #71717a; font-size: 12px; margin-left: 2px;">📺</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; flex-direction: column; gap: 8px;">
                    <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;">
                        <img src="images/teams/chile.png" style="width: 20px; height: 14px; object-fit: cover; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.5);">
                        <span>Şili</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;">
                        <img src="images/teams/colombia.png" style="width: 20px; height: 14px; object-fit: cover; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.5);">
                        <span>Kolombiya</span>
                    </div>
                </div>
                <div style="display: flex; flex-direction: column; gap: 8px; font-size: 15px; font-weight: 900; color: #f6c343; text-align: right; padding-right: 4px;">
                    <span>0</span>
                    <span>0</span>
                </div>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; font-size: 11px; color: #a1a1aa; font-weight: 600;">
                <span>Maç Sonucu</span>
                <span style="color: #a1a1aa;">+283</span>
            </div>
            <div style="background: #182012; border-radius: 8px; padding: 7px 12px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                <div>1 <span style="color: #f6c343; font-weight: 800; margin-left: 12px;">3.4</span></div>
                <div>X <span style="color: #f6c343; font-weight: 800; margin-left: 12px;">2.55</span></div>
                <div>2 <span style="color: #f6c343; font-weight: 800; margin-left: 12px;">2.62</span></div>
            </div>
        </div>

        <!-- Live Card 3: Uruguay vs Dominik Cumhuriyeti -->
        <div style="background: #11170d; border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; min-width: 320px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a1a1aa; font-weight: 600;">
                    <span style="display: inline-block; width: 14px; height: 10px; background: #3b82f6; border-radius: 2px;"></span> Milli Takımlar Dostluk Maçları. En İyi Takımlar
                </div>
                <span style="font-size: 14px; color: #71717a; cursor: pointer;">☆</span>
            </div>
            <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; font-weight: 700; color: #ef4444;">
                <span style="display: inline-block; width: 6px; height: 6px; background: #ef4444; border-radius: 50%;"></span>
                <span>(•) 1. Yarı 22'</span>
                <span style="color: #71717a; font-size: 12px; margin-left: 2px;">📺</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; flex-direction: column; gap: 8px;">
                    <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;">
                        <img src="images/teams/uruguay.png" style="width: 20px; height: 14px; object-fit: cover; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.5);">
                        <span>Uruguay</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;">
                        <img src="images/teams/dominican.png" style="width: 20px; height: 14px; object-fit: cover; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.5);">
                        <span>Dominik Cumhuriyeti</span>
                    </div>
                </div>
                <div style="display: flex; flex-direction: column; gap: 8px; font-size: 15px; font-weight: 900; color: #f6c343; text-align: right; padding-right: 4px;">
                    <span>0</span>
                    <span>0</span>
                </div>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; font-size: 11px; color: #a1a1aa; font-weight: 600;">
                <span>Maç Sonucu</span>
                <span style="color: #a1a1aa;">+409</span>
            </div>
            <div style="background: #182012; border-radius: 8px; padding: 7px 12px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                <div>1 <span style="color: #f6c343; font-weight: 800; margin-left: 12px;">1.17</span></div>
                <div>X <span style="color: #f6c343; font-weight: 800; margin-left: 12px;">6.05</span></div>
                <div>2 <span style="color: #f6c343; font-weight: 800; margin-left: 12px;">18</span></div>
            </div>
        </div>
    </div>
</div>
'''

# 2. Popüler Maç Öncesi - Attığın Ekran Görüntüsünün Birebir Kopyası (Gerçek Kulüp Amblemleriyle)
populer_prematch_markup = f'''
<div class="sport_widgets" id="js-sport-Prematch-cont" style="padding: 0 4px;">
    {filter_bar_svg}

    <div style="display: flex; gap: 14px; overflow-x: auto; padding: 4px 0 16px 0; width: 100%; scrollbar-width: none;">
        <!-- Prematch Card 1: Meksika vs Jamaica -->
        <div style="background: #11170d; border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; min-width: 320px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a1a1aa; font-weight: 600;">
                    <span style="display: inline-block; width: 14px; height: 10px; background: #3b82f6; border-radius: 2px;"></span> CONCACAF Uluslar Lig
                </div>
                <span style="font-size: 14px; color: #71717a; cursor: pointer;">☆</span>
            </div>
            <div style="font-size: 12px; font-weight: 700; color: #a1a1aa;">18.11 5:30</div>
            <div style="display: flex; flex-direction: column; gap: 8px;">
                <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;">
                    <img src="images/teams/mexico.png" style="width: 20px; height: 14px; object-fit: cover; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.5);">
                    <span>Meksika</span>
                </div>
                <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;">
                    <img src="images/teams/jamaica.png" style="width: 20px; height: 14px; object-fit: cover; border-radius: 2px; box-shadow: 0 1px 3px rgba(0,0,0,0.5);">
                    <span>Jamaica</span>
                </div>
            </div>
            <div style="background: #182012; border-radius: 8px; padding: 6px 10px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                <div>1 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">1.12</span></div>
                <div>X <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">8</span></div>
                <div>2 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">15</span></div>
            </div>
            <div style="background: #182012; border-radius: 8px; padding: 6px 10px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                <div>Üst (3.5) <span style="color: #f6c343; font-weight: 800; margin-left: 10px;">1.78</span></div>
                <div>Alt (3.5) <span style="color: #f6c343; font-weight: 800; margin-left: 10px;">1.92</span></div>
            </div>
        </div>

        <!-- Prematch Card 2: BK Hacken(K) vs Manchester City(K) -->
        <div style="background: #11170d; border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; min-width: 320px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a1a1aa; font-weight: 600;">
                    <span style="display: inline-block; width: 14px; height: 10px; background: #3b82f6; border-radius: 2px;"></span> Kadınlar. UEFA Şampiyonlar Ligi
                </div>
                <span style="font-size: 14px; color: #71717a; cursor: pointer;">☆</span>
            </div>
            <div style="font-size: 12px; font-weight: 700; color: #a1a1aa;">18.11 20:45</div>
            <div style="display: flex; flex-direction: column; gap: 8px;">
                <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;">
                    <img src="images/teams/hacken.png" style="width: 18px; height: 18px; object-fit: contain;">
                    <span>BK Hacken(K)</span>
                </div>
                <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;">
                    <img src="images/teams/mancity.png" style="width: 18px; height: 18px; object-fit: contain;">
                    <span>Manchester City(K)</span>
                </div>
            </div>
            <div style="background: #182012; border-radius: 8px; padding: 6px 10px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                <div>1 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">8</span></div>
                <div>X <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">5.4</span></div>
                <div>2 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">1.27</span></div>
            </div>
            <div style="background: #182012; border-radius: 8px; padding: 6px 10px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                <div>Üst (3) <span style="color: #f6c343; font-weight: 800; margin-left: 10px;">1.7</span></div>
                <div>Alt (3) <span style="color: #f6c343; font-weight: 800; margin-left: 10px;">2</span></div>
            </div>
        </div>

        <!-- Prematch Card 3: Real Madrid(K) vs Inter Milano(K) -->
        <div style="background: #11170d; border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; min-width: 320px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a1a1aa; font-weight: 600;">
                    <span style="display: inline-block; width: 14px; height: 10px; background: #3b82f6; border-radius: 2px;"></span> Kadınlar. UEFA Şampiyonlar Ligi
                </div>
                <span style="font-size: 14px; color: #71717a; cursor: pointer;">☆</span>
            </div>
            <div style="font-size: 12px; font-weight: 700; color: #a1a1aa;">18.11 20:45</div>
            <div style="display: flex; flex-direction: column; gap: 8px;">
                <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;">
                    <img src="images/teams/realmadrid.png" style="width: 18px; height: 18px; object-fit: contain;">
                    <span>Real Madrid(K)</span>
                </div>
                <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;">
                    <img src="images/teams/inter.png" style="width: 18px; height: 18px; object-fit: contain;">
                    <span>Inter Milano(K)</span>
                </div>
            </div>
            <div style="background: #182012; border-radius: 8px; padding: 6px 10px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                <div>1 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">1.21</span></div>
                <div>X <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">6</span></div>
                <div>2 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">9.5</span></div>
            </div>
            <div style="background: #182012; border-radius: 8px; padding: 6px 10px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                <div>Üst (3.5) <span style="color: #f6c343; font-weight: 800; margin-left: 10px;">1.96</span></div>
                <div>Alt (3.5) <span style="color: #f6c343; font-weight: 800; margin-left: 10px;">1.76</span></div>
            </div>
        </div>
    </div>
</div>
'''

# 1. Populer Canli Maclar alanini degistir
p_live = html.find('id="js-sport-Live-cont"')
if p_live != -1:
    p_pre = html.find('Popüler Maç Öncesi', p_live)
    p_prev_div = html.rfind('<div class="dynamic_container">', p_live, p_pre)
    html = html[:p_live-30] + populer_canli_markup + '</div>\n' + html[p_prev_div:]

# 2. Populer Mac Oncesi alanini degistir
p_pre_idx = html.find('id="js-sport-Prematch-cont"')
if p_pre_idx != -1:
    p_next_dyn = html.find('<div class="dynamic_container">', p_pre_idx)
    html = html[:p_pre_idx-30] + populer_prematch_markup + '</div>\n' + html[p_next_dyn:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Emojiler SVG yapildi ve takim logolari her iki kisim icin de birebir orijinal yerlestirildi!')
