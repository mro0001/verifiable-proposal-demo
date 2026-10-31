"""Make the Word style file styles/reference.docx. Python 3.9, standard library only.

Usage: make_reference.py SOURCE.docx OUT.docx

SOURCE.docx is a copy of a Word file in the proposal's styles (the earlier
appendix builds used the proposal draft of October 23). The steps are those of
the appendix build script of October 27 (121_build_appendix.py), then the clean
step of the demo survey (clean_reference.py).

1. Drop the source's images, comments, and people parts.
2. Set code and table text to 10 point, and add the Report Text paragraph style
   (a left rule in the verification red) for the example report in A2.5.
3. Add a centered page number in the footer.
4. Empty the body, keeping only the last section's page setup, and empty the
   creator and last-modified-by fields, so the file holds no text of the source
   and no name.
"""
import re
import sys
import zipfile

FOOTER = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
          '<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
          'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
          '<w:p><w:pPr><w:jc w:val="center"/></w:pPr>'
          '<w:r><w:fldChar w:fldCharType="begin"/></w:r>'
          '<w:r><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>'
          '<w:r><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:t>1</w:t></w:r>'
          '<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p></w:ftr>')
REPORT_TEXT = (
    '<w:style w:type="paragraph" w:customStyle="1" w:styleId="ReportText"><w:name w:val="Report Text"/>'
    '<w:basedOn w:val="Normal"/><w:qFormat/><w:pPr><w:pBdr><w:left w:val="single" w:sz="18" w:space="8" '
    'w:color="8C2F39"/></w:pBdr><w:spacing w:before="30" w:after="50"/><w:ind w:left="300"/></w:pPr>'
    '<w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:sz w:val="19"/><w:szCs w:val="19"/>'
    '</w:rPr></w:style>')
DROP = re.compile(r"(comments|commentsExtended|commentsIds|commentsExtensible|people)\.xml$")


def styled(parts):
    """Steps 1 to 3 of the docstring, on a dict of part name to bytes."""
    rels = parts["word/_rels/document.xml.rels"].decode("utf8")
    types = parts["[Content_Types].xml"].decode("utf8")
    for match in list(re.finditer(r'<Relationship [^>]*Target="([^"]+)"[^>]*/>', rels)):
        target = match.group(1)
        if target.startswith("media/") or DROP.match(target):
            rels = rels.replace(match.group(0), "")
            parts.pop("word/" + target, None)
            types = re.sub(r'<Override PartName="/word/%s"[^>]*/>' % re.escape(target), "", types)
    for name in [n for n in parts if n.startswith("word/media/")]:
        del parts[name]

    styles = parts["word/styles.xml"].decode("utf8")
    styles = styles.replace('<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/><w:sz w:val="22"/>',
                            '<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/><w:sz w:val="20"/><w:szCs w:val="20"/>', 1)
    compact_old = '<w:pPr><w:spacing w:before="36" w:after="36"/></w:pPr></w:style>'
    compact_new = ('<w:pPr><w:spacing w:before="36" w:after="36"/></w:pPr>'
                   '<w:rPr><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr></w:style>')
    at = styles.find('w:styleId="Compact"')
    end = styles.find(compact_old, at)
    if at < 0 or end < 0:
        raise SystemExit("the source has no Compact style in the expected form")
    styles = styles[:end] + compact_new + styles[end + len(compact_old):]
    if 'w:styleId="ReportText"' not in styles:
        styles = styles.replace("</w:styles>", REPORT_TEXT + "</w:styles>", 1)
    parts["word/styles.xml"] = styles.encode("utf8")

    parts["word/footer1.xml"] = FOOTER.encode("utf8")
    if "footer1.xml" not in rels:
        rels = rels.replace("</Relationships>",
                            '<Relationship Id="rIdFtrPage" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
                            'relationships/footer" Target="footer1.xml"/></Relationships>')
    if "/word/footer1.xml" not in types:
        types = types.replace("</Types>", '<Override PartName="/word/footer1.xml" ContentType="application/'
                              'vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/></Types>')
    parts["word/_rels/document.xml.rels"] = rels.encode("utf8")
    parts["[Content_Types].xml"] = types.encode("utf8")

    doc = parts["word/document.xml"].decode("utf8")
    k = doc.rfind("<w:sectPr")
    e = doc.find(">", k)
    if "footerReference" not in doc[k:]:
        doc = doc[:e + 1] + '<w:footerReference w:type="default" r:id="rIdFtrPage"/>' + doc[e + 1:]
    parts["word/document.xml"] = doc.encode("utf8")
    return parts


def cleaned(parts):
    """Step 4 of the docstring."""
    doc = parts["word/document.xml"].decode("utf8")
    head = doc[: doc.index("<w:body>") + len("<w:body>")]
    sect = re.search(r"<w:sectPr[ >].*?</w:sectPr>", doc[doc.rindex("<w:sectPr"):], re.S).group(0)
    parts["word/document.xml"] = (head + "<w:p/>" + sect + "</w:body></w:document>").encode("utf8")
    core = parts["docProps/core.xml"].decode("utf8")
    core = re.sub(r"<dc:creator>.*?</dc:creator>", "<dc:creator></dc:creator>", core, flags=re.S)
    core = re.sub(r"<cp:lastModifiedBy>.*?</cp:lastModifiedBy>", "<cp:lastModifiedBy></cp:lastModifiedBy>", core, flags=re.S)
    parts["docProps/core.xml"] = core.encode("utf8")
    return parts


def main(src, dst):
    with zipfile.ZipFile(src) as z:
        names = sorted(z.namelist())
        parts = {name: z.read(name) for name in names}
    parts = cleaned(styled(parts))
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as z:
        for name in sorted(parts):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, parts[name])
    print("wrote", dst)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
