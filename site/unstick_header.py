html_path = r'C:\Users\laure\.gemini\antigravity\scratch\GrandPashabetSite\site\index.html'

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Header'in sayfayla birlikte asagi kaymasini engelleyen, sayfayla beraber dogal sekilde yukarida kalmasini saglayan CSS
unstick_header_css = '''
<style>
/* Tepe Logo ve Butonlarinin sayfayla birlikte asagi kaymasini onle */
#header, .header__wrap_block, .header_both {
    position: static !important;
    top: auto !important;
    transform: none !important;
}

body {
    padding-top: 0 !important;
}

.cw_header_space {
    display: none !important;
}
</style>
'''

if '</head>' in html:
    html = html.replace('</head>', unstick_header_css + '\n</head>')
    print('Header sabitlik kurali eklendi!')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Tamamlandi!')
