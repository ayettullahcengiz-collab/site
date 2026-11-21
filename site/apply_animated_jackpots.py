html_path = r'.\index.html'

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Orijinal 3D parlak kristalli EGT/Amusnet ve Spor Jackpot kartlari + canli yukselen sayac animasyon scripti
animated_jackpots = '''
<div id="jackpot_container_16" class="jackpot_container onerow">
    <div style="display: flex; gap: 14px; overflow-x: auto; padding: 6px 0 14px 0; width: 100%; scrollbar-width: none;">
        <!-- Level 1: Club (Sinek) -->
        <div style="background: linear-gradient(180deg, #1f2710 0%, #151a0b 100%); border-radius: 12px; padding: 12px 18px; min-width: 220px; flex: 1; display: flex; align-items: center; gap: 14px; box-shadow: 0 8px 16px rgba(0,0,0,0.4); border: 1px solid rgba(255,255,255,0.05); position: relative; overflow: hidden;">
            <div style="width: 44px; height: 44px; flex-shrink: 0; background-image: url('images/cdn/egt_jackpot_icons_new.png'); background-size: 44px 188px; background-position: 0 -141px; filter: drop-shadow(0 0 6px rgba(163,230,53,0.4));"></div>
            <div style="display: flex; align-items: baseline; gap: 6px;">
                <span id="amusnet_val_1" style="color: #f6c343; font-size: 20px; font-weight: 800; font-family: monospace, sans-serif; letter-spacing: 0.5px;">1.909,34</span>
                <span style="color: #f6c343; font-size: 13px; font-weight: 700;">TRY</span>
            </div>
        </div>

        <!-- Level 2: Diamond (Karo) -->
        <div style="background: linear-gradient(180deg, #1f2710 0%, #151a0b 100%); border-radius: 12px; padding: 12px 18px; min-width: 220px; flex: 1; display: flex; align-items: center; gap: 14px; box-shadow: 0 8px 16px rgba(0,0,0,0.4); border: 1px solid rgba(255,255,255,0.05); position: relative; overflow: hidden;">
            <div style="width: 44px; height: 44px; flex-shrink: 0; background-image: url('images/cdn/egt_jackpot_icons_new.png'); background-size: 44px 188px; background-position: 0 -94px; filter: drop-shadow(0 0 6px rgba(244,63,94,0.4));"></div>
            <div style="display: flex; align-items: baseline; gap: 6px;">
                <span id="amusnet_val_2" style="color: #f6c343; font-size: 20px; font-weight: 800; font-family: monospace, sans-serif; letter-spacing: 0.5px;">27.899,87</span>
                <span style="color: #f6c343; font-size: 13px; font-weight: 700;">TRY</span>
            </div>
        </div>

        <!-- Level 3: Heart (Kupa) -->
        <div style="background: linear-gradient(180deg, #1f2710 0%, #151a0b 100%); border-radius: 12px; padding: 12px 18px; min-width: 220px; flex: 1; display: flex; align-items: center; gap: 14px; box-shadow: 0 8px 16px rgba(0,0,0,0.4); border: 1px solid rgba(255,255,255,0.05); position: relative; overflow: hidden;">
            <div style="width: 44px; height: 44px; flex-shrink: 0; background-image: url('images/cdn/egt_jackpot_icons_new.png'); background-size: 44px 188px; background-position: 0 -47px; filter: drop-shadow(0 0 6px rgba(234,179,8,0.4));"></div>
            <div style="display: flex; align-items: baseline; gap: 6px;">
                <span id="amusnet_val_3" style="color: #f6c343; font-size: 20px; font-weight: 800; font-family: monospace, sans-serif; letter-spacing: 0.5px;">941.333,77</span>
                <span style="color: #f6c343; font-size: 13px; font-weight: 700;">TRY</span>
            </div>
        </div>

        <!-- Level 4: Spade (Maca) -->
        <div style="background: linear-gradient(180deg, #1f2710 0%, #151a0b 100%); border-radius: 12px; padding: 12px 18px; min-width: 220px; flex: 1; display: flex; align-items: center; gap: 14px; box-shadow: 0 8px 16px rgba(0,0,0,0.4); border: 1px solid rgba(255,255,255,0.05); position: relative; overflow: hidden;">
            <div style="width: 44px; height: 44px; flex-shrink: 0; background-image: url('images/cdn/egt_jackpot_icons_new.png'); background-size: 44px 188px; background-position: 0 0; filter: drop-shadow(0 0 6px rgba(168,85,247,0.4));"></div>
            <div style="display: flex; align-items: baseline; gap: 6px;">
                <span id="amusnet_val_4" style="color: #f6c343; font-size: 20px; font-weight: 800; font-family: monospace, sans-serif; letter-spacing: 0.5px;">2.333.928,14</span>
                <span style="color: #f6c343; font-size: 13px; font-weight: 700;">TRY</span>
            </div>
        </div>
    </div>
</div>
'''

