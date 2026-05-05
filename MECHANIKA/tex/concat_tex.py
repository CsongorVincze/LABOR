import os

tex_dir = os.path.dirname(os.path.abspath(__file__))

preamble = """\\documentclass{article}
\\usepackage{graphicx} % Required for inserting images
\\usepackage{caption} % Required for \\captionof
\\usepackage{amsmath}
\\usepackage{float}
\\usepackage{comment}
\\usepackage[T1]{fontenc}
\\usepackage[utf8]{inputenc}
\\usepackage{lmodern}
\\usepackage{microtype}
\\usepackage{xcolor}
\\usepackage{framed}
\\renewenvironment{leftbar}{%
  \\def\\FrameCommand{\\textcolor{orange}{\\vrule width 3pt} \\hspace{10pt}}%
  \\MakeFramed {\\advance\\hsize-\\width \\FrameRestore}}%
 {\\endMakeFramed}

\\title{Mechanikai mérés}
\\author{Kern Luca, Vincze Csongor}
\\date{2026 Április 22}

\\begin{document}

\\maketitle

"""

output_file = os.path.join(tex_dir, "Teljes_Jegyzo.tex")

with open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.write(preamble)
    
    for i in range(1, 11):
        filename = os.path.join(tex_dir, f"{i}_feladat.tex")
        if not os.path.exists(filename):
            continue
            
        with open(filename, 'r', encoding='utf-8') as infile:
            content = infile.read()
            
            # Kicsomagoljuk a lényegi részt
            if '\\maketitle' in content:
                body = content.split('\\maketitle')[1]
            elif '\\begin{document}' in content:
                body = content.split('\\begin{document}')[1]
            else:
                body = content
                
            if '\\end{document}' in body:
                body = body.split('\\end{document}')[0]
                
            outfile.write(body.strip() + "\n\n\\newpage\n\n")

    outfile.write("\\end{document}\n")
    
print(f"Kész! A fájlok sikeresen egyesítve lettek a {output_file} fájlba.")
