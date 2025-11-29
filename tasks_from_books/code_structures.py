from turtledemo.sorting_animate import randomize

from cffi.cffi_opcode import PRIM_INT16
import re
import secrets
import random



# '''Напишіть код, який виводить різні повідомлення, в залежності від значення, що зберігається у змінній weather_forecast:
# What a beautiful day!, якщо значення змінної дорівнює sun, Take an umbrella!, якщо значення змінної дорівнює rain і The sun’s
# just gone in! – у іншому випадку.'''
#
# forecast = input("Enter weather: ").strip().lower()
# if forecast == "sun":
#     print("What a beautiful day!")
# elif forecast == "rain":
#     print("Take an umbrella!")
# else:
#     print("The sun’s just gone in!")
#
# '''Створіть програму, яка виводить повідомлення про кількість очок, які отримав гравець у комп’ютерній грі. Створіть змінну з ім’ям
# points_color і надайте їй значення 'green', 'yellow' або 'red'. Якщо змінна points_color містить значення 'green', виведіть повідомлення
# про те, що гравець отримав 5 очок, якщо 'yellow' - 10 очок, якщо 'red', виведіть повідомлення про те, що гравець отримав 15 очок.'''
#
# points = {
#     "green": 5,
#     "yellow": 10,
#     "red": 15
# }
# points_color = input("Введіть колір: ").strip().lower()
# score = points.get(points_color)
# if score:
#     print(f"Гравець отримав {score} очок!")
# else:
#     print("Очки не нараховані!")
#
# '''Напишіть ланцюжок if-elif-else для визначення віку людини. Надайте значення змінній age, а потім виведіть повідомлення.
# Якщо значення age менше 2 - baby, якщо значення age більше або дорівнює 2, але менше 4 - kid, якщо значення age більше або дорівнює 4,
# але менше 13 - child, якщо значення age більше або дорівнює 13, але менше 20 - teenager. якщо значення age більше або дорівнює 20,
# але менше 65 - grown-up, якщо значення age більше або дорівнює 65 - senior.'''
#
# while True:
#     try:
#         age = int(input("Введіть вік: "))
#     except ValueError:
#         print("Введіть вік цифрою!")
#         continue
#
#     if age < 0:
#         print("Вік не може бути від’ємним!")
#         continue
#
#     if 0 <= age < 2:
#         print("baby")
#     elif 2 <= age < 4:
#         print("kid")
#     elif 4 <= age < 13:
#         print("child")
#     elif 13 <= age < 20:
#         print("teenager")
#     elif 20 <= age < 65:
#         print("grown-up")
#     else:
#         print("senior")
#     break
#
# '''Створіть список трьох своїх улюблених фруктів і назвіть його favorite_fruits. Напишіть перевірку на те, чи входить фрукт у список.
# Якщо фрукт входить у список, виводиться повідомлення, на зразок You really like peaches!, у протилежному випадку - повідомлення про
# відсутність фрукту у списку.'''
#
#
# favorite_fruits = ['apple', 'banana', 'orange']
# while True:
#     user_fruits = input('Введіть назву фрукту: ').strip().lower()
#     if not user_fruits:  # користувач натиснув Enter
#         print("Ви нічого не ввели!")
#         continue
#
#     if user_fruits in favorite_fruits:
#         print(f'You really like {user_fruits}!')
#     else:
#         print('Your fruit is not on the list')
#     break
#
# '''Використайте цикл for, щоб вивести на екран в окремих рядках значення списку [5, 4, 3, 2, 1, 0, 'GO!'].'''
# readout = [5, 4, 3, 2, 1, 0, 'GO!']
# for item in readout:
#     print(item)

