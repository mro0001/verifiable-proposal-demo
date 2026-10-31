#!/bin/bash
# Convert the two Word files to the markdown that proposal.md and appendix.md started from.
# Python 3.9 and pandoc 3.9.0.2. Run from the project folder.
#
# Usage: tools/convert.sh PROPOSAL.docx APPENDIX.docx OUT_FOLDER
#
# The Word files are the proposal of October 27 (br_mo_oct27c) and the technical appendix of
# October 27 (10_27f, last saved October 28). They are not in this repository, since their
# properties carry the author's name and email.
#
# The proposal needs only pandoc and the figure lines. The appendix also needs docx_to_md.py
# (the earlier converter, keeping pandoc's escapes) and table_widths.py (its Word column
# widths). The output was then written into proposal.md and appendix.md, and four edits
# were made to appendix.md by hand, none of which changes the printed text:
#   - the literal placeholder in A2.3 written so the resolver does not read it
#   - two code spans that Word had split, joined (Tables A5 and A6)
#   - the at sign of [@nakamura2020] in the example report escaped
# Figure 3 of the proposal is cut to what the Word file shows with cut_figure3.py.
set -euo pipefail
proposal_docx="$1"
appendix_docx="$2"
out="$3"
here="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$out"

pandoc -f docx -t markdown --wrap=none --extract-media="$out/proposal_media" "$proposal_docx" -o "$out/proposal_raw.md"
python3 "$here/fix_figs.py" "$out/proposal_raw.md" "$out/proposal.md" \
  "image1.png=figures/proposal/fig2_flow.png,image2.png=figures/proposal/fig3_components.png,image3.png=figures/proposal/fig3_dashboard.png"

pandoc -f docx -t markdown-simple_tables-multiline_tables-grid_tables --wrap=none --extract-media="$out/appendix_media" "$appendix_docx" -o "$out/appendix_raw.md"
python3 "$here/docx_to_md.py" "$out/appendix_raw.md" "$out/appendix_1.md"
python3 "$here/table_widths.py" "$out/appendix_1.md" "$out/appendix_2.md" "$appendix_docx"
python3 "$here/fix_figs.py" "$out/appendix_2.md" "$out/appendix.md" \
  "image1.png=figures/appendix/fig_system.png,image2.png=figures/appendix/fig_connections.png,image3.png=figures/appendix/fig_pipeline.png,image4.png=figures/appendix/fig_audit.png,image5.png=figures/appendix/fig_runtime.png,image6.png=figures/appendix/fig_lifecycle.png,image7.png=figures/appendix/fig_procedures.png"

python3 "$here/cut_figure3.py" "$proposal_docx" "$out/fig3_dashboard.png"
echo "wrote $out/proposal.md, $out/appendix.md, and $out/fig3_dashboard.png"
