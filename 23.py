import re

r_del = r"[^\s]+"

with open("23", "r", encoding="utf-8") as file:
    for line in file:
        st = ""
        words = re.findall(r_del, line)
        print(" ".join(words))