html_path = r'.\index.html'

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Orijinal GrandPashabet Populer Canli Maclar Kartlari (Canli dakika, skor, 1-X-2 oranlari)
live_matches_markup = '''
<div class="sport_widgets" id="js-sport-Live-cont" style="padding: 0 4px;">
    <div style="display: flex; gap: 12px; overflow-x: auto; padding: 6px 0 16px 0; width: 100%; scrollbar-width: none;">
        <!-- Match 1: Real Madrid vs Man City -->
        <div style="background: linear-gradient(180deg, #182212 0%, #10160b 100%); border: 1px solid #2d381c; border-radius: 12px; min-width: 280px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 8px;">
                <span style="font-size: 11px; color: #a3e635; font-weight: 700; text-transform: uppercase;">⚽ UEFA Şampiyonlar Ligi</span>
                <span style="background: rgba(239,68,68,0.2); color: #ef4444; border: 1px solid #ef4444; border-radius: 4px; padding: 2px 6px; font-size: 11px; font-weight: 800; display: flex; align-items: center; gap: 4px;">
                    <span style="width: 6px; height: 6px; background: #ef4444; border-radius: 50%; display: inline-block;"></span> 64' CANLI
                </span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; font-size: 14px; font-weight: 700; color: #ffffff;">
                <div style="display: flex; flex-direction: column; gap: 6px;">
                    <span>Real Madrid</span>
                    <span>Manchester City</span>
                </div>
                <div style="display: flex; flex-direction: column; gap: 6px; font-size: 16px; font-weight: 900; color: #ffcc00; text-align: right;">
                    <span>2</span>
                    <span>1</span>
                </div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; margin-top: 4px;">
                <div style="background: #232d16; border: 1px solid #3d4f24; border-radius: 6px; padding: 6px; text-align: center; cursor: pointer;">
                    <div style="font-size: 10px; color: #8fa368; font-weight: 600;">1</div>
                    <div style="font-size: 13px; font-weight: 800; color: #ffffff;">2.15</div>
                </div>
                <div style="background: #232d16; border: 1px solid #3d4f24; border-radius: 6px; padding: 6px; text-align: center; cursor: pointer;">
                    <div style="font-size: 10px; color: #8fa368; font-weight: 600;">X</div>
                    <div style="font-size: 13px; font-weight: 800; color: #ffffff;">3.40</div>
                </div>
                <div style="background: #232d16; border: 1px solid #3d4f24; border-radius: 6px; padding: 6px; text-align: center; cursor: pointer;">
                    <div style="font-size: 10px; color: #8fa368; font-weight: 600;">2</div>
                    <div style="font-size: 13px; font-weight: 800; color: #ffffff;">3.10</div>
                </div>
            </div>
        </div>

        <!-- Match 2: Galatasaray vs Fenerbahçe -->
        <div style="background: linear-gradient(180deg, #182212 0%, #10160b 100%); border: 1px solid #2d381c; border-radius: 12px; min-width: 280px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 8px;">
                <span style="font-size: 11px; color: #a3e635; font-weight: 700; text-transform: uppercase;">⚽ Süper Lig</span>
                <span style="background: rgba(239,68,68,0.2); color: #ef4444; border: 1px solid #ef4444; border-radius: 4px; padding: 2px 6px; font-size: 11px; font-weight: 800; display: flex; align-items: center; gap: 4px;">
                    <span style="width: 6px; height: 6px; background: #ef4444; border-radius: 50%; display: inline-block;"></span> 78' CANLI
                </span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; font-size: 14px; font-weight: 700; color: #ffffff;">
                <div style="display: flex; flex-direction: column; gap: 6px;">
                    <span>Galatasaray</span>
                    <span>Fenerbahçe</span>
                </div>
                <div style="display: flex; flex-direction: column; gap: 6px; font-size: 16px; font-weight: 900; color: #ffcc00; text-align: right;">
                    <span>1</span>
                    <span>1</span>
                </div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; margin-top: 4px;">
                <div style="background: #232d16; border: 1px solid #3d4f24; border-radius: 6px; padding: 6px; text-align: center; cursor: pointer;">
                    <div style="font-size: 10px; color: #8fa368; font-weight: 600;">1</div>
                    <div style="font-size: 13px; font-weight: 800; color: #ffffff;">2.65</div>
                </div>
                <div style="background: #232d16; border: 1px solid #3d4f24; border-radius: 6px; padding: 6px; text-align: center; cursor: pointer;">
                    <div style="font-size: 10px; color: #8fa368; font-weight: 600;">X</div>
                    <div style="font-size: 13px; font-weight: 800; color: #ffffff;">2.30</div>
                </div>
                <div style="background: #232d16; border: 1px solid #3d4f24; border-radius: 6px; padding: 6px; text-align: center; cursor: pointer;">
                    <div style="font-size: 10px; color: #8fa368; font-weight: 600;">2</div>
                    <div style="font-size: 13px; font-weight: 800; color: #ffffff;">2.90</div>
                </div>
            </div>
        </div>

        <!-- Match 3: Arsenal vs Liverpool -->
        <div style="background: linear-gradient(180deg, #182212 0%, #10160b 100%); border: 1px solid #2d381c; border-radius: 12px; min-width: 280px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 8px;">
                <span style="font-size: 11px; color: #a3e635; font-weight: 700; text-transform: uppercase;">⚽ İngiltere Premier Lig</span>
                <span style="background: rgba(239,68,68,0.2); color: #ef4444; border: 1px solid #ef4444; border-radius: 4px; padding: 2px 6px; font-size: 11px; font-weight: 800; display: flex; align-items: center; gap: 4px;">
                    <span style="width: 6px; height: 6px; background: #ef4444; border-radius: 50%; display: inline-block;"></span> 41' CANLI
                </span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; font-size: 14px; font-weight: 700; color: #ffffff;">
                <div style="display: flex; flex-direction: column; gap: 6px;">
                    <span>Arsenal</span>
                    <span>Liverpool</span>
                </div>
                <div style="display: flex; flex-direction: column; gap: 6px; font-size: 16px; font-weight: 900; color: #ffcc00; text-align: right;">
                    <span>0</span>
                    <span>2</span>
                </div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; margin-top: 4px;">
                <div style="background: #232d16; border: 1px solid #3d4f24; border-radius: 6px; padding: 6px; text-align: center; cursor: pointer;">
                    <div style="font-size: 10px; color: #8fa368; font-weight: 600;">1</div>
                    <div style="font-size: 13px; font-weight: 800; color: #ffffff;">5.50</div>
                </div>
                <div style="background: #232d16; border: 1px solid #3d4f24; border-radius: 6px; padding: 6px; text-align: center; cursor: pointer;">
                    <div style="font-size: 10px; color: #8fa368; font-weight: 600;">X</div>
                    <div style="font-size: 13px; font-weight: 800; color: #ffffff;">4.10</div>
                </div>
                <div style="background: #232d16; border: 1px solid #3d4f24; border-radius: 6px; padding: 6px; text-align: center; cursor: pointer;">
                    <div style="font-size: 10px; color: #8fa368; font-weight: 600;">2</div>
                    <div style="font-size: 13px; font-weight: 800; color: #ffffff;">1.42</div>
                </div>
            </div>
        </div>
    </div>
</div>
'''

