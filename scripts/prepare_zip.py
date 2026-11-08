import shutil
import sys
import zipfile
from pathlib import Path

zip_path = Path(sys.argv[1])
destination = Path("app/src/main/assets/site")
temporary = Path("build/extracted")

if not zip_path.is_file():
    raise SystemExit(f"ZIP não encontrado: {zip_path}")

if temporary.exists():
    shutil.rmtree(temporary)
if destination.exists():
    shutil.rmtree(destination)
temporary.mkdir(parents=True, exist_ok=True)
destination.mkdir(parents=True, exist_ok=True)

with zipfile.ZipFile(zip_path) as archive:
    for member in archive.infolist():
        target = (temporary / member.filename).resolve()
        if temporary.resolve() not in target.parents and target != temporary.resolve():
            raise SystemExit("O ZIP contém um caminho inválido.")
    archive.extractall(temporary)

html_files = list(temporary.rglob("index.html"))
if not html_files:
    html_files = [p for p in temporary.rglob("*.html") if p.is_file()]
if not html_files:
    raise SystemExit("Não encontrei index.html nem outro arquivo HTML no ZIP.")

site_root = html_files[0].parent
for item in site_root.iterdir():
    target = destination / item.name
    if item.is_dir():
        shutil.copytree(item, target)
    else:
        shutil.copy2(item, target)

if not (destination / "index.html").exists():
    shutil.copy2(html_files[0], destination / "index.html")

print(f"Projeto preparado: {destination / 'index.html'}")
