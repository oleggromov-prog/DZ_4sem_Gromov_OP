import csv

n = 0
sum_b = 0
sr = 0
max_b = 0
max_s = ""
group_nums = {}
group_sum = {}
group_sr = {}
with open("students.csv", "r", encoding = "utf-8") as file:
    reader = csv.DictReader(file)

    for st in reader:
        name = st["name"]
        group = st["group"]
        score = int(st["score"])

        n += 1
        sum_b += score

        if score > max_b:
            max_b = score
            max_s = name


        if group not in group_nums:
            group_nums[group] = 0
        group_nums[group] += 1

        if group not in group_sum:
            group_sum[group] = 0
        group_sum[group] += score

if n == 0:
    print("Нет данных")
else:
    sr = sum_b / n

    for group in group_sum:
        group_sr[group] = group_sum[group] / group_nums[group]

    print(sr)
    print(max_s)
    print(group_sr)
