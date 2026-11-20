html_path = r'C:\Users\laure\.gemini\antigravity\scratch\GrandPashabetSite\site\index.html'

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Billboard gorselleri (7'den 28'e kadar tum mobil afisler)
banner_images = [
    'images/7_mobil_20_3__20251109232352256.webp',
    'images/8_mobil_20_15__20260726171644127.webp',
    'images/9_mobil_20251005182622174.webp',
    'images/10_mobil_20260620150347432.webp',
    'images/11_mobil_20_2__20250708164758874.webp',
    'images/12_primmobil_20260511180353818.webp',
    'images/13_mobil_20_15__20261103190149735.webp',
    'images/14_mobil_20_1__20251229153823185.webp',
    'images/15_mobil2_20_1__20251119184817128.webp',
    'images/16_mobil_20_16__20261103185904561.webp',
    'images/17_mobil_20_17__20261103190346549.webp',
    'images/18_mobil4_20250706172217094.webp',
    'images/19_mobil4_20261103015433801.webp',
    'images/20_mobil_20251113123023587.webp',
    'images/21_mobil_20_1__20250802200008794.webp',
    'images/22_mobil3_20261102194049623_20261108173444339.webp',
    'images/23_mobil_20_3__20251120131052943.webp',
    'images/24_mobil_20260129201710755.webp',
    'images/25_mobil6_20250706172356738.webp',
    'images/26_mobil5_20250704185452966.webp',
    'images/27_mobil9_20250706172321556.webp',
    'images/28_mobil5_20250706172244054.webp'
]

# Dokunmatik (Swipe) ve Mobilde Akici Kaydirilabilir Billboard Banner
billboard_slides_html = ''
for i, src in enumerate(banner_images):
    billboard_slides_html += f'''
        <div class="custom-billboard-slide" style="min-width: 82%; max-width: 82%; flex-shrink: 0; scroll-snap-align: center; border-radius: 16px; overflow: hidden; box-shadow: 0 8px 24px rgba(0,0,0,0.5);">
            <img src="{src}" style="width: 100%; height: auto; display: block; border-radius: 16px; aspect-ratio: 1/1; object-fit: cover;">
        </div>
    '''

dots_html = ''
for i in range(len(banner_images)):
    active_style = 'background: #f6c343; width: 16px;' if i == 0 else 'background: rgba(255,255,255,0.25); width: 6px;'
    dots_html += f'<span class="custom-dot" data-idx="{i}" style="{active_style} height: 6px; border-radius: 3px; display: inline-block; transition: all 0.3s ease; cursor: pointer;"></span>'

custom_billboard_markup = f'''
<div class="dynamic_container billboard_container" style="padding: 10px 0 16px 0; overflow: hidden; position: relative;">
    <!-- Kaydirilabilir Banner Seridi (Touch & Mouse Drag Destekli) -->
    <div id="custom_billboard_track" style="display: flex; gap: 12px; overflow-x: auto; scroll-snap-type: x mandatory; padding: 4px 16px 14px 16px; scrollbar-width: none; -webkit-overflow-scrolling: touch; cursor: grab;">
        {billboard_slides_html}
    </div>

    <!-- Pagination Noktalari -->
    <div id="custom_billboard_dots" style="display: flex; justify-content: center; align-items: center; gap: 6px; margin-top: 4px;">
        {dots_html}
    </div>
</div>
'''

# JavaScript Kaydirma ve Otomatik Akis Motoru
slider_script = '''
<script>
(function() {
    let track = document.getElementById('custom_billboard_track');
    let dots = document.querySelectorAll('.custom-dot');
    if (!track || !dots.length) return;

    let currentIndex = 0;
    let slides = track.querySelectorAll('.custom-billboard-slide');

    function updateDots(index) {
        dots.forEach((dot, idx) => {
            if (idx === index) {
                dot.style.background = '#f6c343';
                dot.style.width = '16px';
            } else {
                dot.style.background = 'rgba(255,255,255,0.25)';
                dot.style.width = '6px';
            }
        });
    }

    // Scroll takip edip aktif noktayi guncelle
    track.addEventListener('scroll', function() {
        let scrollLeft = track.scrollLeft;
        let slideWidth = slides[0].offsetWidth + 12;
        let idx = Math.round(scrollLeft / slideWidth);
        idx = Math.max(0, Math.min(slides.length - 1, idx));
        if (idx !== currentIndex) {
            currentIndex = idx;
            updateDots(currentIndex);
        }
    }, { passive: true });

    // Noktalara tiklayinca kaydir
    dots.forEach((dot, idx) => {
        dot.addEventListener('click', () => {
            let slideWidth = slides[0].offsetWidth + 12;
            track.scrollTo({ left: idx * slideWidth, behavior: 'smooth' });
        });
    });

    // Otomatik Yumusak Akis (4 saniyede bir sonrakine gec)
    let autoScrollInterval = setInterval(() => {
        currentIndex = (currentIndex + 1) % slides.length;
        let slideWidth = slides[0].offsetWidth + 12;
        track.scrollTo({ left: currentIndex * slideWidth, behavior: 'smooth' });
    }, 4000);

    // Kullanici dokundugunda otomatik akisi gecici olarak durdur
    track.addEventListener('touchstart', () => clearInterval(autoScrollInterval), { passive: true });
    track.addEventListener('mousedown', () => clearInterval(autoScrollInterval), { passive: true });
})();
</script>
'''

# index.html icindeki eski billboard containerini degistir
p_start = html.find('class="dynamic_container billboard_container"')
if p_start != -1:
    # Bu dynamic_container'in kapanisina kadar bul
    p_dyn_next = html.find('<div class="dynamic_container', p_start + 45)
    if p_dyn_next != -1:
        html = html[:p_start-5] + custom_billboard_markup + html[p_dyn_next:]
        print('Billboard basariyla dinamik kaydirilabilir afis panosuna donusturuldu!')

if '</body>' in html:
    html = html.replace('</body>', slider_script + '\n</body>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Bitti!')
