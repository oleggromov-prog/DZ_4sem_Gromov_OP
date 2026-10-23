import re

r_phone = r"(?:\+7|8) (?:\(\d{3}\)|\d{3}) \d{3}-\d{2}-\d{2}"

with open("19", "r", encoding="utf-8") as file:
    for line in file:
        phone = re.findall(r_phone, line)
        for p in phone:
            print(p)