html_path = r'C:\Users\laure\.gemini\antigravity\scratch\GrandPashabetSite\site\index.html'

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# 1. Tum Spor Branslari Icin Interaktif Canli Maclar Verisi ve HTML Yapisi
sports_live_complete = '''
<div class="sport_widgets" id="js-sport-Live-cont" style="padding: 0 4px;">
    <!-- Spor Brans Butonlari (Interaktif Tiklanabilir Filtre) -->
    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 14px; overflow-x: auto; padding: 2px 0; scrollbar-width: none;">
        <div class="sport-filter-btn active" data-target="live" data-sport="football" style="background: #f6c343; color: #10160b; border-radius: 20px; padding: 6px 16px; font-size: 13px; font-weight: 800; display: flex; align-items: center; gap: 8px; cursor: pointer; white-space: nowrap;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polygon points="12 8 8 11 9.5 15 14.5 15 16 11 12 8" fill="currentColor"></polygon></svg>
            Futbol
        </div>
        <div class="sport-filter-btn" data-target="live" data-sport="basketball" style="background: rgba(255,255,255,0.06); color: #d4d4d8; border-radius: 20px; padding: 6px 14px; font-size: 13px; font-weight: 800; display: flex; align-items: center; gap: 8px; cursor: pointer; white-space: nowrap;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M5 5a14 14 0 0 0 14 14"></path><path d="M19 5a14 14 0 0 1-14 14"></path><line x1="12" y1="2" x2="12" y2="22"></line><line x1="2" y1="12" x2="22" y2="12"></line></svg>
            Basketbol
        </div>
        <div class="sport-filter-btn" data-target="live" data-sport="tennis" style="background: rgba(255,255,255,0.06); color: #d4d4d8; border-radius: 20px; padding: 6px 14px; font-size: 13px; font-weight: 800; display: flex; align-items: center; gap: 8px; cursor: pointer; white-space: nowrap;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M18 12a6 6 0 0 0-6-6"></path><path d="M6 12a6 6 0 0 0 6 6"></path></svg>
            Tenis
        </div>
        <div class="sport-filter-btn" data-target="live" data-sport="volleyball" style="background: rgba(255,255,255,0.06); color: #d4d4d8; border-radius: 20px; padding: 6px 14px; font-size: 13px; font-weight: 800; display: flex; align-items: center; gap: 8px; cursor: pointer; white-space: nowrap;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 12a10 10 0 0 0 10 0"></path><path d="M12 12a10 10 0 0 0-5 8.66"></path><path d="M12 12a10 10 0 0 0-5-8.66"></path></svg>
            Voleybol
        </div>
        <div class="sport-filter-btn" data-target="live" data-sport="hockey" style="background: rgba(255,255,255,0.06); color: #d4d4d8; border-radius: 20px; padding: 6px 14px; font-size: 13px; font-weight: 800; display: flex; align-items: center; gap: 8px; cursor: pointer; white-space: nowrap;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><ellipse cx="12" cy="12" rx="9" ry="4"></ellipse><path d="M3 12v3c0 2.2 4 4 9 4s9-1.8 9-4v-3"></path></svg>
            Buz Hokeyi
        </div>
    </div>

    <!-- Canli Mac Listeleri -->
    <div id="live_cards_container" style="display: flex; gap: 14px; overflow-x: auto; padding: 4px 0 16px 0; width: 100%; scrollbar-width: none;">
        <!-- FUTBOL (Varsayilan) -->
        <div class="live-sport-panel" data-sport="football" style="display: flex; gap: 14px; width: 100%;">
            <!-- Arjantin vs Kosta Rika -->
            <div style="background: #11170d; border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; min-width: 320px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a1a1aa; font-weight: 600;"><span style="display: inline-block; width: 14px; height: 10px; background: #3b82f6; border-radius: 2px;"></span> Milli Takımlar Dostluk Maçları</div>
                    <span style="font-size: 14px; color: #71717a;">☆</span>
                </div>
                <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; font-weight: 700; color: #ef4444;"><span style="display: inline-block; width: 6px; height: 6px; background: #ef4444; border-radius: 50%;"></span> (•) İlk Yarı <span style="color: #71717a;">📺</span></div>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="display: flex; flex-direction: column; gap: 8px;">
                        <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/argentina.png" style="width: 20px; height: 14px; object-fit: cover; border-radius: 2px;"> Arjantin</div>
                        <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/costa_rica.png" style="width: 20px; height: 14px; object-fit: cover; border-radius: 2px;"> Kosta Rika</div>
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 8px; font-size: 15px; font-weight: 900; color: #f6c343; text-align: right;"><span>4</span><span>0</span></div>
                </div>
                <div style="background: #182012; border-radius: 8px; padding: 7px 12px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                    <div>Üst (6) <span style="color: #f6c343; font-weight: 800; margin-left: 12px;">1.8</span></div>
                    <div>Alt (6) <span style="color: #f6c343; font-weight: 800; margin-left: 12px;">1.99</span></div>
                </div>
            </div>
            <!-- Şili vs Kolombiya -->
            <div style="background: #11170d; border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; min-width: 320px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a1a1aa; font-weight: 600;"><span style="display: inline-block; width: 14px; height: 10px; background: #3b82f6; border-radius: 2px;"></span> Milli Takımlar Dostluk Maçları</div>
                    <span style="font-size: 14px; color: #71717a;">☆</span>
                </div>
                <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; font-weight: 700; color: #ef4444;"><span style="display: inline-block; width: 6px; height: 6px; background: #ef4444; border-radius: 50%;"></span> (•) 1. Yarı 45' <span style="color: #71717a;">📺</span></div>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="display: flex; flex-direction: column; gap: 8px;">
                        <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/chile.png" style="width: 20px; height: 14px; object-fit: cover; border-radius: 2px;"> Şili</div>
                        <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/colombia.png" style="width: 20px; height: 14px; object-fit: cover; border-radius: 2px;"> Kolombiya</div>
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 8px; font-size: 15px; font-weight: 900; color: #f6c343; text-align: right;"><span>0</span><span>0</span></div>
                </div>
                <div style="background: #182012; border-radius: 8px; padding: 7px 12px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                    <div>1 <span style="color: #f6c343; font-weight: 800; margin-left: 12px;">3.4</span></div>
                    <div>X <span style="color: #f6c343; font-weight: 800; margin-left: 12px;">2.55</span></div>
                    <div>2 <span style="color: #f6c343; font-weight: 800; margin-left: 12px;">2.62</span></div>
                </div>
            </div>
        </div>

        <!-- BASKETBOL -->
        <div class="live-sport-panel" data-sport="basketball" style="display: none; gap: 14px; width: 100%;">
            <!-- Lakers vs Warriors -->
            <div style="background: #11170d; border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; min-width: 320px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a1a1aa; font-weight: 600;"><span style="display: inline-block; width: 14px; height: 10px; background: #eab308; border-radius: 2px;"></span> NBA Normal Sezon</div>
                    <span style="font-size: 14px; color: #71717a;">☆</span>
                </div>
                <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; font-weight: 700; color: #ef4444;"><span style="display: inline-block; width: 6px; height: 6px; background: #ef4444; border-radius: 50%;"></span> (•) 3. Çeyrek 04:12 <span style="color: #71717a;">📺</span></div>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="display: flex; flex-direction: column; gap: 8px;">
                        <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/lakers.png" style="width: 20px; height: 20px; object-fit: contain;"> LA Lakers</div>
                        <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/warriors.png" style="width: 20px; height: 20px; object-fit: contain;"> Golden State</div>
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 8px; font-size: 15px; font-weight: 900; color: #f6c343; text-align: right;"><span>78</span><span>82</span></div>
                </div>
                <div style="background: #182012; border-radius: 8px; padding: 7px 12px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                    <div>1 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">2.10</span></div>
                    <div>2 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">1.72</span></div>
                </div>
            </div>
            <!-- Panathinaikos vs Olympiacos -->
            <div style="background: #11170d; border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; min-width: 320px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a1a1aa; font-weight: 600;"><span style="display: inline-block; width: 14px; height: 10px; background: #eab308; border-radius: 2px;"></span> EuroLeague</div>
                    <span style="font-size: 14px; color: #71717a;">☆</span>
                </div>
                <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; font-weight: 700; color: #ef4444;"><span style="display: inline-block; width: 6px; height: 6px; background: #ef4444; border-radius: 50%;"></span> (•) 2. Çeyrek <span style="color: #71717a;">📺</span></div>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="display: flex; flex-direction: column; gap: 8px;">
                        <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/greece.png" style="width: 20px; height: 14px; object-fit: cover;"> Panathinaikos</div>
                        <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/greece.png" style="width: 20px; height: 14px; object-fit: cover;"> Olympiacos</div>
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 8px; font-size: 15px; font-weight: 900; color: #f6c343; text-align: right;"><span>41</span><span>38</span></div>
                </div>
                <div style="background: #182012; border-radius: 8px; padding: 7px 12px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                    <div>1 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">1.85</span></div>
                    <div>2 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">1.95</span></div>
                </div>
            </div>
        </div>

        <!-- TENIS -->
        <div class="live-sport-panel" data-sport="tennis" style="display: none; gap: 14px; width: 100%;">
            <!-- Alcaraz vs Sinner -->
            <div style="background: #11170d; border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; min-width: 320px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a1a1aa; font-weight: 600;"><span style="display: inline-block; width: 14px; height: 10px; background: #10b981; border-radius: 2px;"></span> ATP Finals - Tek Erkekler</div>
                    <span style="font-size: 14px; color: #71717a;">☆</span>
                </div>
                <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; font-weight: 700; color: #ef4444;"><span style="display: inline-block; width: 6px; height: 6px; background: #ef4444; border-radius: 50%;"></span> (•) 2. Set (4-3) <span style="color: #71717a;">📺</span></div>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="display: flex; flex-direction: column; gap: 8px;">
                        <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/alcaraz.png" style="width: 20px; height: 14px; object-fit: cover;"> Carlos Alcaraz</div>
                        <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/sinner.png" style="width: 20px; height: 14px; object-fit: cover;"> Jannik Sinner</div>
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 8px; font-size: 15px; font-weight: 900; color: #f6c343; text-align: right;"><span>1</span><span>0</span></div>
                </div>
                <div style="background: #182012; border-radius: 8px; padding: 7px 12px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                    <div>1 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">1.65</span></div>
                    <div>2 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">2.25</span></div>
                </div>
            </div>
        </div>

        <!-- VOLEYBOL -->
        <div class="live-sport-panel" data-sport="volleyball" style="display: none; gap: 14px; width: 100%;">
            <!-- Polonya vs Brezilya -->
            <div style="background: #11170d; border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; min-width: 320px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a1a1aa; font-weight: 600;"><span style="display: inline-block; width: 14px; height: 10px; background: #8b5cf6; border-radius: 2px;"></span> FIVB Milletler Ligi</div>
                    <span style="font-size: 14px; color: #71717a;">☆</span>
                </div>
                <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; font-weight: 700; color: #ef4444;"><span style="display: inline-block; width: 6px; height: 6px; background: #ef4444; border-radius: 50%;"></span> (•) 3. Set (18-21) <span style="color: #71717a;">📺</span></div>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="display: flex; flex-direction: column; gap: 8px;">
                        <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/poland.png" style="width: 20px; height: 14px; object-fit: cover;"> Polonya</div>
                        <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/brazil.png" style="width: 20px; height: 14px; object-fit: cover;"> Brezilya</div>
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 8px; font-size: 15px; font-weight: 900; color: #f6c343; text-align: right;"><span>1</span><span>1</span></div>
                </div>
                <div style="background: #182012; border-radius: 8px; padding: 7px 12px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                    <div>1 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">1.90</span></div>
                    <div>2 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">1.85</span></div>
                </div>
            </div>
        </div>

        <!-- BUZ HOKEYI -->
        <div class="live-sport-panel" data-sport="hockey" style="display: none; gap: 14px; width: 100%;">
            <!-- Edmonton Oilers vs Florida Panthers -->
            <div style="background: #11170d; border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; min-width: 320px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a1a1aa; font-weight: 600;"><span style="display: inline-block; width: 14px; height: 10px; background: #06b6d4; border-radius: 2px;"></span> NHL Stanley Cup</div>
                    <span style="font-size: 14px; color: #71717a;">☆</span>
                </div>
                <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; font-weight: 700; color: #ef4444;"><span style="display: inline-block; width: 6px; height: 6px; background: #ef4444; border-radius: 50%;"></span> (•) 2. Periyot 11:45 <span style="color: #71717a;">📺</span></div>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="display: flex; flex-direction: column; gap: 8px;">
                        <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/oilers.png" style="width: 20px; height: 20px; object-fit: contain;"> Edmonton Oilers</div>
                        <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/panthers.png" style="width: 20px; height: 20px; object-fit: contain;"> Florida Panthers</div>
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 8px; font-size: 15px; font-weight: 900; color: #f6c343; text-align: right;"><span>2</span><span>3</span></div>
                </div>
                <div style="background: #182012; border-radius: 8px; padding: 7px 12px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                    <div>1 <span style="color: #f6c343; font-weight: 800; margin-left: 12px;">2.45</span></div>
                    <div>X <span style="color: #f6c343; font-weight: 800; margin-left: 12px;">4.10</span></div>
                    <div>2 <span style="color: #f6c343; font-weight: 800; margin-left: 12px;">2.30</span></div>
                </div>
            </div>
        </div>
    </div>
</div>
'''

