html_path = r'C:\Users\laure\.gemini\antigravity\scratch\GrandPashabetSite\site\index.html'

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Orijinal kayan slot makinesi cercevesi ve animasyonlu donen sayac stili
slot_roller_markup = '''
<style>
/* Gercek Slot Roller / Donen Cark Stilleri */
.slot-jackpot-card {
    background: linear-gradient(180deg, #242c12 0%, #151a0b 100%);
    border-radius: 12px;
    padding: 12px 18px;
    min-width: 220px;
    flex: 1;
    display: flex;
    align-items: center;
    gap: 14px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.4);
    border: 1px solid rgba(255,255,255,0.06);
    position: relative;
}

.slot-roller-container {
    display: flex;
    align-items: center;
    font-family: monospace, sans-serif;
    font-weight: 800;
    font-size: 21px;
    color: #f6c343;
    line-height: 24px;
    height: 24px;
    overflow: hidden;
}

.slot-reel {
    height: 24px;
    line-height: 24px;
    overflow: hidden;
    display: inline-block;
    position: relative;
    width: 14px;
    text-align: center;
}

.slot-reel-strip {
    display: flex;
    flex-direction: column;
    transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.3, 1);
}

.slot-reel-strip span {
    height: 24px;
    line-height: 24px;
    display: block;
    text-align: center;
}

.slot-static-char {
    display: inline-block;
    text-align: center;
    color: #f6c343;
}

.slot-currency {
    color: #f6c343;
    font-size: 13px;
    font-weight: 700;
    margin-left: 6px;
}
</style>

<div id="jackpot_container_16" class="jackpot_container onerow">
    <div style="display: flex; gap: 14px; overflow-x: auto; padding: 6px 0 14px 0; width: 100%; scrollbar-width: none;">
        <!-- Level 1: Club (Sinek) -->
        <div class="slot-jackpot-card">
            <div style="width: 44px; height: 44px; flex-shrink: 0; background-image: url('images/cdn/egt_jackpot_icons_new.png'); background-size: 44px 188px; background-position: 0 -141px; filter: drop-shadow(0 0 6px rgba(163,230,53,0.4));"></div>
            <div class="slot-roller-container" id="roller_amus_1">
                <!-- Dinamik Carklar JS Tarafindan Olusturulur -->
            </div>
            <span class="slot-currency">TRY</span>
        </div>

        <!-- Level 2: Diamond (Karo) -->
        <div class="slot-jackpot-card">
            <div style="width: 44px; height: 44px; flex-shrink: 0; background-image: url('images/cdn/egt_jackpot_icons_new.png'); background-size: 44px 188px; background-position: 0 -94px; filter: drop-shadow(0 0 6px rgba(244,63,94,0.4));"></div>
            <div class="slot-roller-container" id="roller_amus_2">
            </div>
            <span class="slot-currency">TRY</span>
        </div>

        <!-- Level 3: Heart (Kupa) -->
        <div class="slot-jackpot-card">
            <div style="width: 44px; height: 44px; flex-shrink: 0; background-image: url('images/cdn/egt_jackpot_icons_new.png'); background-size: 44px 188px; background-position: 0 -47px; filter: drop-shadow(0 0 6px rgba(234,179,8,0.4));"></div>
            <div class="slot-roller-container" id="roller_amus_3">
            </div>
            <span class="slot-currency">TRY</span>
        </div>

        <!-- Level 4: Spade (Maca) -->
        <div class="slot-jackpot-card">
            <div style="width: 44px; height: 44px; flex-shrink: 0; background-image: url('images/cdn/egt_jackpot_icons_new.png'); background-size: 44px 188px; background-position: 0 0; filter: drop-shadow(0 0 6px rgba(168,85,247,0.4));"></div>
            <div class="slot-roller-container" id="roller_amus_4">
            </div>
            <span class="slot-currency">TRY</span>
        </div>
    </div>
</div>
'''

