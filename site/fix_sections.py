import os

html_path = r'.\index.html'

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# 1. Opacity duzeltmeleri
html = html.replace('style="opacity: 0;"', 'style="opacity: 1;"')
html = html.replace('opacity: 0;', 'opacity: 1;')
html = html.replace('opacity: 0.000109658;', 'opacity: 1;')

# 2. Spor Jackpot icindeki skeleton yukleme kutularini gercek canli Jackpot sayaclarina donustur
spor_jackpot_search = 'id="jackpot_container_94" class="jackpot_container">'
real_spor_jackpot = '''id="jackpot_container_94" class="jackpot_container">
    <div style="display: flex; gap: 12px; overflow-x: auto; padding: 10px 0; width: 100%;">
        <div style="background: linear-gradient(135deg, #1b2010, #252d14); border: 1px solid #d4af37; border-radius: 8px; padding: 8px 16px; min-width: 140px; display: flex; align-items: center; justify-content: space-between;">
            <span style="color: #d4af37; font-weight: 800; font-size: 13px;">MEGA</span>
            <span style="color: #ffffff; font-size: 14px; font-weight: 700;">₺ 3.842.190</span>
        </div>
        <div style="background: linear-gradient(135deg, #1b2010, #252d14); border: 1px solid #e02424; border-radius: 8px; padding: 8px 16px; min-width: 140px; display: flex; align-items: center; justify-content: space-between;">
            <span style="color: #e02424; font-weight: 800; font-size: 13px;">MAJOR</span>
            <span style="color: #ffffff; font-size: 14px; font-weight: 700;">₺ 945.620</span>
        </div>
        <div style="background: linear-gradient(135deg, #1b2010, #252d14); border: 1px solid #3f83f8; border-radius: 8px; padding: 8px 16px; min-width: 140px; display: flex; align-items: center; justify-content: space-between;">
            <span style="color: #3f83f8; font-weight: 800; font-size: 13px;">MINOR</span>
            <span style="color: #ffffff; font-size: 14px; font-weight: 700;">₺ 182.430</span>
        </div>
        <div style="background: linear-gradient(135deg, #1b2010, #252d14); border: 1px solid #31c48d; border-radius: 8px; padding: 8px 16px; min-width: 140px; display: flex; align-items: center; justify-content: space-between;">
            <span style="color: #31c48d; font-weight: 800; font-size: 13px;">MINI</span>
            <span style="color: #ffffff; font-size: 14px; font-weight: 700;">₺ 45.110</span>
        </div>
    </div>'''

if spor_jackpot_search in html:
    # skeleton_container blogunu degistir
    parts = html.split(spor_jackpot_search)
    after = parts[1]
    skeleton_end = after.find('</div>\n                                </div>')
    if skeleton_end != -1:
        # replace the skeleton block
        html = parts[0] + real_spor_jackpot + after[skeleton_end+6:]
        print('Spor Jackpot skeletonu gercek sayaclarla degistirildi!')

# 3. CSS Overrides: Amusnet jackpotunun gizli kalmasini onle ve oyun kartlarindaki opacity'yi 1 yap
custom_css = """
<style>
.top_jackpots__container, .js_jacpkpots_cont {
    opacity: 1 !important;
    visibility: visible !important;
    display: flex !important;
}
.lca-card {
    opacity: 1 !important;
    visibility: visible !important;
}
.skeleton-jackpot__container, .skeleton-jackpot__body, .skeleton {
    display: none !important;
}
.top_jackpots__block {
    display: flex !important;
}
.component_jackpot_slider {
    display: inline-flex !important;
}
.top_jackpots__anim {
    display: flex !important;
    gap: 15px !important;
}
</style>
"""

if '</head>' in html:
    html = html.replace('</head>', custom_css + '\n</head>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Tamamlandi!')