animated_spor_jackpot = '''
<div id="jackpot_container_94" class="jackpot_container">
    <div style="display: flex; gap: 16px; overflow-x: auto; padding: 6px 0 16px 0; width: 100%; scrollbar-width: none;">
        <!-- Spor MEGA -->
        <div style="background: linear-gradient(135deg, rgba(16,35,45,0.85) 0%, rgba(10,18,12,0.95) 100%); border-radius: 14px; padding: 14px 20px; min-width: 280px; flex: 1; display: flex; justify-content: space-between; align-items: center; border: 1px solid rgba(56,189,248,0.25); box-shadow: 0 8px 20px rgba(0,0,0,0.4); position: relative; overflow: hidden;">
            <div style="display: flex; flex-direction: column; gap: 4px;">
                <div style="font-size: 13px; color: #94a3b8; font-weight: 600;"><span style="color: #ffffff; font-weight: 800;">MEGA</span> • Minimum Bahis TRY 1 000</div>
                <div style="color: #ffffff; font-size: 22px; font-weight: 900; font-family: monospace, sans-serif; letter-spacing: 0.5px;">TRY <span id="spor_val_1">1 648 550.14</span></div>
            </div>
            <div style="width: 48px; height: 56px; flex-shrink: 0; background-image: url('images/cdn/sport_jackpot_icons.png'); background-size: 48px 205px; background-position: 0 0; filter: drop-shadow(0 0 10px rgba(56,189,248,0.6));"></div>
        </div>

        <!-- Spor MAJOR -->
        <div style="background: linear-gradient(135deg, rgba(45,18,18,0.85) 0%, rgba(10,18,12,0.95) 100%); border-radius: 14px; padding: 14px 20px; min-width: 280px; flex: 1; display: flex; justify-content: space-between; align-items: center; border: 1px solid rgba(239,68,68,0.25); box-shadow: 0 8px 20px rgba(0,0,0,0.4); position: relative; overflow: hidden;">
            <div style="display: flex; flex-direction: column; gap: 4px;">
                <div style="font-size: 13px; color: #94a3b8; font-weight: 600;"><span style="color: #ffffff; font-weight: 800;">MAJOR</span> • Minimum Bahis TRY 500</div>
                <div style="color: #ffffff; font-size: 22px; font-weight: 900; font-family: monospace, sans-serif; letter-spacing: 0.5px;">TRY <span id="spor_val_2">27 463.04</span></div>
            </div>
            <div style="width: 48px; height: 56px; flex-shrink: 0; background-image: url('images/cdn/sport_jackpot_icons.png'); background-size: 48px 205px; background-position: 0 -51px; filter: drop-shadow(0 0 10px rgba(239,68,68,0.6));"></div>
        </div>

        <!-- Spor MINOR -->
        <div style="background: linear-gradient(135deg, rgba(20,30,35,0.85) 0%, rgba(10,18,12,0.95) 100%); border-radius: 14px; padding: 14px 20px; min-width: 280px; flex: 1; display: flex; justify-content: space-between; align-items: center; border: 1px solid rgba(148,163,184,0.25); box-shadow: 0 8px 20px rgba(0,0,0,0.4); position: relative; overflow: hidden;">
            <div style="display: flex; flex-direction: column; gap: 4px;">
                <div style="font-size: 13px; color: #94a3b8; font-weight: 600;"><span style="color: #ffffff; font-weight: 800;">MINOR</span> • Minimum Bahis TRY 50</div>
                <div style="color: #ffffff; font-size: 22px; font-weight: 900; font-family: monospace, sans-serif; letter-spacing: 0.5px;">TRY <span id="spor_val_3">2 536.75</span></div>
            </div>
            <div style="width: 48px; height: 56px; flex-shrink: 0; background-image: url('images/cdn/sport_jackpot_icons.png'); background-size: 48px 205px; background-position: 0 -102px; filter: drop-shadow(0 0 10px rgba(255,255,255,0.4));"></div>
        </div>
    </div>
</div>
'''

