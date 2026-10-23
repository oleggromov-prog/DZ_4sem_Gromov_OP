import re

emails = []

with open("12", "r", encoding = "utf-8") as file:
    for st in file:
        email = re.findall(r"\w+@\w+\.\w+", st)
        if len(email) > 0:
            emails.append(email[0])

emails = set(emails)
for email in emails:
    print(email)