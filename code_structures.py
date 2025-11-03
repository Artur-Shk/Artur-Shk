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

'''Використайте функцію zip(), щоб створити словник movies, який об’єднує у пари списки: seasons = ['summer', 'autumn'] і 
months = [ 'july', 'november']. Виведіть вміст словника.'''

seasons = ['summer', 'autumn']
months = [ 'july', 'november']
movies = dict(zip(seasons, months))
print(movies)

'''Використайте відомі вам структури коду для виведення ключів і значень словника activity = {'business': 'manager', 
'it': 'software developer', 'science': 'scientist'} у вигляді, на зразок «категорія: професія».'''

activity = {'business': 'manager', 'it': 'software developer', 'science': 'scientist'}
for key, value in activity.items():
    print(f' Категорія - {key}, професія - {value}')

'''Використайте включення списку, щоб створити список, який містить парні числа у діапазоні range(12).'''

even_numbers = [num for num in range(12) if num % 2 == 0]
print(even_numbers)

'''Використайте включення словника, щоб створити словник squares з ключами у вигляді цілих чисел з діапазону range(1, 11). 
Значення словника формуються піднесенням ключів до другого степеня.'''
squares = {num: num ** 2 for num in range(1, 11)}
for key, value in squares.items():
    print(f"{key}² = {value}")

'''Використайте цикл for для виведення чисел від 1 до 15 включно, в один рядок і пропусками між ними.'''
for num in range(1, 16):
    print(num, end=' ')
print()

'''Створіть список чисел від 1 до 1 000 000. Скористайтеся функціями min() і max() та переконайтеся у тому, що список дійсно 
починається 1 і закінчується 1 000 000. Викличте функцію sum() і подивіться, наскільки швидко Python зможе підсумувати мільйон чисел.'''

numbers = range(1, 1000001)
print(f'Мінімальне число списку - {min(numbers)}!\nМаксимальне число списку - {max(numbers)}!\nСума усіх чисел списку = {sum(numbers)}!')

'''Cкористайтеся третім аргументом функції range() для створення списку непарних чисел від 1 до 25 і виведіть усі числа в 
окремих рядках у циклі for.'''

odd_numbers = range(1, 25, 2)
for num in odd_numbers:
    print(num, end=' ')
print()

'''Створіть список перших 10 кубів (тобто кубів усіх цілих чисел від 1 до 10) і виведіть значення усіх кубів у циклі for 
в один рядок з пропусками.'''
cubed_numbers =[num**3 for num in range(1, 11)]
for num in cubed_numbers:
    print(num, end=' ')

'''Cтворіть список чисел у діапазоні від 3 до 60 і виведіть усі числа списку у циклі while в окремих рядках.'''

num = 3
while num <= 60:
    print(num)
    num += 1

'''Визначте функцію trees, яка повертає список ['poplar', 'willow', 'lime']. Викличте функцію.'''
def trees():
    types_of_trees = ['poplar', 'willow', 'lime']
    return types_of_trees

result = trees()
print(result)