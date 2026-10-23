import re

r_adres = r"(?:http://|https://)(?:[A-Za-z0-9]+(?:\.[A-Za-z0-9]+)+)(?:(?:/[A-Za-z0-9]+)*(?:\.[A-Za-z0-9]+)*)*"

with open("22", "r", encoding="utf-8") as file:
    for line in file:
        adres = re.findall(r_adres, line)
        for a in adres:
            print(a)