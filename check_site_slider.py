with open(r'.\site\index.html', 'r', encoding='utf-8', errors='replace') as f:
    c = f.read()

import re
print("--- SWIPER references in site/index.html ---")
matches = set(re.findall(r'[^\s"\'<>]*swiper[^\s"\'<>]*', c, re.IGNORECASE))
for m in sorted(matches):
    print(" ", m)

print("\n--- SCRIPT tags in site/index.html ---")
scripts = re.findall(r'<script[^>]*src=["\']([^"\']+)["\']', c, re.IGNORECASE)
for s in scripts:
    print(" ", s)

print("\n--- CSS links in site/index.html ---")
csss = re.findall(r'<link[^>]*href=["\']([^"\']+\.css[^"\']*)["\']', c, re.IGNORECASE)
for cs in csss:
    print(" ", cs)

print("\n--- Billboard / Slider HTML container ---")
for m in re.finditer(r'(billboard|swiper-container|swiper-wrapper|slider)', c, re.IGNORECASE):
    idx = m.start()
    print(c[max(0, idx-40):min(len(c), idx+100)].replace('\n', ' '))
    print('-'*40)
    break
