import re

def parse_number(value):
    try:
        return int(value)
    except ValueError:
        pass

    try:
        return float(value)
    except ValueError:
        raise ValueError("Неверное значение для перевода в число")

nums = ["42", "-17", "0", "3.14", "1e3", "abc", "12x", "--5"]
for num in nums:
    try:
        print(parse_number(num))
    except ValueError as exc:
        print(exc)