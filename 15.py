from io import StringIO

def count_lines(stream):
    count = 0
    for st in stream:
        count += 1
    return count

file = StringIO()
file.write("Hello\nword")
file.seek(0)
print(count_lines(file))

with open("1", "r", encoding = "utf-8") as  file:
    print(count_lines(file))