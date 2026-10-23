from pathlib import Path

files = 0
dirs = 0
sum_size = 0
py_files = []

p = Path("catalog")

for f in p.iterdir():
    if f.is_file():
        files += 1
        sum_size += f.stat().st_size
        if f.suffix == ".py":
            py_files.append(f.name)
    if f.is_dir():
        dirs += 1

print(files)
print(dirs)
print(py_files)
print(sum_size)