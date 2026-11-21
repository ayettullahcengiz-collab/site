with open(r'.\site\index.html', 'r', encoding='utf-8', errors='replace') as f:
    c = f.read()

import re
# Find billboard HTML in site/index.html
for m in re.finditer(r'<[^>]+class="[^"]*billboard[^"]*"', c, re.IGNORECASE):
    idx = m.start()
    print(c[idx:idx+400])
    print('-'*50)

# Check for swiper initialization
m2 = list(re.finditer(r'new\s+Swiper', c, re.IGNORECASE))
print(f"Total 'new Swiper' in site/index.html: {len(m2)}")
for m in m2:
    idx = m.start()
    print(c[idx:idx+300])
    print('-'*50)
