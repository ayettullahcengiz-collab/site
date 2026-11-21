html_path = r'.\index.html'

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Orijinal GrandPashabet "Populer Canli Maclar" (Spor tablari + Canli Mac Kartlari)
live_exact_markup = '''
<div class="sport_widgets" id="js-sport-Live-cont" style="padding: 0 4px;">
    <!-- Spor Brans Butonlari (Futbol, Basketbol, Tenis, Voleybol, Buz Hokeyi) -->
    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 14px; overflow-x: auto; padding: 2px 0; scrollbar-width: none;">
        <div style="background: #f6c343; color: #10160b; border-radius: 20px; padding: 6px 16px; font-size: 13px; font-weight: 800; display: flex; align-items: center; gap: 6px; cursor: pointer; white-space: nowrap;">
            <span>⚽</span> Futbol
        </div>
        <div style="background: rgba(255,255,255,0.06); color: #d4d4d8; border-radius: 20px; width: 34px; height: 34px; display: flex; align-items: center; justify-content: center; cursor: pointer; flex-shrink: 0;">
            <span>🏀</span>
        </div>
        <div style="background: rgba(255,255,255,0.06); color: #d4d4d8; border-radius: 20px; width: 34px; height: 34px; display: flex; align-items: center; justify-content: center; cursor: pointer; flex-shrink: 0;">
            <span>🎾</span>
        </div>
        <div style="background: rgba(255,255,255,0.06); color: #d4d4d8; border-radius: 20px; width: 34px; height: 34px; display: flex; align-items: center; justify-content: center; cursor: pointer; flex-shrink: 0;">
            <span>🏐</span>
        </div>
        <div style="background: rgba(255,255,255,0.06); color: #d4d4d8; border-radius: 20px; width: 34px; height: 34px; display: flex; align-items: center; justify-content: center; cursor: pointer; flex-shrink: 0;">
            <span>🏒</span>
        </div>
    </div>

    <!-- Canli Mac Kartlari -->
    <div style="display: flex; gap: 14px; overflow-x: auto; padding: 4px 0 16px 0; width: 100%; scrollbar-width: none;">
        <!-- Match 1: Real Madrid vs Man City -->
        <div style="background: #11170d; border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; min-width: 320px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a1a1aa; font-weight: 600;">
                    <span style="display: inline-block; width: 14px; height: 10px; background: #3b82f6; border-radius: 2px;"></span> UEFA Şampiyonlar Ligi
                </div>
                <span style="font-size: 14px; color: #71717a; cursor: pointer;">☆</span>
            </div>
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="color: #ef4444; font-size: 12px; font-weight: 800;">64'</span>
                <span style="color: #ef4444; font-size: 11px; font-weight: 700; background: rgba(239,68,68,0.15); padding: 1px 4px; border-radius: 3px;">CANLI</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; flex-direction: column; gap: 8px;">
                    <div style="display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 700; color: #ffffff;">
                        <span style="font-size: 15px;">⚪</span> Real Madrid
                    </div>
                    <div style="display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 700; color: #ffffff;">
                        <span style="font-size: 15px;">🔵</span> Manchester City
                    </div>
                </div>
                <div style="display: flex; flex-direction: column; gap: 8px; font-size: 15px; font-weight: 900; color: #f6c343; text-align: right; padding-right: 4px;">
                    <span>2</span>
                    <span>1</span>
                </div>
            </div>
            <!-- 1 - X - 2 Rows -->
            <div style="background: #182012; border-radius: 8px; padding: 6px 10px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                <div>1 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">2.15</span></div>
                <div>X <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">3.40</span></div>
                <div>2 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">3.10</span></div>
            </div>
            <!-- Alt / Ust Rows -->
            <div style="background: #182012; border-radius: 8px; padding: 6px 10px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                <div>Üst (3.5) <span style="color: #f6c343; font-weight: 800; margin-left: 10px;">1.85</span></div>
                <div>Alt (3.5) <span style="color: #f6c343; font-weight: 800; margin-left: 10px;">1.95</span></div>
            </div>
        </div>

        <!-- Match 2: Galatasaray vs Fenerbahçe -->
        <div style="background: #11170d; border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; min-width: 320px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a1a1aa; font-weight: 600;">
                    <span style="display: inline-block; width: 14px; height: 10px; background: #ef4444; border-radius: 2px;"></span> Süper Lig
                </div>
                <span style="font-size: 14px; color: #71717a; cursor: pointer;">☆</span>
            </div>
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="color: #ef4444; font-size: 12px; font-weight: 800;">78'</span>
                <span style="color: #ef4444; font-size: 11px; font-weight: 700; background: rgba(239,68,68,0.15); padding: 1px 4px; border-radius: 3px;">CANLI</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; flex-direction: column; gap: 8px;">
                    <div style="display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 700; color: #ffffff;">
                        <span style="font-size: 15px;">🦁</span> Galatasaray
                    </div>
                    <div style="display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 700; color: #ffffff;">
                        <span style="font-size: 15px;">🟡</span> Fenerbahçe
                    </div>
                </div>
                <div style="display: flex; flex-direction: column; gap: 8px; font-size: 15px; font-weight: 900; color: #f6c343; text-align: right; padding-right: 4px;">
                    <span>1</span>
                    <span>1</span>
                </div>
            </div>
            <div style="background: #182012; border-radius: 8px; padding: 6px 10px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                <div>1 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">2.65</span></div>
                <div>X <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">2.30</span></div>
                <div>2 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">2.90</span></div>
            </div>
            <div style="background: #182012; border-radius: 8px; padding: 6px 10px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                <div>Üst (2.5) <span style="color: #f6c343; font-weight: 800; margin-left: 10px;">1.72</span></div>
                <div>Alt (2.5) <span style="color: #f6c343; font-weight: 800; margin-left: 10px;">2.05</span></div>
            </div>
        </div>
    </div>
</div>
'''

