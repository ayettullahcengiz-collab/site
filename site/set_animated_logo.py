html_path = r'C:\Users\laure\.gemini\antigravity\scratch\GrandPashabetSite\site\index.html'

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Orijinal header icindeki bos LogoMobilePlatform linkine dogrudan hareketli gif gorseli verelim
old_str = '<a class="LogoMobilePlatform" href="https://grandpashabet9090.com/"></a>'

new_str = '''<a class="LogoMobilePlatform" href="/" style="display: flex; align-items: center; width: auto; height: 38px; text-decoration: none; background: none;">
    <img src="images/cdn/logoBigGif.gif" alt="GRANDPASHABET" style="height: 38px; width: auto; max-width: 190px; object-fit: contain; filter: drop-shadow(0 0 6px rgba(246,195,67,0.3)); display: block;">
</a>'''

if old_str in html:
    html = html.replace(old_str, new_str)
    print('Logo basariyla eklendi!')
else:
    pos = html.find('LogoMobilePlatform')
    if pos != -1:
        p_start = html.rfind('<a', 0, pos)
        p_end = html.find('</a>', pos) + 4
        html = html[:p_start] + new_str + html[p_end:]
        print('Logo alternatif yontemle eklendi!')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Tamamlandi!')
