with open(r'.\site\index.html', 'r', encoding='utf-8', errors='replace') as f:
    c = f.read()

import re
idx = c.find('js_billboard_banner_cont_870')
end = c.find('</div>\n    </div>', idx)
snippet = c[idx:idx+4000]
imgs = re.findall(r'src=["\']([^"\']+)["\']', snippet)
print("First 10 images in billboard 870:")
for im in imgs[:10]:
    print(" ", im)

# How many slides are there?
slides = re.findall(r'class="[^"]*swiper-slide[^"]*"', snippet)
print("Total slides:", len(slides))
