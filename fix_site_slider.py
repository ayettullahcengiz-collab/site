import re, os, shutil

site_html_path = r'.\site\index.html'
with open(site_html_path, 'r', encoding='utf-8', errors='replace') as f:
    c = f.read()

# 1. Fix broken https:/plat/prd/ -> /plat/prd/
old_count = c.count('https:/plat/prd/')
c = c.replace('https:/plat/prd/', '/plat/prd/')
print(f"Fixed {old_count} broken 'https:/plat/prd/' -> '/plat/prd/'")

# Also fix http:/plat/prd/
old_count2 = c.count('http:/plat/prd/')
c = c.replace('http:/plat/prd/', '/plat/prd/')
print(f"Fixed {old_count2} broken 'http:/plat/prd/' -> '/plat/prd/'")

# 2. Check if swiper.js script tag exists
if 'swiper.js' not in c or '<script' not in c.split('swiper.js')[0][-200:]:
    # Add swiper.js and storySliderWeb.js before </body>
    swiper_scripts = """
<script src="/plat/prd/CW/GGP/Scripts/Utils/swiper.js"></script>
<script src="/plat/prd/CW/GGP/Scripts/Utils/storySliderWeb.js"></script>
<script>
// Initialize billboard swiper
(function() {
    function initBillboard() {
        var el = document.getElementById('js_billboard_banner_cont_870');
        if (!el || typeof Swiper === 'undefined') return;
        // Don't re-init if already running
        if (el.swiper) return;
        new Swiper(el, {
            slidesPerView: 'auto',
            loop: true,
            autoplay: { delay: 5000, disableOnInteraction: false },
            pagination: { el: el.querySelector('.swiper-pagination'), clickable: true, dynamicBullets: true },
            speed: 300,
            spaceBetween: 8
        });
    }
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initBillboard);
    } else {
        initBillboard();
    }
    window.addEventListener('load', function() {
        setTimeout(initBillboard, 200);
        setTimeout(initBillboard, 1000);
    });
})();
</script>
"""
    c = c.replace('</body>', swiper_scripts + '\n</body>')
    print("Added swiper.js, storySliderWeb.js and billboard init script")
else:
    print("swiper.js already present")

# 3. Check mobile CSS files exist locally
mobile_css_files = [
    'plat/prd/CW/GGP/Content/mobile/styles.css',
    'plat/prd/CW/GGP/Content/mobile/redesignMobile.css',
    'plat/prd/CW/GGP/Content/mobile/components/dynamicBanners_v1.0.css',
    'plat/prd/CW/GGP/Content/components/navBar.css',
    'plat/prd/CW/GGP/Content/mobile/partners/1093.css',
    'plat/prd/Img/Partners/1093/CustomCSS/customMob.css',
    'plat/prd/CW/GGP/Content/components/cwDynamicIcons.css',
]
base = r'.'
for css_file in mobile_css_files:
    full = os.path.join(base, css_file.replace('/', os.sep))
    if os.path.exists(full):
        print(f"  OK   {css_file}")
    else:
        print(f"  MISS {css_file}")

# 4. Strip ?v= query strings from local CSS/JS references
c = re.sub(r'(/plat/prd/[^"\'?\s]+)\?v=[^"\'>\s]+', r'\1', c)
print("Stripped ?v= query params from /plat/prd/ paths")

with open(site_html_path, 'w', encoding='utf-8') as f:
    f.write(c)

print("\nDone! site/index.html updated.")

# Also fix the big HTML file
big_path = r".\site\GrandPashabet Türkiye'nin En Büyük Casino Sitesi.html"
if os.path.exists(big_path):
    with open(big_path, 'r', encoding='utf-8', errors='replace') as f:
        bc = f.read()
    n1 = bc.count('https:/plat/prd/')
    bc = bc.replace('https:/plat/prd/', '/plat/prd/')
    bc = bc.replace('http:/plat/prd/', '/plat/prd/')
    bc = re.sub(r'(/plat/prd/[^"\'?\s]+)\?v=[^"\'>\s]+', r'\1', bc)
    with open(big_path, 'w', encoding='utf-8') as f:
        f.write(bc)
    print(f"Also fixed big HTML ({n1} broken paths)")
