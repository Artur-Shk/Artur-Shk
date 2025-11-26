import csv
'''Збережіть рядок 'Test variable to write to file' у змінну test1 і запишіть змінну test1 у файл з ім’ям tests.txt.
Відкрийте файл tests.txt і зчитайте його вміст у рядок test2. Порівняйте рядки test1 і test2?'''
test1 = "Test variable to write to file"
with open("tests.txt", "w", encoding="utf-8") as f:
    f.write(test1)
    f.write(test1)

with open("tests.txt", "r", encoding="utf-8") as f:
    test2 = f.readline().rstrip("\n")
if test1 == test2:
    print("C")

'''Скопіюйте наступні кілька рядків у файл painters.csv.
author, canvas
Vincent Willem van Gogh, "Vase with sunflowers"
Rembrandt Harmenszoon van Rijn, "Aristotle"
Leonardo da Vinci, "Self-portrait"'''

rows = [
    ["author", "canvas"],
    ["Vincent Willem van Gogh", "Vase with sunflowers"],
    ["Rembrandt Harmenszoon van Rijn" "Aristotle"],
    ["Leonardo da Vinci", "Self-portrait"]
]
with open("painters.csv", "w", newline='') as p:
    csvrecord = csv.writer()
    csvrecord.writerows()