# 2. Tum Spor Branslari Icin Interaktif Mac Oncesi Verisi ve HTML Yapisi
sports_prematch_complete = '''
<div class="sport_widgets" id="js-sport-Prematch-cont" style="padding: 0 4px;">
    <!-- Spor Brans Butonlari (Interaktif Tiklanabilir Filtre) -->
    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 14px; overflow-x: auto; padding: 2px 0; scrollbar-width: none;">
        <div class="sport-filter-btn active" data-target="prematch" data-sport="football" style="background: #f6c343; color: #10160b; border-radius: 20px; padding: 6px 16px; font-size: 13px; font-weight: 800; display: flex; align-items: center; gap: 8px; cursor: pointer; white-space: nowrap;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polygon points="12 8 8 11 9.5 15 14.5 15 16 11 12 8" fill="currentColor"></polygon></svg>
            Futbol
        </div>
        <div class="sport-filter-btn" data-target="prematch" data-sport="basketball" style="background: rgba(255,255,255,0.06); color: #d4d4d8; border-radius: 20px; padding: 6px 14px; font-size: 13px; font-weight: 800; display: flex; align-items: center; gap: 8px; cursor: pointer; white-space: nowrap;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M5 5a14 14 0 0 0 14 14"></path><path d="M19 5a14 14 0 0 1-14 14"></path><line x1="12" y1="2" x2="12" y2="22"></line><line x1="2" y1="12" x2="22" y2="12"></line></svg>
            Basketbol
        </div>
        <div class="sport-filter-btn" data-target="prematch" data-sport="tennis" style="background: rgba(255,255,255,0.06); color: #d4d4d8; border-radius: 20px; padding: 6px 14px; font-size: 13px; font-weight: 800; display: flex; align-items: center; gap: 8px; cursor: pointer; white-space: nowrap;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M18 12a6 6 0 0 0-6-6"></path><path d="M6 12a6 6 0 0 0 6 6"></path></svg>
            Tenis
        </div>
        <div class="sport-filter-btn" data-target="prematch" data-sport="volleyball" style="background: rgba(255,255,255,0.06); color: #d4d4d8; border-radius: 20px; padding: 6px 14px; font-size: 13px; font-weight: 800; display: flex; align-items: center; gap: 8px; cursor: pointer; white-space: nowrap;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 12a10 10 0 0 0 10 0"></path><path d="M12 12a10 10 0 0 0-5 8.66"></path><path d="M12 12a10 10 0 0 0-5-8.66"></path></svg>
            Voleybol
        </div>
        <div class="sport-filter-btn" data-target="prematch" data-sport="hockey" style="background: rgba(255,255,255,0.06); color: #d4d4d8; border-radius: 20px; padding: 6px 14px; font-size: 13px; font-weight: 800; display: flex; align-items: center; gap: 8px; cursor: pointer; white-space: nowrap;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><ellipse cx="12" cy="12" rx="9" ry="4"></ellipse><path d="M3 12v3c0 2.2 4 4 9 4s9-1.8 9-4v-3"></path></svg>
            Buz Hokeyi
        </div>
    </div>

    <!-- Mac Oncesi Listeleri -->
    <div id="prematch_cards_container" style="display: flex; gap: 14px; overflow-x: auto; padding: 4px 0 16px 0; width: 100%; scrollbar-width: none;">
        <!-- FUTBOL (Varsayilan) -->
        <div class="prematch-sport-panel" data-sport="football" style="display: flex; gap: 14px; width: 100%;">
            <!-- Meksika vs Jamaica -->
            <div style="background: #11170d; border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; min-width: 320px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a1a1aa; font-weight: 600;"><span style="display: inline-block; width: 14px; height: 10px; background: #3b82f6; border-radius: 2px;"></span> CONCACAF Uluslar Lig</div>
                    <span style="font-size: 14px; color: #71717a;">☆</span>
                </div>
                <div style="font-size: 12px; font-weight: 700; color: #a1a1aa;">18.11 5:30</div>
                <div style="display: flex; flex-direction: column; gap: 8px;">
                    <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/mexico.png" style="width: 20px; height: 14px; object-fit: cover;"> Meksika</div>
                    <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/jamaica.png" style="width: 20px; height: 14px; object-fit: cover;"> Jamaica</div>
                </div>
                <div style="background: #182012; border-radius: 8px; padding: 6px 10px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                    <div>1 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">1.12</span></div>
                    <div>X <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">8</span></div>
                    <div>2 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">15</span></div>
                </div>
            </div>
            <!-- Real Madrid(K) vs Inter Milano(K) -->
            <div style="background: #11170d; border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; min-width: 320px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a1a1aa; font-weight: 600;"><span style="display: inline-block; width: 14px; height: 10px; background: #3b82f6; border-radius: 2px;"></span> Kadınlar. UEFA Şampiyonlar Ligi</div>
                    <span style="font-size: 14px; color: #71717a;">☆</span>
                </div>
                <div style="font-size: 12px; font-weight: 700; color: #a1a1aa;">18.11 20:45</div>
                <div style="display: flex; flex-direction: column; gap: 8px;">
                    <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/realmadrid.png" style="width: 18px; height: 18px; object-fit: contain;"> Real Madrid(K)</div>
                    <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/inter.png" style="width: 18px; height: 18px; object-fit: contain;"> Inter Milano(K)</div>
                </div>
                <div style="background: #182012; border-radius: 8px; padding: 6px 10px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                    <div>1 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">1.21</span></div>
                    <div>X <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">6</span></div>
                    <div>2 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">9.5</span></div>
                </div>
            </div>
        </div>

        <!-- BASKETBOL -->
        <div class="prematch-sport-panel" data-sport="basketball" style="display: none; gap: 14px; width: 100%;">
            <!-- Boston Celtics vs Miami Heat -->
            <div style="background: #11170d; border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; min-width: 320px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a1a1aa; font-weight: 600;"><span style="display: inline-block; width: 14px; height: 10px; background: #eab308; border-radius: 2px;"></span> NBA</div>
                    <span style="font-size: 14px; color: #71717a;">☆</span>
                </div>
                <div style="font-size: 12px; font-weight: 700; color: #a1a1aa;">Yarın 03:30</div>
                <div style="display: flex; flex-direction: column; gap: 8px;">
                    <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/usa.png" style="width: 20px; height: 14px; object-fit: cover;"> Boston Celtics</div>
                    <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/usa.png" style="width: 20px; height: 14px; object-fit: cover;"> Miami Heat</div>
                </div>
                <div style="background: #182012; border-radius: 8px; padding: 6px 10px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                    <div>1 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">1.35</span></div>
                    <div>2 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">3.20</span></div>
                </div>
            </div>
        </div>

        <!-- TENIS -->
        <div class="prematch-sport-panel" data-sport="tennis" style="display: none; gap: 14px; width: 100%;">
            <!-- Djokovic vs Medvedev -->
            <div style="background: #11170d; border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; min-width: 320px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a1a1aa; font-weight: 600;"><span style="display: inline-block; width: 14px; height: 10px; background: #10b981; border-radius: 2px;"></span> ATP Masters</div>
                    <span style="font-size: 14px; color: #71717a;">☆</span>
                </div>
                <div style="font-size: 12px; font-weight: 700; color: #a1a1aa;">Yarın 16:00</div>
                <div style="display: flex; flex-direction: column; gap: 8px;">
                    <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/djokovic.png" style="width: 20px; height: 14px; object-fit: cover;"> Novak Djokovic</div>
                    <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/medvedev.png" style="width: 20px; height: 14px; object-fit: cover;"> Daniil Medvedev</div>
                </div>
                <div style="background: #182012; border-radius: 8px; padding: 6px 10px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                    <div>1 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">1.75</span></div>
                    <div>2 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">2.05</span></div>
                </div>
            </div>
        </div>

        <!-- VOLEYBOL -->
        <div class="prematch-sport-panel" data-sport="volleyball" style="display: none; gap: 14px; width: 100%;">
            <!-- VakıfBank vs Eczacıbaşı -->
            <div style="background: #11170d; border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; min-width: 320px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a1a1aa; font-weight: 600;"><span style="display: inline-block; width: 14px; height: 10px; background: #8b5cf6; border-radius: 2px;"></span> Sultanlar Ligi</div>
                    <span style="font-size: 14px; color: #71717a;">☆</span>
                </div>
                <div style="font-size: 12px; font-weight: 700; color: #a1a1aa;">Yarın 19:30</div>
                <div style="display: flex; flex-direction: column; gap: 8px;">
                    <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/turkey.png" style="width: 20px; height: 14px; object-fit: cover;"> VakıfBank(K)</div>
                    <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/turkey.png" style="width: 20px; height: 14px; object-fit: cover;"> Eczacıbaşı(K)</div>
                </div>
                <div style="background: #182012; border-radius: 8px; padding: 6px 10px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                    <div>1 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">1.80</span></div>
                    <div>2 <span style="color: #f6c343; font-weight: 800; margin-left: 14px;">1.95</span></div>
                </div>
            </div>
        </div>

        <!-- BUZ HOKEYI -->
        <div class="prematch-sport-panel" data-sport="hockey" style="display: none; gap: 14px; width: 100%;">
            <!-- New York Rangers vs Toronto -->
            <div style="background: #11170d; border: 1px solid rgba(255,255,255,0.07); border-radius: 12px; min-width: 320px; flex: 1; padding: 14px 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.4); display: flex; flex-direction: column; gap: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: #a1a1aa; font-weight: 600;"><span style="display: inline-block; width: 14px; height: 10px; background: #06b6d4; border-radius: 2px;"></span> NHL</div>
                    <span style="font-size: 14px; color: #71717a;">☆</span>
                </div>
                <div style="font-size: 12px; font-weight: 700; color: #a1a1aa;">Yarın 02:00</div>
                <div style="display: flex; flex-direction: column; gap: 8px;">
                    <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/usa.png" style="width: 20px; height: 14px; object-fit: cover;"> NY Rangers</div>
                    <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #ffffff;"><img src="images/teams/usa.png" style="width: 20px; height: 14px; object-fit: cover;"> Toronto Maple Leafs</div>
                </div>
                <div style="background: #182012; border-radius: 8px; padding: 6px 10px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: #a1a1aa;">
                    <div>1 <span style="color: #f6c343; font-weight: 800; margin-left: 12px;">2.20</span></div>
                    <div>X <span style="color: #f6c343; font-weight: 800; margin-left: 12px;">3.90</span></div>
                    <div>2 <span style="color: #f6c343; font-weight: 800; margin-left: 12px;">2.60</span></div>
                </div>
            </div>
        </div>
    </div>
</div>
'''

