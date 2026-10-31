"""Give each pipe table the column widths its Word file had. Python 3.9.

Usage: table_widths.py IN.md OUT.md SOURCE.docx

Pandoc reads a docx table into a pipe table with equal columns. This reads the
grid of every table in SOURCE.docx, in document order, and rewrites the
separator line of each pipe table in IN.md, in the same order, with one dash per
percent of the width, so pandoc prints the columns in the same proportions. It
stops when the two files hold a different number of tables or a table has a
different number of columns.
"""
import re
import sys
import zipfile

SEP = re.compile(r"^\|(\s*:?-+:?\s*\|)+\s*$")


def word_widths(docx):
    with zipfile.ZipFile(docx) as z:
        doc = z.read("word/document.xml").decode("utf8")
    widths = []
    for table in re.findall(r"<w:tbl>.*?</w:tbl>", doc, re.S):
        grid = [int(w) for w in re.findall(r'<w:gridCol w:w="(\d+)"', table)]
        total = float(sum(grid))
        widths.append([max(1, int(round(100 * w / total))) for w in grid])
    return widths


def main(src, dst, docx):
    widths = word_widths(docx)
    with open(src, encoding="utf8") as handle:
        lines = handle.read().split("\n")
    n = 0
    for i, line in enumerate(lines):
        if SEP.match(line):
            if n >= len(widths):
                raise SystemExit("the markdown has more tables than %s" % docx)
            cols = line.strip().count("|") - 1
            if cols != len(widths[n]):
                raise SystemExit("table %d has %d columns here and %d in Word" % (n + 1, cols, len(widths[n])))
            lines[i] = "|" + "|".join("-" * w for w in widths[n]) + "|"
            n += 1
    if n != len(widths):
        raise SystemExit("the markdown has %d tables and %s has %d" % (n, docx, len(widths)))
    with open(dst, "w", encoding="utf8") as handle:
        handle.write("\n".join(lines))
    print("set the widths of %d tables" % n)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
