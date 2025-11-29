import csv
import re
pattern_chapter = re.compile(r'^[A-Za-zА-Яа-яІіЇїЄєҐґ]+(?: [A-Za-zА-Яа-яІіЇїЄєҐґ]+)*$')



# '''Збережіть рядок 'Test variable to write to file' у змінну test1 і запишіть змінну test1 у файл з ім’ям tests.txt.
# Відкрийте файл tests.txt і зчитайте його вміст у рядок test2. Порівняйте рядки test1 і test2?'''
# test1 = "Test variable to write to file"
# with open("tests.txt", "w", encoding="utf-8") as f:
#     f.write(test1)
#     f.write(test1)
#
# with open("tests.txt", "r", encoding="utf-8") as f:
#     test2 = f.readline().rstrip("\n")
# if test1 == test2:
#     print("C")
#
# '''Скопіюйте наступні кілька рядків у файл painters.csv.
# author, canvas
# Vincent Willem van Gogh, "Vase with sunflowers"
# Rembrandt Harmenszoon van Rijn, "Aristotle"
# Leonardo da Vinci, "Self-portrait"'''
#
# rows = [
#     ["author", "canvas"],
#     ["Vincent Willem van Gogh", "Vase with sunflowers"],
#     ["Rembrandt Harmenszoon van Rijn", "Aristotle"],
#     ["Leonardo da Vinci", "Self-portrait"]
# ]
# with open("painters.csv", "w", newline='', encoding="utf-8") as p:
#     csvrecord = csv.writer(p)
#     csvrecord.writerows(rows)
#
# '''Використайте модуль csv і його функцію DictReader(), щоб зчитати вміст файла painters.csv у змінну painters. Виведіть значення змінної на екран.'''
# with open("painters.csv", "r", encoding="utf-8") as f:
#     painters = list(csv.DictReader(f))
# print(*painters, sep="\n")
#
# '''Створіть CSV-файл imdb.csv з рейтингом фільмів за версією IMDb, використовуючи список словників:'''
#
# imdb = [
#     {
#         'title': 'Lord of the Rings: Two towers',
#         'year': 2002,
#         'rating': 8.7},
#     {
#         'title': 'Matrix',
#         'year': 1999,
#         'rating': 8.7},
#     {
#         'title': 'Interstellar',
#         'year': 2014,
#         'rating': 8.5},
#     {
#         'title': 'Back to the Future',
#         'year': 1985,
#         'rating': 8.5},
#     {
#         'title': 'Logan: Wolverine',
#         'year': 2017,
#         'rating': 8.1}
# ]
#
# with open("imdb.csv", "w", newline='', encoding="utf-8") as f:
#     crecord = csv.DictWriter(f, ["title", "year", "rating"])
#     crecord.writeheader()
#     crecord.writerows(imdb)
#
# '''Створіть новий файл numbers.txt у текстовому редакторі і запишіть у нього 10 чисел, кожне з нового рядка.
# Напишіть програму, яка зчитує ці числа з файла і обчислює їх суму, виводить цю суму на екран і, водночас, записує цю суму у інший файл
# з назвою sum_numbers.txt.'''
#
# sum_numbers = 0
#
# with open("numbers.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         line = line.strip()   # прибирає пробіли та переноси
#         if not line:          # пропускає порожні рядки
#             continue
#         try:
#             number = int(line) # пропуск буквених рядків
#         except ValueError:
#             continue
#
#         sum_numbers += number
#
# with open("sum_numbers.txt", "w", encoding="utf-8") as f:
#     f.write(f"Сума чисел файлу numbers = {sum_numbers}")
#
# '''Реалізуйте програму, яка зчитує ціле число, що вводиться з командного рядка, і записує у текстовий файл інформацію, щодо парності
# або непарності числа.'''
# while True:
#     try:
#         user_number = int(input("Введіть ціле число: "))
#         break
#     except ValueError:
#         print("Це не ціле число!")
#
# is_even = user_number % 2 == 0
# result = f'Число {user_number} парне!' if is_even else f'Число {user_number} не парне!'
# with open("parity.txt", "w", encoding="utf-8") as f:
#     f.write(result)
#
# '''Створіть новий файл у текстовому редакторі і напишіть кілька рядків тексту у ньому про можливості Python. Кожен рядок повинен починатися з фрази:
# In Python you can .... Збережіть файл з ім’ям learning_python.txt. Напишіть програму, яка зчитує файл і виводить текст з перебором рядків об’єкта
# файла і зі збереженням рядків у списку з подальшим виведенням списку поза блоком with.'''
#
# # варіант 1
# # text = []
# # with open("learning_python.txt", "r", encoding="utf-8") as f:
# #     for line in f:
# #         line = line.strip()  # прибирає пробіли та переноси
# #         if not line:  # пропускає порожні рядки
# #             continue
# #         text.append(line)
# # print(*text, sep="\n")
#
# # варіант 2
# with open("learning_python.txt", encoding="utf-8") as f:
#     text = [line.strip() for line in f if line.strip()]
# print(*text, sep="\n")
#
# '''Функція replace() може використовуватися для заміни будь-якого слова у рядку іншим словом. Прочитайте кожен рядок зі створеного у попередньому
# завданні файла learning_python.txt і замініть слово Python назвою іншої мови, наприклад C при виведенні на екран.'''
# content = []
#
# with open("learning_python.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         line = line.strip()
#         if not line:
#             continue
#         content.append(line.replace("Python", "C"))
#
# # Виведення результату
# print(*content, sep="\n")
#
# '''Створіть порожній файл guest_book.txt у текстовому редакторі. Напишіть цикл while, який запитує у користувачів імена. При введенні кожного імені
# виведіть на екран рядок з вітанням для користувача і запишіть рядок вітання у файл з ім’ям guest_book.txt. Простежте за тим, щоб кожне повідомлення
# розміщувалося в окремому рядку файла. Передбачте вихід з циклу.'''
#
# while True:
#     user_name = input('Введіть ваше імʼя, або "Завершити" для виходу з програми: ').strip().lower()
#
#     if not user_name:
#         print("Імʼя не може бути порожнім.")
#         continue
#
#     if user_name == "завершити":
#         break
#
#     if not pattern.fullmatch(user_name):
#         print("Ви ввели заборонений символ, дозволено лише букви!")
#         continue
#
#     normalized_name = user_name.title()
#
#     greeting = f'Вітаємо {normalized_name}! Приємного користування!!!'
#     with open("guest_book.txt", "a", encoding="utf-8") as f:
#         f.write(greeting + '\n')
#     print(greeting)

