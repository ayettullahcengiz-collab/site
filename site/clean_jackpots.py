import re

html_path = r'.\index.html'

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Amusnet orijinal 4 kart: Sinek (Club), Karo (Diamond), Kupa (Heart), Maça (Spade)
amusnet_real = '''id="jackpot_container_16" class="jackpot_container onerow">
    <div style="display: flex; gap: 15px; overflow-x: auto; padding: 10px 0; width: 100%;">
        <div style="background: #1b2010; border: 1px solid #384218; border-radius: 8px; padding: 12px 18px; min-width: 170px; display: flex; align-items: center; gap: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
            <span style="font-size: 22px; color: #a3e635;">♣</span>
            <div>
                <div style="font-size: 11px; color: #85994b; font-weight: bold; text-transform: uppercase;">1. SEVİYE</div>
                <div style="color: #ffcc00; font-size: 16px; font-weight: 800;">4.602,23 <span style="font-size: 11px; color: #ffeb99;">TRY</span></div>
            </div>
        </div>
        <div style="background: #1b2010; border: 1px solid #384218; border-radius: 8px; padding: 12px 18px; min-width: 170px; display: flex; align-items: center; gap: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
            <span style="font-size: 22px; color: #60a5fa;">♦</span>
            <div>
                <div style="font-size: 11px; color: #85994b; font-weight: bold; text-transform: uppercase;">2. SEVİYE</div>
                <div style="color: #ffcc00; font-size: 16px; font-weight: 800;">24.371,15 <span style="font-size: 11px; color: #ffeb99;">TRY</span></div>
            </div>
        </div>
        <div style="background: #1b2010; border: 1px solid #384218; border-radius: 8px; padding: 12px 18px; min-width: 170px; display: flex; align-items: center; gap: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
            <span style="font-size: 22px; color: #f87171;">♥</span>
            <div>
                <div style="font-size: 11px; color: #85994b; font-weight: bold; text-transform: uppercase;">3. SEVİYE</div>
                <div style="color: #ffcc00; font-size: 16px; font-weight: 800;">540.042,06 <span style="font-size: 11px; color: #ffeb99;">TRY</span></div>
            </div>
        </div>
        <div style="background: #1b2010; border: 1px solid #384218; border-radius: 8px; padding: 12px 18px; min-width: 170px; display: flex; align-items: center; gap: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
            <span style="font-size: 22px; color: #c084fc;">♠</span>
            <div>
                <div style="font-size: 11px; color: #85994b; font-weight: bold; text-transform: uppercase;">4. SEVİYE</div>
                <div style="color: #ffcc00; font-size: 16px; font-weight: 800;">1.212.745,31 <span style="font-size: 11px; color: #ffeb99;">TRY</span></div>
            </div>
        </div>
    </div>'''

# Spor Jackpot'u da temiz ve tam uyumlu yapalim
spor_jackpot_real = '''id="jackpot_container_94" class="jackpot_container">
    <div style="display: flex; gap: 15px; overflow-x: auto; padding: 10px 0; width: 100%;">
        <div style="background: #1b2010; border: 1px solid #384218; border-radius: 8px; padding: 12px 18px; min-width: 170px; display: flex; align-items: center; gap: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
            <span style="background: #eab308; color: #000; font-size: 11px; font-weight: 900; padding: 3px 6px; border-radius: 4px;">MEGA</span>
            <div>
                <div style="color: #ffffff; font-size: 16px; font-weight: 800;">₺ 3.842.190</div>
            </div>
        </div>
        <div style="background: #1b2010; border: 1px solid #384218; border-radius: 8px; padding: 12px 18px; min-width: 170px; display: flex; align-items: center; gap: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
            <span style="background: #ef4444; color: #fff; font-size: 11px; font-weight: 900; padding: 3px 6px; border-radius: 4px;">MAJOR</span>
            <div>
                <div style="color: #ffffff; font-size: 16px; font-weight: 800;">₺ 945.620</div>
            </div>
        </div>
        <div style="background: #1b2010; border: 1px solid #384218; border-radius: 8px; padding: 12px 18px; min-width: 170px; display: flex; align-items: center; gap: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
            <span style="background: #3b82f6; color: #fff; font-size: 11px; font-weight: 900; padding: 3px 6px; border-radius: 4px;">MINOR</span>
            <div>
                <div style="color: #ffffff; font-size: 16px; font-weight: 800;">₺ 182.430</div>
            </div>
        </div>
        <div style="background: #1b2010; border: 1px solid #384218; border-radius: 8px; padding: 12px 18px; min-width: 170px; display: flex; align-items: center; gap: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
            <span style="background: #10b981; color: #fff; font-size: 11px; font-weight: 900; padding: 3px 6px; border-radius: 4px;">MINI</span>
            <div>
                <div style="color: #ffffff; font-size: 16px; font-weight: 800;">₺ 45.110</div>
            </div>
        </div>
    </div>'''

# 1. Amusnet degisimi
p_start = html.find('id="jackpot_container_16"')
if p_start != -1:
    p_end = html.find('</div>\n                        </div>\n                        <div class="dynamic_container">', p_start)
    if p_end != -1:
        html = html[:p_start] + amusnet_real + html[p_end:]
        print('Amusnet jackpot alani tertemiz yeniden yazildi!')
    else:
        # alternatif kapanis arama
        p_spor = html.find('Spor Jackpot', p_start)
        p_div = html.rfind('</div>', p_start, p_spor)
        p_div2 = html.rfind('</div>', p_start, p_div)
        html = html[:p_start] + amusnet_real + '\n</div>\n</div>\n' + html[p_spor-200:]
        print('Amusnet alternatif ile guncellendi')

# 2. Spor Jackpot degisimi
s_start = html.find('id="jackpot_container_94"')
if s_start != -1:
    s_end = html.find('</div>\n                        </div>\n                        <div class="dynamic_container">', s_start)
    if s_end != -1:
        html = html[:s_start] + spor_jackpot_real + html[s_end:]
        print('Spor Jackpot alani tertemiz yeniden yazildi!')
    else:
        # div sonuna kadar
        s_end2 = html.find('<div class="dynamic_featured_content', s_start)
        s_prev_div = html.rfind('</div>', s_start, s_end2)
        html = html[:s_start] + spor_jackpot_real + html[s_prev_div:]
        print('Spor Jackpot alternatif ile guncellendi')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Bitti!')