# Canli Jackpot Akis Scripti (Her 400ms - 800ms'de bir surekli artis)
ticker_script = '''
<script>
(function() {
    function formatTr(val, decimals) {
        let parts = val.toFixed(decimals).split('.');
        parts[0] = parts[0].replace(/\\B(?=(\\d{3})+(?!\\d))/g, ".");
        return parts.join(',');
    }

    function formatSpace(val, decimals) {
        let parts = val.toFixed(decimals).split('.');
        parts[0] = parts[0].replace(/\\B(?=(\\d{3})+(?!\\d))/g, " ");
        return parts.join('.');
    }

    let a1 = 1909.34, a2 = 27899.87, a3 = 941333.77, a4 = 2333928.14;
    let s1 = 1648550.14, s2 = 27463.04, s3 = 2536.75;

    setInterval(function() {
        a1 += (Math.random() * 0.45 + 0.05);
        a2 += (Math.random() * 1.25 + 0.20);
        a3 += (Math.random() * 3.80 + 0.80);
        a4 += (Math.random() * 8.50 + 2.10);

        s1 += (Math.random() * 5.60 + 1.20);
        s2 += (Math.random() * 1.50 + 0.30);
        s3 += (Math.random() * 0.35 + 0.05);

        let el_a1 = document.getElementById('amusnet_val_1');
        let el_a2 = document.getElementById('amusnet_val_2');
        let el_a3 = document.getElementById('amusnet_val_3');
        let el_a4 = document.getElementById('amusnet_val_4');

        if (el_a1) el_a1.textContent = formatTr(a1, 2);
        if (el_a2) el_a2.textContent = formatTr(a2, 2);
        if (el_a3) el_a3.textContent = formatTr(a3, 2);
        if (el_a4) el_a4.textContent = formatTr(a4, 2);

        let el_s1 = document.getElementById('spor_val_1');
        let el_s2 = document.getElementById('spor_val_2');
        let el_s3 = document.getElementById('spor_val_3');

        if (el_s1) el_s1.textContent = formatSpace(s1, 2);
        if (el_s2) el_s2.textContent = formatSpace(s2, 2);
        if (el_s3) el_s3.textContent = formatSpace(s3, 2);
    }, 450);
})();
</script>
'''

# 1. Amusnet kismini degistir
p_start = html.find('id="jackpot_container_16"')
if p_start != -1:
    p_end = html.find('</div>\n                        </div>\n                        <div class="dynamic_container">', p_start)
    if p_end != -1:
        html = html[:p_start-5] + animated_jackpots + html[p_end:]
    else:
        # alternatif
        p_spor = html.find('Spor Jackpot', p_start)
        p_prev = html.rfind('<div class="dynamic_container">', p_start, p_spor)
        html = html[:p_start-5] + animated_jackpots + '</div>\n</div>\n' + html[p_prev:]

# 2. Spor Jackpot kismini degistir
s_start = html.find('id="jackpot_container_94"')
if s_start != -1:
    s_end = html.find('</div>\n                        </div>\n                        <div class="dynamic_container">', s_start)
    if s_end != -1:
        html = html[:s_start-5] + animated_spor_jackpot + html[s_end:]
    else:
        s_end2 = html.find('<div class="dynamic_featured_content', s_start)
        s_prev_div = html.rfind('</div>', s_start, s_end2)
        html = html[:s_start-5] + animated_spor_jackpot + html[s_prev_div:]

# 3. Canli sayac animasyon scriptini </body> oncesine yerlestir
if '</body>' in html:
    html = html.replace('</body>', ticker_script + '\n</body>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Orijinal 3D kristalli ve canli oynayan jackpotlar basariyla kuruldu!')
