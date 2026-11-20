html_path = r'C:\Users\laure\.gemini\antigravity\scratch\GrandPashabetSite\site\index.html'

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Mobil Cerceve Stili (Tum siteyi telefon ekrani gibi ortalar ve sabitler)
mobile_frame_css = '''
<style>
/* Mobil Gorunum Kilidi */
html, body {
    background: #060904 !important;
    margin: 0 !important;
    padding: 0 !important;
}

#wrapper {
    max-width: 460px !important;
    margin: 0 auto !important;
    background: #11170d !important;
    min-height: 100vh !important;
    box-shadow: 0 0 35px rgba(0,0,0,0.85) !important;
    position: relative !important;
    overflow-x: hidden !important;
}

.header__wrap_block {
    max-width: 460px !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
}

.custom-billboard-slide {
    width: 290px !important;
    min-width: 290px !important;
    max-width: 290px !important;
    height: 290px !important;
}

.custom-billboard-slide img {
    width: 290px !important;
    height: 290px !important;
    object-fit: cover !important;
}
</style>
'''

if '</head>' in html:
    html = html.replace('</head>', mobile_frame_css + '\n</head>')
    print('Mobil cerceve CSS eklendi!')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Tamamlandi!')
