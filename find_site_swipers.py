with open(r'.\site\index.html', 'r', encoding='utf-8', errors='replace') as f:
    c = f.read()

import re
matches = re.findall(r'id=["\'](js_billboard[^"\']+)["\']', c)
print("Billboard containers:", matches)

all_swipers = re.findall(r'<div[^>]*class="[^"]*swiper[^"]*"[^>]*id=["\']([^"\']+)["\']', c)
print("All swiper divs with IDs:", all_swipers)
