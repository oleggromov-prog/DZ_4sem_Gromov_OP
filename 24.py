import re

c_id = []

products = [
    "PRD-12345",
    "PRD-00123",
    "USR-12345",
    "PRD-987",
    "PRD-ABCDE",
    "PRD-54321"
]

r_id = r"PRD-\d{5}"

for product in products:
    p = re.findall(r_id, product)
    if len(p) > 0:
        c_id.append(p[0])
print(c_id)