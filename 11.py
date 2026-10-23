import re

ids = []
errors = []
error_ids = []

with open("logs.txt", "r", encoding = "utf-8") as file:
    for st in file:
        id = re.findall(r"User (\d+)", st)
        if len(id) > 0:
            ids.append(id)

        error = re.findall(r"ERROR.*", st)
        if len(error) > 0:
            errors.append(error)

        error_id = re.findall(r"ERROR User (\d+)", st)
        if len(error_id) > 0:
            error_ids.append(error_id)
print(ids)
print(errors)
print(error_ids)