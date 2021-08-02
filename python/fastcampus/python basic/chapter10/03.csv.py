import csv

data = [
    ["이름", "반", "번호"],
    ["한세진", 1, 20],
    ["권보미", 2, 40],
    ["한재인", 3, 10]
]

file = open("student.csv", "w", encoding="utf-8-sig")
writer = csv.writer(file)

for d in data:
    writer.writerow(d)

file.close()