# '''Використайте функцію zip(), щоб створити словник movies, який об’єднує у пари списки: seasons = ['summer', 'autumn'] і
# months = [ 'july', 'november']. Виведіть вміст словника.'''
# from my_string import user_country
#
# seasons = ['summer', 'autumn']
# months = [ 'july', 'november']
# movies = dict(zip(seasons, months))
# print(movies)
#
# '''Використайте відомі вам структури коду для виведення ключів і значень словника activity = {'business': 'manager',
# 'it': 'software developer', 'science': 'scientist'} у вигляді, на зразок «категорія: професія».'''
#
# activity = {'business': 'manager', 'it': 'software developer', 'science': 'scientist'}
# for key, value in activity.items():
#     print(f' Категорія - {key}, професія - {value}')
#
# '''Використайте включення списку, щоб створити список, який містить парні числа у діапазоні range(12).'''
#
# even_numbers = [num for num in range(12) if num % 2 == 0]
# print(even_numbers)
#
# '''Використайте включення словника, щоб створити словник squares з ключами у вигляді цілих чисел з діапазону range(1, 11).
# Значення словника формуються піднесенням ключів до другого степеня.'''
# squares = {num: num ** 2 for num in range(1, 11)}
# for key, value in squares.items():
#     print(f"{key}² = {value}")
#
# '''Використайте цикл for для виведення чисел від 1 до 15 включно, в один рядок і пропусками між ними.'''
# for num in range(1, 16):
#     print(num, end=' ')
# print()
#
# '''Створіть список чисел від 1 до 1 000 000. Скористайтеся функціями min() і max() та переконайтеся у тому, що список дійсно
# починається 1 і закінчується 1 000 000. Викличте функцію sum() і подивіться, наскільки швидко Python зможе підсумувати мільйон чисел.'''
#
# numbers = range(1, 1000001)
# print(f'Мінімальне число списку - {min(numbers)}!\nМаксимальне число списку - {max(numbers)}!\nСума усіх чисел списку = {sum(numbers)}!')
#
# '''Cкористайтеся третім аргументом функції range() для створення списку непарних чисел від 1 до 25 і виведіть усі числа в
# окремих рядках у циклі for.'''
#
# odd_numbers = range(1, 25, 2)
# for num in odd_numbers:
#     print(num, end=' ')
# print()
#
# '''Створіть список перших 10 кубів (тобто кубів усіх цілих чисел від 1 до 10) і виведіть значення усіх кубів у циклі for
# в один рядок з пропусками.'''
# cubed_numbers =[num**3 for num in range(1, 11)]
# for num in cubed_numbers:
#     print(num, end=' ')
#
# '''Cтворіть список чисел у діапазоні від 3 до 60 і виведіть усі числа списку у циклі while в окремих рядках.'''
#
# num = 3
# while num <= 60:
#     print(num)
#     num += 1
#
# '''Визначте функцію trees, яка повертає список ['poplar', 'willow', 'lime']. Викличте функцію.'''
# def trees():
#     types_of_trees = ['poplar', 'willow', 'lime']
#     return types_of_trees
#
# result = trees()
# print(result)
#
# '''Напишіть функцію favorite_book(), яка отримує один параметр title. Функція повинна виводити повідомлення, на зразок One of my
# favorite books is "The Lord of the Rings".. Викличте функцію і переконайтеся у тому, що назва книги правильно передається як аргумент
#  при виконанні функції.'''
# def favorite_book(title):
#     print(f'Одна з моїх улюблених книг -  {title}!')
#
# favorite_book("Кобзар")
#
# '''Напишіть функцію make_shirt(), яка отримує розмір футболки і текст, який повинен бути надрукований на ній. Функція повинна
# виводити повідомлення з розміром і текстом. Викличте функцію з використанням позиційних аргументів. Викличте функцію вдруге з
# використанням іменованих аргументів. Змініть функцію make_shirt(), щоб футболки за замовчуванням мали розмір XL, і на них виводився
# текст I love Python!. Створіть футболку з розміром XL і текстом за замовчуванням.'''
# def make_shirt(size, text):
#     print(f'Замовлення: футболка, розмір - {size}, текст принта - {text}')
#
# make_shirt("M", "I love Python!")
# make_shirt(text="I love Python!", size="S")
#
# def make_shirt_1(size = "XL", text = "I love Python!"):
#     print(f'Замовлення: футболка, розмір - {size}, текст принта - {text}')
#
# make_shirt_1()

