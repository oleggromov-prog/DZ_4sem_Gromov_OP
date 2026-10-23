from pathlib import Path

dirr = input()
ext = input()
dirr = dirr[9:]
ext = ext[12:]

p = Path(dirr)

if p.exists():
    for f in p.rglob("*" + ext):
        if f.is_file():
            print(f)
            print(f.stat().st_size)
else:
    print("Указанного каталога не найдено")