# Spor Jackpot Alani (Ekran Goruntundeki Tasarimin Birebiri)
slot_spor_markup = '''
<div id="jackpot_container_94" class="jackpot_container">
    <div style="display: flex; gap: 16px; overflow-x: auto; padding: 6px 0 16px 0; width: 100%; scrollbar-width: none;">
        <!-- Spor MEGA -->
        <div style="background: linear-gradient(135deg, rgba(16,35,45,0.85) 0%, rgba(10,18,12,0.95) 100%); border-radius: 14px; padding: 14px 20px; min-width: 290px; flex: 1; display: flex; justify-content: space-between; align-items: center; border: 1px solid rgba(56,189,248,0.25); box-shadow: 0 8px 20px rgba(0,0,0,0.4); position: relative; overflow: hidden;">
            <div style="display: flex; flex-direction: column; gap: 4px;">
                <div style="font-size: 13px; color: #94a3b8; font-weight: 600;"><span style="color: #ffffff; font-weight: 800;">MEGA</span> • Minimum Bahis TRY 1 000</div>
                <div style="display: flex; align-items: center; gap: 6px;">
                    <span style="color: #ffffff; font-size: 22px; font-weight: 900;">TRY</span>
                    <div class="slot-roller-container" id="roller_spor_1" style="color: #ffffff; font-size: 22px; font-weight: 900; height: 26px;"></div>
                </div>
            </div>
            <div style="width: 48px; height: 56px; flex-shrink: 0; background-image: url('images/cdn/sport_jackpot_icons.png'); background-size: 48px 205px; background-position: 0 0; filter: drop-shadow(0 0 10px rgba(56,189,248,0.6));"></div>
        </div>

        <!-- Spor MAJOR -->
        <div style="background: linear-gradient(135deg, rgba(45,18,18,0.85) 0%, rgba(10,18,12,0.95) 100%); border-radius: 14px; padding: 14px 20px; min-width: 290px; flex: 1; display: flex; justify-content: space-between; align-items: center; border: 1px solid rgba(239,68,68,0.25); box-shadow: 0 8px 20px rgba(0,0,0,0.4); position: relative; overflow: hidden;">
            <div style="display: flex; flex-direction: column; gap: 4px;">
                <div style="font-size: 13px; color: #94a3b8; font-weight: 600;"><span style="color: #ffffff; font-weight: 800;">MAJOR</span> • Minimum Bahis TRY 500</div>
                <div style="display: flex; align-items: center; gap: 6px;">
                    <span style="color: #ffffff; font-size: 22px; font-weight: 900;">TRY</span>
                    <div class="slot-roller-container" id="roller_spor_2" style="color: #ffffff; font-size: 22px; font-weight: 900; height: 26px;"></div>
                </div>
            </div>
            <div style="width: 48px; height: 56px; flex-shrink: 0; background-image: url('images/cdn/sport_jackpot_icons.png'); background-size: 48px 205px; background-position: 0 -51px; filter: drop-shadow(0 0 10px rgba(239,68,68,0.6));"></div>
        </div>

        <!-- Spor MINOR -->
        <div style="background: linear-gradient(135deg, rgba(20,30,35,0.85) 0%, rgba(10,18,12,0.95) 100%); border-radius: 14px; padding: 14px 20px; min-width: 290px; flex: 1; display: flex; justify-content: space-between; align-items: center; border: 1px solid rgba(148,163,184,0.25); box-shadow: 0 8px 20px rgba(0,0,0,0.4); position: relative; overflow: hidden;">
            <div style="display: flex; flex-direction: column; gap: 4px;">
                <div style="font-size: 13px; color: #94a3b8; font-weight: 600;"><span style="color: #ffffff; font-weight: 800;">MINOR</span> • Minimum Bahis TRY 50</div>
                <div style="display: flex; align-items: center; gap: 6px;">
                    <span style="color: #ffffff; font-size: 22px; font-weight: 900;">TRY</span>
                    <div class="slot-roller-container" id="roller_spor_3" style="color: #ffffff; font-size: 22px; font-weight: 900; height: 26px;"></div>
                </div>
            </div>
            <div style="width: 48px; height: 56px; flex-shrink: 0; background-image: url('images/cdn/sport_jackpot_icons.png'); background-size: 48px 205px; background-position: 0 -102px; filter: drop-shadow(0 0 10px rgba(255,255,255,0.4));"></div>
        </div>
    </div>
</div>
'''

