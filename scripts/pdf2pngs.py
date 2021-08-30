# encoding:utf8

import sys
import os
import fitz


if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python3 pdf2pngs.py <input.pdf> [<output_dir>]")
        exit()
    if len(sys.argv) >= 2:
        pdf_file_path = os.path.abspath(sys.argv[1])
        pdf_file_name = os.path.splitext(os.path.basename(pdf_file_path))[0]
        output_dir = os.path.dirname(pdf_file_path)
    if len(sys.argv) >= 3:
        output_dir = os.path.abspath(sys.argv[2])

    print("Processing: \"%s\"" % (pdf_file_path))
    print("  - output_dir: \"%s\"" % (output_dir))
    print("  - prefix: \"%s\"" % (pdf_file_name))

    doc = fitz.open(pdf_file_path)
    for pg in range(doc.pageCount):
        page = doc[pg]
        rotate = int(0)
        zoom_x = 2.0
        zoom_y = 2.0
        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pm = page.getPixmap(matrix=trans, alpha=False)
        output_path = output_dir + os.sep + ("%s_%d.png" % (pdf_file_name, pg))
        print("  - output: \"%s\"" % (output_path))
        pm.writePNG(output_path)

