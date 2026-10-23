nums = []
minn = 0
maxx = 0
sa = 0
check = 0

with open("2", "r", encoding = "utf-8") as file:
    for l in file:
        try:
            num = int(l.strip())
            nums.append(num)
        except ValueError:
            print("Текст в строке не является числом")
            raise SystemExit

if len(nums) == 0:
    print("В файле отсутствуют числа")
else:
    minn = min(nums)
    maxx = max(nums)
    sa = sum(nums) / len(nums)
    with open("result.txt", "w", encoding = "utf-8") as res_file:
        res_file.write(str(minn) + "\n")
        res_file.write(str(maxx) + "\n")
        res_file.write(str(sa))
