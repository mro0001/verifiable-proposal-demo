"""Cut the proposal's Figure 3 to what the Word file shows. Python 3.9 with Pillow.

Usage: cut_figure3.py SOURCE.docx OUT.png

Word shows Figure 3 with a crop (a:srcRect) that hides the top strip of the
screenshot. Pandoc ignores Word crops, so this script reads the crop of the one
cropped image in SOURCE.docx and writes the image cut in pixels to the part Word
shows. Rows are rounded so that no hidden row is kept. The PNG is written fresh,
with no text chunks.
"""
import io
import math
import re
import sys
import zipfile

from PIL import Image


def main(docx, out):
    with zipfile.ZipFile(docx) as z:
        doc = z.read("word/document.xml").decode("utf8")
        rels = z.read("word/_rels/document.xml.rels").decode("utf8")
        drawings = [d for d in re.findall(r"<w:drawing>.*?</w:drawing>", doc, re.S) if "<a:srcRect " in d]
        if len(drawings) != 1:
            raise SystemExit("expected one cropped image, found %d" % len(drawings))
        drawing = drawings[0]
        rid = re.search(r'r:embed="([^"]+)"', drawing).group(1)
        target = re.search(r'<Relationship [^>]*Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels)
        if target is None:
            target = re.search(r'<Relationship [^>]*Target="([^"]+)"[^>]*Id="%s"' % re.escape(rid), rels)
        image = Image.open(io.BytesIO(z.read("word/" + target.group(1))))
        image.load()
    crop = dict(re.findall(r'(\w)="(\d+)"', re.search(r"<a:srcRect ([^/]*)/>", drawing).group(1)))
    width, height = image.size
    left = int(math.ceil(width * int(crop.get("l", 0)) / 100000.0))
    top = int(math.ceil(height * int(crop.get("t", 0)) / 100000.0))
    right = width - int(math.ceil(width * int(crop.get("r", 0)) / 100000.0))
    bottom = height - int(math.ceil(height * int(crop.get("b", 0)) / 100000.0))
    cut = image.crop((left, top, right, bottom))
    cut.save(out, format="PNG")
    print("cut %dx%d to %dx%d (left %d, top %d, right %d, bottom %d)" % (
        width, height, cut.size[0], cut.size[1], left, top, width - right, height - bottom))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