# '''Напишіть функцію city_country(), яка отримує назву міста і країну.
# Функція повинна повертати рядок у форматі Kyiv, Ukraine. Викличте функцію як мінімум для трьох пар «місто-країна».'''
# def city_country(city, country):
#     return f"{city}, {country}"
#
# print(city_country("Kyiv", "Ukraine"))
# print(city_country("Tokyo", "Japan"))
# print(city_country("Paris", "France"))
#
# '''При введенні числових даних часто зустрічається типова проблема: користувач вводить текст замість чисел. При спробі перетворити
# дані в int генерується виняток TypeError. Напишіть функцію, яка приймає два числа, шукає їх суму і виводить результат. Перехопіть
# виняток TypeError, якщо будь-яке із вхідних значень не є числом, і виведіть зручне повідомлення про помилку. Протестуйте функцію:
# спочатку введіть два числа, а потім введіть текст замість одного з чисел.'''
#
# def summ():
#     try:
#         num_1 = int(input("Введіть перше число: "))
#         num_2 = int(input("Введіть друге число: "))
#         result = num_1 + num_2
#         print(f"Сума чисел: {result}")
#     except TypeError:
#         print("Помилка: введено не число! Спробуйте ще раз.")
#
# summ()
#
# def summ():
#     while True:
#         try:
#             num_1 = int(input("Введіть перше число: "))
#             num_2 = int(input("Введіть друге число: "))
#             result = num_1 + num_2
#         except ValueError:
#             print("Помилка: введено не число! Спробуйте ще раз.\n")
#             continue
#         else:
#             print(f"Сума чисел: {result}")
#             break
#
# summ()
#
# '''Виведіть вітальне повідомлення для кожного користувача після його входу на сайт. Cтворіть список з кількох імен користувачів,
# включаючи ім’я 'Admin'. Перебираючи елементи списку, виведіть повідомлення для кожного користувача. Для користувача з ім’ям 'Admin'
# виведіть особливе повідомлення - наприклад: Hello Admin, I hope you’re well.. У інших випадках виводиться універсальне привітання -
# наприклад: Hello Alex, thank you for logging in again.. Додайте команду if, яка перевірить, що список користувачів не порожній.
# Якщо список порожній, виведіть повідомлення: We need to find some users!. Видаліть зі списку всі імена користувачів і переконайтеся
# у тому, що програма виводить правильне повідомлення.'''

# users_names = ['Artur', 'Pavlo', 'Alex', 'Admin']
# if not users_names:
#     print('We need to find some users!')
# else:
#     name = input('What is your name? ').strip().title()
#
#     if name not in users_names:
#         print(f'User {name} not found in the list!')
#     elif name == 'Admin':
#         print('Hello Admin, I hope you’re well.')
#     else:
#         print(f'Hello {name}, thank you for logging in again.')

# '''Визначте назву геометричної фігури за введеною кількістю її сторін. Програма повинна підтримувати фігури від 3 до 6 сторін. Якщо введена кількість
# сторін поза межами цього діапазону, програма повинна відображати відповідне повідомлення.'''
#
# number_of_sides = {3: 'трикутник',
#                    4: 'чотирикутник',
#                    5: 'пʼятикутник',
#                    6: 'шестикутник'}
# while True:
#     try:
#         users_number = int(input("Введіть кількість сторін фігури: "))
#     except ValueError:
#         print("Помилка: введено не число! Спробуйте ще раз.\n")
#         continue
#     if users_number not in number_of_sides:
#         print(f'Фігура з такою кількістю сторін відсутня!')
#         continue
#     else:
#             print(f' Ваша фігура - {number_of_sides[users_number]}')
#             break

