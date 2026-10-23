with open("1", "r", encoding = "utf-8") as file:
    lines = 0
    words = 0
    symbols = 0
    m = 0

    for l in file:
        l = l.replace("\n", "")
        lines += 1
        words += len(l.split())
        symbols += len(l)
        m = max(m, len(l))

print(lines)
print(words)
print(symbols)
print(m)