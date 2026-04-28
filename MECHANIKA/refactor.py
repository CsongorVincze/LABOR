import os
import glob
import re
import shutil

base_dir = r"c:\Users\Csongor\Documents\BME\LABOR\MECHANIKA"

folders = ['csv', 'tex', 'python', 'images']
for f in folders:
    os.makedirs(os.path.join(base_dir, f), exist_ok=True)

# Update Python files
py_files = glob.glob(os.path.join(base_dir, "*.py"))
for py in py_files:
    if "refactor.py" in py: continue
    with open(py, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Match os.path.join(script_dir, 'something.csv')
    content = re.sub(r"os\.path\.join\(script_dir,\s*'([^']+)\.csv'\)", r"os.path.join(script_dir, '..', 'csv', '\g<1>.csv')", content)
    # Match os.path.join(script_dir, 'something.png')
    content = re.sub(r"os\.path\.join\(script_dir,\s*'([^']+)\.png'\)", r"os.path.join(script_dir, '..', 'images', '\g<1>.png')", content)
    
    with open(py, "w", encoding="utf-8") as f:
        f.write(content)

# Update Tex files
tex_files = glob.glob(os.path.join(base_dir, "*.tex"))
for tex in tex_files:
    with open(tex, "r", encoding="utf-8") as f:
        content = f.read()
    
    def repl(m):
        opt = f"[{m.group(1)}]" if m.group(1) else ""
        return f"\\includegraphics{opt}{{../images/{m.group(2)}.png}}"

    content = re.sub(r"\\includegraphics(?:\[(.*?)\])?\{([^/]+)\.png\}", repl, content)
    
    with open(tex, "w", encoding="utf-8") as f:
        f.write(content)

# Move files
for file in os.listdir(base_dir):
    full_path = os.path.join(base_dir, file)
    if os.path.isdir(full_path): continue
    if file == "refactor.py": continue
    
    if file.endswith(".csv"):
        shutil.move(full_path, os.path.join(base_dir, "csv", file))
    elif file.endswith(".py"):
        shutil.move(full_path, os.path.join(base_dir, "python", file))
    elif file.endswith((".png", ".jpg", ".jpeg")):
        shutil.move(full_path, os.path.join(base_dir, "images", file))
    elif file.endswith((".tex", ".pdf", ".aux", ".log", ".fdb_latexmk", ".fls", ".synctex.gz")) or "synctex" in file:
        shutil.move(full_path, os.path.join(base_dir, "tex", file))

print("Refactoring complete.")