# '''Порядкові числівники у англійській мові закінчуються суфіксом th (окрім 1st, 2nd і 3rd). Cтворіть список чисел від 1 до 9.
# Використайте ланцюжок if-elif-else у циклі для виведення правильного закінчення числівника для кожного числа. Програма повинна виводити
# числівники 1st 2nd 3rd 4th 5th 6th 7th 8th 9th, кожен у новому рядку.'''
#
#
# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in digits:
#     if i == 1:
#         print(f'{i}st')
#     elif i == 2:
#         print(f'{i}nd')
#     elif i == 3:
#         print(f'{i}rd')
#     else:
#         print(f'{i}th')
#
# '''Зчитайте ціле число введене користувачем і виведіть повідомлення про те, чи число парне або непарне.'''
#
# while True:
#     try:
#         user_number = int(input("Введіть бажане число: "))
#     except ValueError:
#         print("Помилка: введено не число! Спробуйте ще раз.\n")
#         continue
#     if user_number % 2 == 0:
#         print(f'Число {user_number} - парне!')
#     else:
#         print(f'Число {user_number} - непарне!')
#     break
#
# '''Зчитайте назву місяця від користувача як рядок і виведіть кількість днів у вказаному місяці.
# Врахувати те, що «February» може мати 28 або 29 днів.'''
#
# month = input("Введіть назву місяця (англійською): ").strip().title()
#
# days_in_month = {
#     "January": 31,
#     "March": 31,
#     "May": 31,
#     "July": 31,
#     "August": 31,
#     "October": 31,
#     "December": 31,
#     "April": 30,
#     "June": 30,
#     "September": 30,
#     "November": 30
# }
#
# if month in days_in_month:
#     print(f"{days_in_month[month]} днів")
# elif month == "February":
#     leap_year = input("Чи є рік високосним? (yes/no): ").strip().lower()
#     if leap_year == "yes":
#         print("29 днів")
#     else:
#         print("28 днів")
# else:
#     print("Невідома назва місяця!")

# '''Потрібно визначити, чи є даний рік високосним. Нагадаємо, що високосними роками вважаються ті роки, порядковий номер яких або кратний 4, а
# ле при цьому не кратний 100, або кратний 400 (наприклад, 2000-й рік був високосним, а 2100-й буде невисокосним роком). Програма повинна коректно
# працювати на числах від 1900 до 3000 років. Виведіть Leap year. у разі, якщо рік є високосним і Ordinary year. у протилежному випадку.'''
#
#
# while True:
#     try:
#         user_year = int(input("Введіть рік: "))
#     except ValueError:
#         print("Введіть рік цілим числом")
#         continue
#     if not 1900 <= user_year <= 3000:
#         print("Введіть рік в діапазоні від 1900 до 3000 включно.")
#         continue
#     else:
#         if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
#             print(f'{user_year} - високосний рік.')
#         else:
#             print(f'{user_year} - невисокосний рік.')
#     break
#
# '''Зчитайте зі стандартного вводу цілі числа, по одному числу у рядку, і після першого введеного нуля виведіть суму отриманих на вхід чисел.'''
# int_nums = []
# while True:
#     try:
#         user_num = int(input("Введіть число для обрахунку суми, або 0 для виведення результату: "))
#     except ValueError:
#         print("Введіть саме ціле число!")
#         continue
#     if user_num != 0:
#         int_nums.append(user_num)
#         continue
#     else:
#         print(f'Сума введених вами чисел = {sum(int_nums)}')
#     break
#
# '''Виведіть імена видатних особистостей України, зображених на грошових знаках. Користувач вводить номінал банкноти . Програма виводить значення
# номіналу і ім’я особи, яка зображена на цій банкноті. Якщо користувач вводить неіснуюче значення номіналу, на екран виводиться відповідне повідомлення.'''
# uah_banknotes = {
#             1: "Володимир Великий",
#             2: "Ярослав Мудрий",
#             5: "Богдан Хмельницький",
#             10: "Іван Мазепа",
#             20: "Іван Франко",
#             50: "Михайло Грушевський",
#             100: "Тарас Шевченко",
#             200: "Леся Українка",
#             500: "Григорій Сковорода",
#             1000: "Володимир Вернадський"
#         }
# while True:
#     try:
#         denomination = int(input("Введіть номінал банкноти: "))
#         if denomination in uah_banknotes:
#             print(f'На банкноті номіналом в {denomination} ₴ зображений(а) {uah_banknotes[denomination]}.')
#         else:
#             print("Такий номінал не існує, перевірте введені дані!")
#     except ValueError:
#         print("Введіть саме ціле число")
#         continue
#     break
#
# '''Створіть програму, яка зчитує позицію шахової фігури від користувача і повідомляє про колір квадрату, де знаходиться фігура.
# Наприклад, якщо користувач вводить a і 1, то програма повинна повідомити, що квадрат має колір black, якщо d і 5 - програма повідомляє,
# що квадрат має колір white.'''
#
# letters = ("a", "b", "c", "d", "e", "f", "g", "h")
# numbers = (1, 2, 3, 4, 5, 6, 7, 8)
# while True:
#
#     user_letter = input("Введіть літеру клітинки: ").strip().lower()
#     if  user_letter not in letters:
#         print(f'На шахматній дошці присутні літери від a до h включно, введіть одну з них!')
#         continue
#     break
# while True:
#     try:
#         user_number = int(input("Введіть число клітинки: "))
#         if user_number not in numbers:
#             print(f'На шахматній дошці присутні цифри від 1 до 8 включно, введіть одну з них!')
#             continue
#     except ValueError:
#         print("Введіть саме цифру від 1 до 8 включно!")
#         continue
#     column = ord(user_letter) - ord('a') + 1
#     if (user_number + column) % 2 == 0:
#         print(f'Колір обраної вами клітинки чорний!')
#     else:
#         print(f'Колір обраної вами клітинки білий!')
#
#     break