# Dikey Donen Cark Animasyon Motoru
roller_engine_script = '''
<script>
(function() {
    function SlotRoller(containerId, isSpaceDelimited) {
        this.container = document.getElementById(containerId);
        this.isSpace = isSpaceDelimited;
        this.reels = [];
    }

    SlotRoller.prototype.render = function(numStr) {
        if (!this.container) return;
        
        // Eger basamak sayisi veya sembol sayisi ayniysa var olan carklari dondur
        let cleanChars = numStr.split('');
        if (this.reels.length !== cleanChars.length) {
            this.container.innerHTML = '';
            this.reels = [];
            for (let i = 0; i < cleanChars.length; i++) {
                let ch = cleanChars[i];
                if (ch >= '0' && ch <= '9') {
                    let reelDiv = document.createElement('div');
                    reelDiv.className = 'slot-reel';
                    let strip = document.createElement('div');
                    strip.className = 'slot-reel-strip';
                    for (let d = 0; d <= 9; d++) {
                        let span = document.createElement('span');
                        span.textContent = d;
                        strip.appendChild(span);
                    }
                    reelDiv.appendChild(strip);
                    this.container.appendChild(reelDiv);
                    this.reels.push({ type: 'digit', strip: strip });
                } else {
                    let staticSpan = document.createElement('span');
                    staticSpan.className = 'slot-static-char';
                    staticSpan.textContent = ch;
                    if (ch === '.' || ch === ',') {
                        staticSpan.style.width = '6px';
                    } else if (ch === ' ') {
                        staticSpan.style.width = '8px';
                    }
                    this.container.appendChild(staticSpan);
                    this.reels.push({ type: 'static', el: staticSpan });
                }
            }
        }

        // Carklari dondur
        for (let i = 0; i < cleanChars.length; i++) {
            let ch = cleanChars[i];
            let reel = this.reels[i];
            if (reel && reel.type === 'digit') {
                let digit = parseInt(ch, 10);
                let offset = -(digit * 24);
                reel.strip.style.transform = 'translateY(' + offset + 'px)';
            }
        }
    };

    function formatTr(val) {
        let parts = val.toFixed(2).split('.');
        parts[0] = parts[0].replace(/\\B(?=(\\d{3})+(?!\\d))/g, ".");
        return parts.join(',');
    }

    function formatSpace(val) {
        let parts = val.toFixed(2).split('.');
        parts[0] = parts[0].replace(/\\B(?=(\\d{3})+(?!\\d))/g, " ");
        return parts.join('.');
    }

    // Baslangic degerleri
    let val_a1 = 1909.34;
    let val_a2 = 29516.67;
    let val_a3 = 943149.02;
    let val_a4 = 2333274.39;

    let val_s1 = 1648681.89;
    let val_s2 = 27594.78;
    let val_s3 = 2701.44;

    let r_a1 = new SlotRoller('roller_amus_1', false);
    let r_a2 = new SlotRoller('roller_amus_2', false);
    let r_a3 = new SlotRoller('roller_amus_3', false);
    let r_a4 = new SlotRoller('roller_amus_4', false);

    let r_s1 = new SlotRoller('roller_spor_1', true);
    let r_s2 = new SlotRoller('roller_spor_2', true);
    let r_s3 = new SlotRoller('roller_spor_3', true);

    function update() {
        r_a1.render(formatTr(val_a1));
        r_a2.render(formatTr(val_a2));
        r_a3.render(formatTr(val_a3));
        r_a4.render(formatTr(val_a4));

        r_s1.render(formatSpace(val_s1));
        r_s2.render(formatSpace(val_s2));
        r_s3.render(formatSpace(val_s3));
    }

    update();

    // Surekli oynayan canli artis
    setInterval(function() {
        val_a1 += (Math.random() * 0.35 + 0.05);
        val_a2 += (Math.random() * 0.90 + 0.15);
        val_a3 += (Math.random() * 2.80 + 0.60);
        val_a4 += (Math.random() * 6.50 + 1.50);

        val_s1 += (Math.random() * 4.20 + 0.90);
        val_s2 += (Math.random() * 1.10 + 0.20);
        val_s3 += (Math.random() * 0.25 + 0.04);

        update();
    }, 450);
})();
</script>
'''

# 1. Eski Amusnet alani yerine slot roller ekle
p_start = html.find('id="jackpot_container_16"')
if p_start != -1:
    p_end = html.find('</div>\n                        </div>\n                        <div class="dynamic_container">', p_start)
    if p_end != -1:
        html = html[:p_start-5] + slot_roller_markup + html[p_end:]
    else:
        p_spor = html.find('Spor Jackpot', p_start)
        p_prev = html.rfind('<div class="dynamic_container">', p_start, p_spor)
        html = html[:p_start-5] + slot_roller_markup + '</div>\n</div>\n' + html[p_prev:]

# 2. Eski Spor Jackpot alani yerine slot roller ekle
s_start = html.find('id="jackpot_container_94"')
if s_start != -1:
    s_end = html.find('</div>\n                        </div>\n                        <div class="dynamic_container">', s_start)
    if s_end != -1:
        html = html[:s_start-5] + slot_spor_markup + html[s_end:]
    else:
        s_end2 = html.find('<div class="dynamic_featured_content', s_start)
        s_prev_div = html.rfind('</div>', s_start, s_end2)
        html = html[:s_start-5] + slot_spor_markup + html[s_prev_div:]

# 3. Eski ticker scriptini kaldir ve yeni cark motorunu ekle
if '</body>' in html:
    # eski scripti temizle
    old_script_pos = html.rfind('<script>')
    if old_script_pos != -1 and 'formatTr' in html[old_script_pos:]:
        html = html[:old_script_pos] + roller_engine_script + '\n</body></html>'
    else:
        html = html.replace('</body>', roller_engine_script + '\n</body>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Slot makinesi cark motoru basariyla monte edildi!')
