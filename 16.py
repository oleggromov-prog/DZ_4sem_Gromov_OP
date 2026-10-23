import re

c_info = 0
c_warning = 0
c_error = 0
r_info = r"\d+-\d+-\d+ \d+:\d+:\d+ INFO"
r_warning = r"\d+-\d+-\d+ \d+:\d+:\d+ WARNING"
r_error = r"\d+-\d+-\d+ \d+:\d+:\d+ ERROR"

with open("16", "r", encoding = "utf-8") as file:
    for line in file:
        if len(re.findall(r_info, line)) > 0:
            c_info += 1
        if len(re.findall(r_warning, line)) > 0:
            c_warning += 1
        if len(re.findall(r_error, line)) > 0:
            c_error += 1

print("INFO: " + str(c_info))
print("WARNIG: " + str(c_warning))
print("ERROR: " + str(c_error))