# '''Чи є рядок «паліндромом»? Рядок є паліндромом, якщо він однаково читається зліва направо та справа наліво. Наприклад, слова Level, Noon, Anna є "
#  "паліндромами, незалежно від регістру літер. Рядки, які треба перевірити, вводяться користувачем. Введення даних можна перервати, якщо ввести слово "
#  "escape. Програма повинна вивести результат перевірки у вигляді повідомлення наприклад: is a palindrome або is not a palindrome.)'''

# pattern = re.compile(r'^[A-Za-zА-Яа-яІіЇїЄєҐґ]+$')
# while True:
#     user_word = input("Введіть слово яке хочете перевірити: ").strip().lower()
#     if user_word == "escape":
#         break
#
#     if not pattern.fullmatch(user_word):
#         print("Ви ввели заборонений символ, дозволено лише букви!")
#         continue
#
#     if user_word == user_word[::-1]:
#         print("Введене вами слово - паліндром")
#     else:
#         print("Нажаль ваше слово не є паліндромом!")
#         continue

# '''Створіть таблицю множення. Розмірність таблиці (кількість рядків і стовпців) вводиться з клавіатури.'''
#
# while True:
#     try:
#         rows = int(input("Введіть кількість рядків: "))
#         cols = int(input("Введіть кількість стовпців: "))
#         break
#     except ValueError:
#         print("Потрібно вводити лише числа!")
#         continue
#
# for i in range(1, rows + 1):
#     for j in range(1, cols + 1):
#         print(f"{i * j:5}", end="")
#     print()

