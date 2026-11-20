html_path = r'C:\Users\laure\.gemini\antigravity\scratch\GrandPashabetSite\site\index.html'

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Orijinal Ekran Goruntusundeki Birebir Amusnet Kartlari
amusnet_clean_exact = '''
<div id="jackpot_container_16" class="jackpot_container onerow" style="padding: 0 4px; overflow-x: auto; scrollbar-width: none;">
    <div style="display: flex; gap: 12px; padding: 4px 12px 14px 12px; width: max-content;">
        
        <!-- Level 1: Club (Sinek) - 4000.25 TRY -->
        <div style="background: linear-gradient(180deg, #1b230f 0%, #111709 100%); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 12px 18px; min-width: 175px; display: flex; align-items: center; gap: 12px; box-shadow: 0 6px 16px rgba(0,0,0,0.45);">
            <div style="width: 38px; height: 38px; flex-shrink: 0; background-image: url('images/cdn/egt_jackpot_icons_new.png'); background-size: 38px 162px; background-position: 0 -122px; filter: drop-shadow(0 0 6px rgba(163,230,53,0.3));"></div>
            <div style="color: #f6c343; font-size: 15px; font-weight: 800; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; white-space: nowrap; letter-spacing: 0.3px;">
                <span id="amus_clean_1">4000.25</span> TRY
            </div>
        </div>

        <!-- Level 2: Diamond (Karo) - 07211.23 TRY -->
        <div style="background: linear-gradient(180deg, #1b230f 0%, #111709 100%); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 12px 18px; min-width: 175px; display: flex; align-items: center; gap: 12px; box-shadow: 0 6px 16px rgba(0,0,0,0.45);">
            <div style="width: 38px; height: 38px; flex-shrink: 0; background-image: url('images/cdn/egt_jackpot_icons_new.png'); background-size: 38px 162px; background-position: 0 -81px; filter: drop-shadow(0 0 6px rgba(244,63,94,0.3));"></div>
            <div style="color: #f6c343; font-size: 15px; font-weight: 800; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; white-space: nowrap; letter-spacing: 0.3px;">
                <span id="amus_clean_2">07211.23</span> TRY
            </div>
        </div>

        <!-- Level 3: Heart (Kupa) - 912020.34 TRY -->
        <div style="background: linear-gradient(180deg, #1b230f 0%, #111709 100%); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 12px 18px; min-width: 175px; display: flex; align-items: center; gap: 12px; box-shadow: 0 6px 16px rgba(0,0,0,0.45);">
            <div style="width: 38px; height: 38px; flex-shrink: 0; background-image: url('images/cdn/egt_jackpot_icons_new.png'); background-size: 38px 162px; background-position: 0 -40px; filter: drop-shadow(0 0 6px rgba(234,179,8,0.3));"></div>
            <div style="color: #f6c343; font-size: 15px; font-weight: 800; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; white-space: nowrap; letter-spacing: 0.3px;">
                <span id="amus_clean_3">912020.34</span> TRY
            </div>
        </div>

        <!-- Level 4: Spade (Maça) - 22462083.86 TRY -->
        <div style="background: linear-gradient(180deg, #1b230f 0%, #111709 100%); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 12px 18px; min-width: 195px; display: flex; align-items: center; gap: 12px; box-shadow: 0 6px 16px rgba(0,0,0,0.45);">
            <div style="width: 38px; height: 38px; flex-shrink: 0; background-image: url('images/cdn/egt_jackpot_icons_new.png'); background-size: 38px 162px; background-position: 0 0; filter: drop-shadow(0 0 6px rgba(168,85,247,0.3));"></div>
            <div style="color: #f6c343; font-size: 15px; font-weight: 800; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; white-space: nowrap; letter-spacing: 0.3px;">
                <span id="amus_clean_4">22462083.86</span> TRY
            </div>
        </div>

    </div>
</div>
'''

# Canli Artis Scripti (Fotograftaki formatin birebiri: 4000.25 TRY)
clean_ticker_script = '''
<script>
(function() {
    let a1 = 4000.25;
    let a2 = 7211.23;
    let a3 = 912020.34;
    let a4 = 22462083.86;

    function formatClean(val, minIntLen) {
        let parts = val.toFixed(2).split('.');
        while (parts[0].length < minIntLen) {
            parts[0] = '0' + parts[0];
        }
        return parts.join('.');
    }

    setInterval(function() {
        a1 += (Math.random() * 0.25 + 0.05);
        a2 += (Math.random() * 0.45 + 0.10);
        a3 += (Math.random() * 2.20 + 0.50);
        a4 += (Math.random() * 6.50 + 1.20);

        let e1 = document.getElementById('amus_clean_1');
        let e2 = document.getElementById('amus_clean_2');
        let e3 = document.getElementById('amus_clean_3');
        let e4 = document.getElementById('amus_clean_4');

        if (e1) e1.textContent = formatClean(a1, 4);
        if (e2) e2.textContent = formatClean(a2, 5);
        if (e3) e3.textContent = formatClean(a3, 6);
        if (e4) e4.textContent = formatClean(a4, 8);
    }, 450);
})();
</script>
'''

p_start = html.find('id="jackpot_container_16"')
if p_start != -1:
    p_div_start = html.rfind('<div', 0, p_start)
    # Bu bolumun bitisini bul (Spor Jackpot oncesi)
    p_spor = html.find('Spor Jackpot', p_start)
    p_dyn = html.rfind('<div class="dynamic_container">', p_start, p_spor)
    html = html[:p_div_start] + amusnet_clean_exact + '</div>\n' + html[p_dyn:]
    print('Amusnet alani birebir fotograftaki temiz formata cevrildi!')

if '</body>' in html:
    html = html.replace('</body>', clean_ticker_script + '\n</body>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Bitti!')