# Orijinal GrandPashabet Populer Mac Oncesi Kartlari (Tarih/Saat ve 1-X-2 oranlari)
prematch_matches_markup = '''
<div class="sport_widgets" id="js-sport-Prematch-cont" style="padding: 0 4px;">
    <div style="display: flex; gap: 12px; overflow-x: auto; padding: 6px 0 16px 0; width: 100%; scrollbar-width: none;">
        <!-- Match 1: Inter vs Barcelona -->
        <div style="background: linear-gradient(180deg, #182212 0%, #10160b 100%); border: 1px solid #2d381c; border-radius: 12px; min-width: 280px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 8px;">
                <span style="font-size: 11px; color: #a3e635; font-weight: 700; text-transform: uppercase;">⚽ Şampiyonlar Ligi</span>
                <span style="color: #94a3b8; font-size: 11px; font-weight: 700;">Bugün 22:00</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; font-size: 14px; font-weight: 700; color: #ffffff;">
                <div style="display: flex; flex-direction: column; gap: 6px;">
                    <span>Inter Milan</span>
                    <span>Barcelona</span>
                </div>
                <div style="font-size: 13px; font-weight: 700; color: #94a3b8;">vs</div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; margin-top: 4px;">
                <div style="background: #232d16; border: 1px solid #3d4f24; border-radius: 6px; padding: 6px; text-align: center; cursor: pointer;">
                    <div style="font-size: 10px; color: #8fa368; font-weight: 600;">1</div>
                    <div style="font-size: 13px; font-weight: 800; color: #ffffff;">2.40</div>
                </div>
                <div style="background: #232d16; border: 1px solid #3d4f24; border-radius: 6px; padding: 6px; text-align: center; cursor: pointer;">
                    <div style="font-size: 10px; color: #8fa368; font-weight: 600;">X</div>
                    <div style="font-size: 13px; font-weight: 800; color: #ffffff;">3.55</div>
                </div>
                <div style="background: #232d16; border: 1px solid #3d4f24; border-radius: 6px; padding: 6px; text-align: center; cursor: pointer;">
                    <div style="font-size: 10px; color: #8fa368; font-weight: 600;">2</div>
                    <div style="font-size: 13px; font-weight: 800; color: #ffffff;">2.85</div>
                </div>
            </div>
        </div>

        <!-- Match 2: Bayern Munich vs PSG -->
        <div style="background: linear-gradient(180deg, #182212 0%, #10160b 100%); border: 1px solid #2d381c; border-radius: 12px; min-width: 280px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 8px;">
                <span style="font-size: 11px; color: #a3e635; font-weight: 700; text-transform: uppercase;">⚽ Şampiyonlar Ligi</span>
                <span style="color: #94a3b8; font-size: 11px; font-weight: 700;">Bugün 22:00</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; font-size: 14px; font-weight: 700; color: #ffffff;">
                <div style="display: flex; flex-direction: column; gap: 6px;">
                    <span>Bayern Münih</span>
                    <span>Paris Saint-Germain</span>
                </div>
                <div style="font-size: 13px; font-weight: 700; color: #94a3b8;">vs</div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; margin-top: 4px;">
                <div style="background: #232d16; border: 1px solid #3d4f24; border-radius: 6px; padding: 6px; text-align: center; cursor: pointer;">
                    <div style="font-size: 10px; color: #8fa368; font-weight: 600;">1</div>
                    <div style="font-size: 13px; font-weight: 800; color: #ffffff;">1.95</div>
                </div>
                <div style="background: #232d16; border: 1px solid #3d4f24; border-radius: 6px; padding: 6px; text-align: center; cursor: pointer;">
                    <div style="font-size: 10px; color: #8fa368; font-weight: 600;">X</div>
                    <div style="font-size: 13px; font-weight: 800; color: #ffffff;">3.80</div>
                </div>
                <div style="background: #232d16; border: 1px solid #3d4f24; border-radius: 6px; padding: 6px; text-align: center; cursor: pointer;">
                    <div style="font-size: 10px; color: #8fa368; font-weight: 600;">2</div>
                    <div style="font-size: 13px; font-weight: 800; color: #ffffff;">3.50</div>
                </div>
            </div>
        </div>

        <!-- Match 3: Beşiktaş vs Trabzonspor -->
        <div style="background: linear-gradient(180deg, #182212 0%, #10160b 100%); border: 1px solid #2d381c; border-radius: 12px; min-width: 280px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 8px;">
                <span style="font-size: 11px; color: #a3e635; font-weight: 700; text-transform: uppercase;">⚽ Süper Lig</span>
                <span style="color: #94a3b8; font-size: 11px; font-weight: 700;">Yarın 19:00</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; font-size: 14px; font-weight: 700; color: #ffffff;">
                <div style="display: flex; flex-direction: column; gap: 6px;">
                    <span>Beşiktaş</span>
                    <span>Trabzonspor</span>
                </div>
                <div style="font-size: 13px; font-weight: 700; color: #94a3b8;">vs</div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; margin-top: 4px;">
                <div style="background: #232d16; border: 1px solid #3d4f24; border-radius: 6px; padding: 6px; text-align: center; cursor: pointer;">
                    <div style="font-size: 10px; color: #8fa368; font-weight: 600;">1</div>
                    <div style="font-size: 13px; font-weight: 800; color: #ffffff;">2.05</div>
                </div>
                <div style="background: #232d16; border: 1px solid #3d4f24; border-radius: 6px; padding: 6px; text-align: center; cursor: pointer;">
                    <div style="font-size: 10px; color: #8fa368; font-weight: 600;">X</div>
                    <div style="font-size: 13px; font-weight: 800; color: #ffffff;">3.30</div>
                </div>
                <div style="background: #232d16; border: 1px solid #3d4f24; border-radius: 6px; padding: 6px; text-align: center; cursor: pointer;">
                    <div style="font-size: 10px; color: #8fa368; font-weight: 600;">2</div>
                    <div style="font-size: 13px; font-weight: 800; color: #ffffff;">3.45</div>
                </div>
            </div>
        </div>
    </div>
</div>
'''