# '''Як відомо, День програміста припадає на 256 день року, у невисокосний рік це 13 вересня, а у високосний - 12.
# Дізнайтеся число і номер місяця, що припадають на день, за номером n, який вводиться користувачем, у невисокосному 2017 році.'''
#
# months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# months = ["січня", "лютого", "березня", "квітня", "травня", "червня", "липня", "серпня", "вересня", "жовтня", "листопада", "грудня"]
# while True:
#
#     try:
#         user_day = int(input("Введіть номер дня: "))
#     except ValueError:
#         print("Введіть номер дня цифрами!")
#         continue
#
#     if not 1 <= user_day <= 365:
#         print("Введіть число в діапазоні від 1 до 365 включно!")
#         continue
#
#     month_index = 0
#     for days_in_month in months_days:
#         if user_day > days_in_month:
#             user_day -= days_in_month  # Відкидаємо дні пройденого місяця
#             month_index += 1  # Переходимо до наступного місяця
#         else:
#             break
#
#     print(f'Ваша дата: {user_day} {months[month_index]}')
#
#     break
#
# '''Конвертуйте десяткове число (з основою 10) у бінарне (двійкове, з основою 2). Користувач вводить десяткове число як ціле, а потім використовується
# алгоритм поділу (псевдокод), показаний нижче, щоб виконати перетворення. Коли алгоритм завершується, результат містить двійкове подання числа. Програма
# має вивести відповідне повідомлення, на зразок: 2018 in Decimal is 11111100010 in Binary. Модифікуйте програму таким чином, щоб вона виконувала
# зворотну операцію: перетворювала двійкове чиcло у десяткове.'''
#
# while True:
#     try:
#         decimal_number = int(input("Введіть десяткове число: "))
#     except ValueError:
#         print("Введіть ціле число!")
#         continue
#
#     original_decimal = decimal_number
#     binary_result = ""
#
#     if decimal_number == 0:
#         binary_result = "0"
#     else:
#         while decimal_number > 0:
#             remainder = decimal_number % 2
#             binary_result = str(remainder) + binary_result
#             decimal_number //= 2
#
#     print(f"{original_decimal} в десятковій системі це {binary_result} у двійковій")
#     break
#
#
# while True:
#     binary_number = input("Введіть двійкове число: ").strip()
#     if all(char in "01" for char in binary_number):
#         break
#     print("Дозволені лише цифри 0 і 1!")
#
# original_binary = binary_number
# decimal_result = 0
#
# for bit_char in binary_number:
#     decimal_result = decimal_result * 2 + int(bit_char)
#
# print(f"{original_binary} в бінарній системі це {decimal_result} в десятковій.")
#
# '''Реалізуйте шифр Цезаря. Один з перших відомих прикладів шифрування був використаний Юлієм Цезарем. Цезар надавав письмові вказівки своїм генералам, але він не бажав, зрозуміло, щоб про них
# знали вороги. У результаті він створив власне шифрування, що згодом стало відоме як шифр Цезаря. Ідея цього шифру проста (і, як наслідок, вона не забезпечує серйозного захисту). Кожна буква в
# оригінальному повідомленні зміщується на 3 позиції. В результаті A стає D, B стає E, C стає F, D стає G і т. д. Останні три букви у алфавіті повертаються до початку: X стає A, Y стає B, а Z стає
# C. Нелітерні символи не враховуються шифром. Користувач вводить з клавітури повідомлення та зсув, а потім програма відображає зашифроване повідомлення. Переконайтеся, що програма шифрує як
# великі та малі літери. Програма також повинна підтримувати значення негативних зсувів, щоб її можна було використовувати як для кодування повідомлень, так і для декодування повідомлень. У
# нагоді стануть такі функції: ord() (перетворює символ у номер позиції цього символу у таблиці ASCII ) і chr() (перетворює номер позиції символу у таблиці ASCII у відповідний символ).'''
#
# pattern = re.compile(r'^[A-Za-zА-Яа-яІіЇїЄєҐґ]$')  # Перевіряємо кожен символ, а не рядок
# # --- Шифрування ---
# while True:
#     message = input('Введіть ваше повідомлення: ').strip()
#     if message.strip() == "":
#         print("Повідомлення не може бути порожнім або складатися лише з пробілів!")
#         continue
#     try:
#         letter_shift = int(input("Введіть бажане число зсуву: "))
#     except ValueError:
#         print("Введіть саме ціле число!")
#         continue
#
#     result = ""
#
#     for char in message:
#         if pattern.fullmatch(char):
#             if 'A' <= char <= 'Z':
#                 encrypted_char = chr((ord(char) - ord('A') + letter_shift) % 26 + ord('A'))
#             elif 'a' <= char <= 'z':
#                 encrypted_char = chr((ord(char) - ord('a') + letter_shift) % 26 + ord('a'))
#             elif 'А' <= char <= 'Я':
#                 encrypted_char = chr((ord(char) - ord('А') + letter_shift) % 33 + ord('А'))
#             elif 'а' <= char <= 'я':
#                 encrypted_char = chr((ord(char) - ord('а') + letter_shift) % 33 + ord('а'))
#         else:
#             encrypted_char = char
#         result += encrypted_char
#
#     print("Зашифровано:", result)
#     break
#
#
# # --- Розшифрування ---
# while True:
#     message = input('Введіть отримане повідомлення: ').strip()
#     if message.strip() == "":
#         print("Повідомлення не може бути порожнім або складатися лише з пробілів!")
#         continue
#     try:
#         letter_shift = int(input("Введіть необхідне число зсуву: "))
#     except ValueError:
#         print("Введіть саме ціле число!")
#         continue
#
#     result = ""
#
#     for char in message:
#         if pattern.fullmatch(char):
#             if 'A' <= char <= 'Z':
#                 decrypted_char = chr((ord(char) - ord('A') - letter_shift) % 26 + ord('A'))
#             elif 'a' <= char <= 'z':
#                 decrypted_char = chr((ord(char) - ord('a') - letter_shift) % 26 + ord('a'))
#             elif 'А' <= char <= 'Я':
#                 decrypted_char = chr((ord(char) - ord('А') - letter_shift) % 33 + ord('А'))
#             elif 'а' <= char <= 'я':
#                 decrypted_char = chr((ord(char) - ord('а') - letter_shift) % 33 + ord('а'))
#         else:
#             decrypted_char = char
#
#         result += decrypted_char
#
#     print("Розшифровано:", result)
#     break

