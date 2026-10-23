import re

def is_valid_login(line):
    login = re.findall(r"^[A-Za-z]\w{3,15}$", line)
    if len(login) > 0:
        return True
    else:
        return False

with open("21", "r", encoding="utf-8") as file:
    for line in file:
        print(is_valid_login(line))