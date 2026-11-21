import os, shutil, glob

SITE = r'.'
BENIM = glob.glob(r'C:\benim-kopyam\Grand*11_files')[0]

# Map: source filename -> destination path
copies = {
    'styles.css':              os.path.join(SITE, 'plat', 'prd', 'CW', 'GGP', 'Content', 'mobile', 'styles.css'),
    'redesignMobile.css':      os.path.join(SITE, 'plat', 'prd', 'CW', 'GGP', 'Content', 'mobile', 'redesignMobile.css'),
    'dynamicBanners_v1.0.css': os.path.join(SITE, 'plat', 'prd', 'CW', 'GGP', 'Content', 'mobile', 'components', 'dynamicBanners_v1.0.css'),
    'navBar.css':              os.path.join(SITE, 'plat', 'prd', 'CW', 'GGP', 'Content', 'components', 'navBar.css'),
    '1093.css':                os.path.join(SITE, 'plat', 'prd', 'CW', 'GGP', 'Content', 'mobile', 'partners', '1093.css'),
    'customMob.css':           os.path.join(SITE, 'plat', 'prd', 'Img', 'Partners', '1093', 'CustomCSS', 'customMob.css'),
}

# Search in benim-kopyam for these files
for name, dst in copies.items():
    if os.path.exists(dst):
        print(f"Already exists: {name}")
        continue
    
    # Search in benim-kopyam files dir
    src = os.path.join(BENIM, name)
    if not os.path.exists(src):
        # Try .indir extension
        src = os.path.join(BENIM, name + '.indir')
    if not os.path.exists(src):
        # Search recursively in benim-kopyam
        found = None
        for root, dirs, files in os.walk(r'C:\benim-kopyam'):
            for f in files:
                if f == name or f == name + '.indir':
                    found = os.path.join(root, f)
                    break
            if found:
                break
        if found:
            src = found
    
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        print(f"Copied: {name} ({os.path.getsize(dst)} bytes)")
    else:
        print(f"NOT FOUND: {name}")

# Also search in site-klonu itself (maybe under a different path)
for root, dirs, files in os.walk(SITE):
    for f in files:
        if f in copies and not os.path.exists(copies[f]):
            src = os.path.join(root, f)
            dst = copies[f]
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            print(f"Found locally: {f} -> {dst}")

# Verify
print("\n=== Verification ===")
for name, dst in copies.items():
    exists = os.path.exists(dst)
    size = os.path.getsize(dst) if exists else 0
    print(f"  {'OK' if exists else 'FAIL':4} {size:>8} {name}")