# 1. Populer Canli Maclar altindaki bos shadow DOM elementini degistir
live_target = '<div class="sport_widgets" id="js-sport-Live-cont"><sport-live><template shadowmode="open"><div id="sport-live"></div></template></sport-live></div>'
if live_target in html:
    html = html.replace(live_target, live_matches_markup)
    print('Populer Canli Maclar alani basariyla dolduruldu!')
else:
    # alternatif arama
    p_live = html.find('id="js-sport-Live-cont"')
    if p_live != -1:
        p_live_end = html.find('</div>', p_live) + 6
        html = html[:p_live-28] + live_matches_markup + html[p_live_end:]
        print('Populer Canli Maclar alternatif ile dolduruldu!')

# 2. Populer Mac Oncesi altindaki bos shadow DOM elementini degistir
prematch_target = '<div class="sport_widgets" id="js-sport-Prematch-cont"><sport-prematch><template shadowmode="open"><div id="sport-prematch"></div></template></sport-prematch></div>'
if prematch_target in html:
    html = html.replace(prematch_target, prematch_matches_markup)
    print('Populer Mac Oncesi alani basariyla dolduruldu!')
else:
    p_pre = html.find('id="js-sport-Prematch-cont"')
    if p_pre != -1:
        p_pre_end = html.find('</div>', p_pre) + 6
        html = html[:p_pre-28] + prematch_matches_markup + html[p_pre_end:]
        print('Populer Mac Oncesi alternatif ile dolduruldu!')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Mac alanlari tamamlandi!')
