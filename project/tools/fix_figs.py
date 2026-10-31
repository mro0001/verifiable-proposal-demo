"""Point figure lines at named figure files and drop pandoc's size attributes. Python 3.9.

Usage: fix_figs.py IN.md OUT.md MAPPING
MAPPING is comma-separated media=path pairs, such as image1.png=figures/fig_system.png.
The visible caption is kept as written in the docx; the alt text is kept as alt.
"""
import re
import sys

src, dst, mapping = sys.argv[1], sys.argv[2], sys.argv[3]
pairs = dict(item.split("=", 1) for item in mapping.split(","))
out = []
fig = re.compile(r"^!\[(?P<cap>[^\]]*)\]\((?P<path>[^)]*)\)(?:\{(?P<attrs>[^}]*)\})?\s*$")
for line in open(src, encoding="utf8").read().split("\n"):
    m = fig.match(line)
    if m:
        name = m.group("path").rsplit("/", 1)[-1]
        if name in pairs:
            attrs = m.group("attrs") or ""
            alt = re.search(r'alt="([^"]*)"', attrs)
            keep = ['width="6.5in"']
            if alt:
                keep.insert(0, 'alt="%s"' % alt.group(1))
            line = "![%s](%s){%s}" % (m.group("cap"), pairs[name], " ".join(keep))
    out.append(line)
open(dst, "w", encoding="utf8").write("\n".join(out))