# Orijinal GrandPashabet "Populer Mac Oncesi" (Birebir Ekran Goruntundeki Maclar ve Oranlar)
prematch_exact_markup = '''
<div class="sport_widgets" id="js-sport-Prematch-cont" style="padding: 0 4px;">
    <!-- Spor Brans Butonlari (Futbol, Basketbol, Tenis, Voleybol, Buz Hokeyi) -->
    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 14px; overflow-x: auto; padding: 2px 0; scrollbar-width: none;">
        <div style="background: #f6c343; color: #10160b; border-radius: 20px; padding: 6px 16px; font-size: 13px; font-weight: 800; display: flex; align-items: center; gap: 6px; cursor: pointer; white-space: nowrap;">
            <span>⚽</span> Futbol
        </div>
        <div style="background: rgba(255,255,255,0.06); color: #d4d4d8; border-radius: 20px; width: 34px; height: 34px; display: flex; align-items: center; justify-content: center; cursor: pointer; flex-shrink: 0;">
            <span>🏀</span>
        </div>
        <div style="background: rgba(255,255,255,0.06); color: #d4d4d8; border-radius: 20px; width: 34px; height: 34px; display: flex; align-items: center; justify-content: center; cursor: pointer; flex-shrink: 0;">
            <span>🎾</span>
        </div>
        <div style="background: rgba(255,255,255,0.06); color: #d4d4d8; border-radius: 20px; width: 34px; height: 34px; display: flex; align-items: center; justify-content: center; cursor: pointer; flex-shrink: 0;">
            <span>🏐</span>
        </div>
        <div style="background: rgba(255,255,255,0.06); color: #d4d4d8; border-radius: 20px; width: 34px; height: 34px; display: flex; align-items: center; justify-content: center; cursor: pointer; flex-shrink: 0;">
            <span>🏒</span>
        </div>
    </div>

    <!-- Ekran Goruntundeki Kartlarin Birebiri -->
    <div style="display: flex; gap: 14px; overflow-x: auto; padding: 4px 0 16px 0; width: 100%; scrollbar-width: none;">
        <!-- Card 1: ABD vs Haiti -->
        <div style="background: #11170d; border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; min-width: 320px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a1a1aa; font-weight: 600;">
                    <span style="display: inline-block; width: 14px; height: 10px; background: #3b82f6; border-radius: 2px;"></span> CONCACAF Uluslar Lig
                </div>
                <span style="font-size: 14px; color: #71717a; cursor: pointer;">☆</span>
            </div>
            <div style="font-size: 12px; font-weight: 700; color: #a1a1aa;">18.11 3:00</div>
            <div style="display: flex; flex-direction: column; gap: 8px;">
                <div style="display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 700; color: #ffffff;">
                    <span>🇺🇸</span> ABD
                </div>
                <div style="display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 700; color: #ffffff;">
                    <span>🇭🇹</span> Haiti
                </div>
            </div>
            <!-- 1 - X - 2 Rows -->
            <div style="background: #182012; border-radius: 8px; padding: 6px 10px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                <div>1 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">1.06</span></div>
                <div>X <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">11</span></div>
                <div>2 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">22</span></div>
            </div>
            <!-- Alt / Ust Rows -->
            <div style="background: #182012; border-radius: 8px; padding: 6px 10px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                <div>Üst (4) <span style="color: #f6c343; font-weight: 800; margin-left: 10px;">1.7</span></div>
                <div>Alt (4) <span style="color: #f6c343; font-weight: 800; margin-left: 10px;">2.05</span></div>
            </div>
        </div>

        <!-- Card 2: Meksika vs Jamaica -->
        <div style="background: #11170d; border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; min-width: 320px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a1a1aa; font-weight: 600;">
                    <span style="display: inline-block; width: 14px; height: 10px; background: #3b82f6; border-radius: 2px;"></span> CONCACAF Uluslar Lig
                </div>
                <span style="font-size: 14px; color: #71717a; cursor: pointer;">☆</span>
            </div>
            <div style="font-size: 12px; font-weight: 700; color: #a1a1aa;">18.11 5:30</div>
            <div style="display: flex; flex-direction: column; gap: 8px;">
                <div style="display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 700; color: #ffffff;">
                    <span>🇲🇽</span> Meksika
                </div>
                <div style="display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 700; color: #ffffff;">
                    <span>🇯🇲</span> Jamaica
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

        <!-- Card 3: BK Hacken(K) vs Manchester City(K) -->
        <div style="background: #11170d; border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; min-width: 320px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a1a1aa; font-weight: 600;">
                    <span style="display: inline-block; width: 14px; height: 10px; background: #3b82f6; border-radius: 2px;"></span> Kadınlar. UEFA Şampiyonlar Ligi
                </div>
                <span style="font-size: 14px; color: #71717a; cursor: pointer;">☆</span>
            </div>
            <div style="font-size: 12px; font-weight: 700; color: #a1a1aa;">18.11 20:45</div>
            <div style="display: flex; flex-direction: column; gap: 8px;">
                <div style="display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 700; color: #ffffff;">
                    <span>🟡</span> BK Hacken(K)
                </div>
                <div style="display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 700; color: #ffffff;">
                    <span>🔵</span> Manchester City(K)
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
    </div>
</div>
'''

# 1. Populer Canli Maclar alanini degistir
p_live = html.find('id="js-sport-Live-cont"')
if p_live != -1:
    p_pre = html.find('Popüler Maç Öncesi', p_live)
    p_prev_div = html.rfind('<div class="dynamic_container">', p_live, p_pre)
    html = html[:p_live-30] + live_exact_markup + '</div>\n' + html[p_prev_div:]

# 2. Populer Mac Oncesi alanini degistir
p_pre_idx = html.find('id="js-sport-Prematch-cont"')
if p_pre_idx != -1:
    p_next_dyn = html.find('<div class="dynamic_container">', p_pre_idx)
    html = html[:p_pre_idx-30] + prematch_exact_markup + '</div>\n' + html[p_next_dyn:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Birebir orijinal attigin fotoğraftaki Populer Mac Oncesi & Canli Maclar kuruldu!')
