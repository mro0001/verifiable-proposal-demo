"""Compare the plain text of two Word files. Python 3.9, standard library only.

Usage: check_text.py BUILT.docx ORIGINAL.docx [--out FILE]

Reads the body of each docx (word/document.xml) paragraph by paragraph, table
cells included, in document order. A tab counts as a space and a line break
starts a new line. Alt text, headers, footers, and field codes are not read.
Then it evens out the text, so that a no-break space is a space, curly quotes
are straight, the ellipsis character is three dots, runs of spaces are one, and
empty lines are dropped. It prints how many lines each file has and every line
that differs, as a unified diff, and exits 0 when the two texts are the same and
1 when they differ. With --out it also writes the evened-out text of the built
file and the original beside FILE, as FILE.built.txt and FILE.original.txt, and
the diff as FILE.
"""
import difflib
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def paragraphs(docx):
    with zipfile.ZipFile(docx) as z:
        root = ET.fromstring(z.read("word/document.xml"))
    body = root.find(W + "body")
    lines = []
    for p in body.iter(W + "p"):
        parts = []
        for node in p.iter():
            if node.tag == W + "t" and node.text:
                parts.append(node.text)
            elif node.tag == W + "tab":
                parts.append(" ")
            elif node.tag in (W + "br", W + "cr"):
                parts.append("\n")
        lines.extend("".join(parts).split("\n"))
    return lines


def even(lines):
    out = []
    for line in lines:
        line = line.replace(" ", " ").replace("’", "'").replace("‘", "'")
        line = line.replace("“", '"').replace("”", '"').replace("…", "...")
        line = re.sub(r"\s+", " ", line).strip()
        if line:
            out.append(line)
    return out


def main(argv):
    out = None
    if "--out" in argv:
        at = argv.index("--out")
        out = argv[at + 1]
        argv = argv[:at] + argv[at + 2:]
    built, original = argv[0], argv[1]
    a, b = even(paragraphs(built)), even(paragraphs(original))
    diff = list(difflib.unified_diff(b, a, fromfile=original, tofile=built, lineterm="", n=1))
    print("%s: %d lines" % (built, len(a)))
    print("%s: %d lines" % (original, len(b)))
    changed = [line for line in diff if line[:1] in "+-" and not line.startswith(("+++", "---"))]
    if diff:
        print("%d lines differ" % len(changed))
        print("\n".join(diff))
    else:
        print("same text, line for line")
    if out:
        with open(out + ".built.txt", "w", encoding="utf8") as handle:
            handle.write("\n".join(a) + "\n")
        with open(out + ".original.txt", "w", encoding="utf8") as handle:
            handle.write("\n".join(b) + "\n")
        with open(out, "w", encoding="utf8") as handle:
            handle.write("\n".join(diff) + "\n" if diff else "")
    return 1 if diff else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
