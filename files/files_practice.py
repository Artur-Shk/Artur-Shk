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
    ["Rembrandt Harmenszoon van Rijn", "Aristotle"],
    ["Leonardo da Vinci", "Self-portrait"]
]
with open("painters.csv", "w", newline='', encoding="utf-8") as p:
    csvrecord = csv.writer(p)
    csvrecord.writerows(rows)

'''Використайте модуль csv і його функцію DictReader(), щоб зчитати вміст файла painters.csv у змінну painters. Виведіть значення змінної на екран.'''
with open("painters.csv", "r", encoding="utf-8") as f:
    painters = list(csv.DictReader(f))
print(*painters, sep="\n")

'''Створіть CSV-файл imdb.csv з рейтингом фільмів за версією IMDb, використовуючи список словників:'''

imdb = [
    {
        'title': 'Lord of the Rings: Two towers',
        'year': 2002,
        'rating': 8.7},
    {
        'title': 'Matrix',
        'year': 1999,
        'rating': 8.7},
    {
        'title': 'Interstellar',
        'year': 2014,
        'rating': 8.5},
    {
        'title': 'Back to the Future',
        'year': 1985,
        'rating': 8.5},
    {
        'title': 'Logan: Wolverine',
        'year': 2017,
        'rating': 8.1}
]

with open("imdb.csv", "w", newline='', encoding="utf-8") as f:
    crecord = csv.DictWriter(f, ["title", "year", "rating"])
    crecord.writeheader()
    crecord.writerows(imdb)
