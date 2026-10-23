import json

max_sum = 0
max_student = ""

with open("students.json", "r", encoding = "utf-8") as file:
    students = json.load(file)
    print(students)

for student in students:
    if student["score"] >= 60:
        student["passed"] = True
    else:
        student["passed"] = False

    if student["score"] > max_sum:
        max_sum = student["score"]
        max_student = student

with open("students_res.json", "w", encoding = "utf-8") as res_file:
    json.dump(students, res_file, indent = 4)