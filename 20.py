import re

r_date = r"\d{1,2}\.\d{1,2}\.\d{4}"

with open("20", "r", encoding="utf-8") as file:
    for line in file:
        date = re.findall(r_date, line)
        for d in date:
            print(d)