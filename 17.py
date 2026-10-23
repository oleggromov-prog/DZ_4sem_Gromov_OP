summ = 0
minn = float("inf")
maxx = 0
count = 0
sr = 0

with open("17", "r", encoding = "utf-8") as file:
    for line in file:
        num = int(line.strip())
        summ += num
        count += 1
        if num > maxx:
            maxx = num
        if num < minn:
            minn = num

if count == 0:
    print("Файл пуст")
else:
    sr = summ / count
    print(summ)
    print(minn)
    print(maxx)
    print(count)
    print(sr)