# '''У програмі визначте функцію, яка генерує випадковий пароль. Пароль має бути довільної довжини від 7 до 10 символів. Кожен символ паролю
# повинен бути випадково обраним з позицій 33 до 126 з таблиці кодів ASCII . Функція повертає випадково сформований пароль як єдиний її результат
# і він виводиться в основній програмі. Скористайтеся вказівками з попередньої задачі.'''
#
#
# def password():
#     length = secrets.choice(range(7, 11))
#     allowed_chars = [chr(i) for i in range(33, 127)]
#     password = ''.join(secrets.choice(allowed_chars) for _ in range(length))
#     return password
#
#
# if __name__ == '__main__':
#     pwd = password()
#     print("Згенерований пароль:", pwd)
#
# '''Напишіть програму, у якій комп’ютер генерує випадкове число, а користувач повинен вгадати число, вводячи його з клавіатури за вказану кількість
# спроб.'''
#
# random_number = random.randint(1, 10)
# counter = 5
# print("Спробуйте вгадати число від 1 до 10. У вас є 5 спроб!")
#
# while counter > 0:
#     try:
#         user_number = int(input("Введіть число: "))
#         if not 1 <= user_number <= 10:
#             print("Ваше число не відповідає заданому діапазону!")
#             continue
#     except ValueError:
#         print("Ви ввели заборонений символ, введіть саме ціле число!")
#         continue
#     counter -= 1
#     if user_number == random_number:
#         print(f"Вау!!! Ви вгадали, я дійсно загадав число {random_number}.")
#         break
#     else:
#         if counter > 0:
#             print(f"Нажаль, ви не вгадали. Залишилось {counter} спроб.")
#         else:
#             print(f"Ви програли. Я загадав число {random_number}.")
#
# Створіть програму за мотивами відомої гри «Камінь, Ножиці, Папір». Застосуйте функціональний підхід при написанні коду програми.

import random

options = ["Камінь", "Ножиці", "Папір"]

def get_user_choice():
    while True:
        user_choice = input('Введіть "Камінь", "Ножиці" чи "Папір": ').capitalize().strip()
        if user_choice  not in options:
            print("Ви ввели невідоме значення")
            continue
        return user_choice

def get_computer_choice():
    computer_choice = random.choice(options)
    return computer_choice

def get_winner(user, comp):
    if user == comp:
        return "Ми зіграли в нічию!"

    # Камінь
    if user == "Камінь":
        if comp == "Ножиці":
            return "Ви перемогли! Камінь б’є ножиці."
        else:
            return "Я переміг! Папір накриває камінь."

    # Ножиці
    if user == "Ножиці":
        if comp == "Папір":
            return "Ви перемогли! Ножиці ріжуть папір."
        else:
            return "Я переміг! Камінь ламає ножиці."

    # Папір
    if user == "Папір":
        if comp == "Камінь":
            return "Ви перемогли! Папір накриває камінь."
        else:
            return "Я переміг! Ножиці ріжуть папір."

def main():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"Ваш вибір: {user_choice}")
    print(f"Вибір комп’ютера: {computer_choice}")

    result = get_winner(user_choice, computer_choice)
    print(result)

main()

