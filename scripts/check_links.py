from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
for p in root.glob('*.html'):
    text=p.read_text(encoding='utf-8')
    local=[]
    for href in re.findall(r'href="([^"]+)"', text):
        if href.startswith(('http://','https://','mailto:','#')): continue
        target=(p.parent/href.split('#')[0])
        if href.split('#')[0] and not target.exists(): local.append(href)
    print(p.name, 'missing local links:', local or 'none')