'''Зайдіть на сайт Project Gutenberg’s і знайдіть кілька книг для аналізу. Завантажте текстові файли цих творів або скопіюйте текст з браузера у 
текстовий файл на вашому комп’ютері. Напишіть програму, яка зчитує дані з файла і визначає кількість входжень слова 'the' в кожному тексті 
незалежно від регістру. Для підрахунку кількості входжень слова або виразу в рядок можна скористатися функцією count().'''

pattern_the = re.compile(r"\bthe\b", re.IGNORECASE)
count_control_word = 0

with open("Alice's_Adventures_in_Wonderland.txt", "r", encoding="utf-8") as f:
    for line in f:
        count_control_word += len(pattern_the.findall(line))

print(f'У вашому файлі слово "the" зустрічається {count_control_word} разів.')

'''Завантажте текстову версію однієї з книг із сайту Project Gutenberg’s . Замініть усі розриви рядків у тексті символом пропуску і запишіть 
відформатований текст у новий файл formatted_text.txt.'''

with open("Romeo_and_Juliet.txt", "r", encoding="utf-8") as f:
    text = f.read().replace("\n", " ")

# видаляє подвійні пробіли, потрійні пробіли
formatted = " ".join(text.split())

with open("formatted_text.txt", "w", encoding="utf-8") as f:
    f.write(formatted)

'''Завантажте текстову версію книги The Life and Adventures of Robinson Crusoe By Daniel Defoe  із сайту Project Gutenberg’s . Витягніть із тексту 
заголовки усіх розділів, які мають вигляд, на зразок: CHAPTER I—START IN LIFE. Запишіть знайдені назви у новий файл chapters.txt.'''



pattern_chapter = re.compile(r"^CHAPTER [IVXLCDM]+[—\.].*", re.IGNORECASE)
chapters = []

with open("The Life_and_Adventures_of_Robinson_Crusoe.txt", "r", encoding="utf-8") as f:
    for line in f:
        clean_line = line.strip()
        if pattern_chapter.match(clean_line):
            chapters.append(clean_line)

with open("chapters.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(chapters))

'''Визначте відсоток малих і великих літер у тексті, що зберігається у файлі. Скористайтеся, як зразком вхідного текстового файла, файл The Count of Monte Cristo  із сайту Project Gutenberg’s. 
Використайте функцію isalpha().'''
uppercase = 0
lowercase = 0

with open("monte_cristo.txt", "r", encoding="utf-8") as file:
    text = file.read()

for char in text:
    if char.isalpha():           # вибирає тільки літери
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1

total_letters = uppercase + lowercase

if total_letters > 0:
    upper_percent = (uppercase / total_letters) * 100
    lower_percent = (lowercase / total_letters) * 100

    print(f"У вашому тексті {upper_percent:.2f}% великих літер.")
    print(f"У вашому тексті {lower_percent:.2f}% малих літер.")
else:
    print("У тексті немає літер.")