# 3. Interaktif Tab Gecis JS Scripti (Kullanici Basketbol, Tenis vb. tikladiginda maclar aninda degisir)
filter_click_script = '''
<script>
(function() {
    document.querySelectorAll('.sport-filter-btn').forEach(function(btn) {
        btn.addEventListener('click', function() {
            var targetType = this.getAttribute('data-target'); // 'live' or 'prematch'
            var sport = this.getAttribute('data-sport');

            // Tum kardes butonlarin aktifligini kaldir
            var parent = this.parentElement;
            parent.querySelectorAll('.sport-filter-btn').forEach(function(b) {
                b.style.background = 'rgba(255,255,255,0.06)';
                b.style.color = '#d4d4d8';
            });

            // Secili butonu altin sarisi yap
            this.style.background = '#f6c343';
            this.style.color = '#10160b';

            // Ilgili panelleri goster / gizle
            var panelClass = (targetType === 'live') ? '.live-sport-panel' : '.prematch-sport-panel';
            document.querySelectorAll(panelClass).forEach(function(panel) {
                if (panel.getAttribute('data-sport') === sport) {
                    panel.style.display = 'flex';
                } else {
                    panel.style.display = 'none';
                }
            });
        });
    });
})();
</script>
'''

# index.html icindeki Canli ve Mac Oncesi alanlarini guncelle
p_live = html.find('id="js-sport-Live-cont"')
if p_live != -1:
    p_pre = html.find('Popüler Maç Öncesi', p_live)
    p_prev_div = html.rfind('<div class="dynamic_container">', p_live, p_pre)
    html = html[:p_live-30] + sports_live_complete + '</div>\n' + html[p_prev_div:]

p_pre_idx = html.find('id="js-sport-Prematch-cont"')
if p_pre_idx != -1:
    p_next_dyn = html.find('<div class="dynamic_container">', p_pre_idx)
    html = html[:p_pre_idx-30] + sports_prematch_complete + '</div>\n' + html[p_next_dyn:]

if '</body>' in html:
    html = html.replace('</body>', filter_click_script + '\n</body>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Tum spor branslari icin canli ve mac oncesi maclar canli filtreyle monte edildi!')
