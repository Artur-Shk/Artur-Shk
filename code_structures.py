'''
Напишіть код, який виводить різні повідомлення, в залежності від значення, що зберігається у змінній weather_forecast:
What a beautiful day!, якщо значення змінної дорівнює sun, Take an umbrella!, якщо значення змінної дорівнює rain і The sun’s
just gone in! – у іншому випадку.'''

forecast = input("Enter weather: ").strip().lower()
if forecast == "sun":
    print("What a beautiful day!")
elif forecast == "rain":
    print("Take an umbrella!")
else:
    print("The sun’s just gone in!")

'''Створіть програму, яка виводить повідомлення про кількість очок, які отримав гравець у комп’ютерній грі. Створіть змінну з ім’ям 
points_color і надайте їй значення 'green', 'yellow' або 'red'. Якщо змінна points_color містить значення 'green', виведіть повідомлення 
про те, що гравець отримав 5 очок, якщо 'yellow' - 10 очок, якщо 'red', виведіть повідомлення про те, що гравець отримав 15 очок.'''

points = {
    "green": 5,
    "yellow": 10,
    "red": 15
}
points_color = input("Введіть колір: ").strip().lower()
score = points.get(points_color)
if score:
    print(f"Гравець отримав {score} очок!")
else:
    print("Очки не нараховані!")

'''Напишіть ланцюжок if-elif-else для визначення віку людини. Надайте значення змінній age, а потім виведіть повідомлення. 
Якщо значення age менше 2 - baby, якщо значення age більше або дорівнює 2, але менше 4 - kid, якщо значення age більше або дорівнює 4, 
але менше 13 - child, якщо значення age більше або дорівнює 13, але менше 20 - teenager. якщо значення age більше або дорівнює 20, 
але менше 65 - grown-up, якщо значення age більше або дорівнює 65 - senior.'''

while True:
    try:
        age = int(input("Введіть вік: "))
    except ValueError:
        print("Введіть вік цифрою!")
        continue

    if age < 0:
        print("Вік не може бути від’ємним!")
        continue

    if 0 <= age < 2:
        print("baby")
    elif 2 <= age < 4:
        print("kid")
    elif 4 <= age < 13:
        print("child")
    elif 13 <= age < 20:
        print("teenager")
    elif 20 <= age < 65:
        print("grown-up")
    else:
        print("senior")
    break

'''Створіть список трьох своїх улюблених фруктів і назвіть його favorite_fruits. Напишіть перевірку на те, чи входить фрукт у список. 
Якщо фрукт входить у список, виводиться повідомлення, на зразок You really like peaches!, у протилежному випадку - повідомлення про 
відсутність фрукту у списку.'''


favorite_fruits = ['apple', 'banana', 'orange']
while True:
    user_fruits = input('Введіть назву фрукту: ').strip().lower()
    if not user_fruits:  # користувач натиснув Enter
        print("Ви нічого не ввели!")
        continue

    if user_fruits in favorite_fruits:
        print(f'You really like {user_fruits}!')
    else:
        print('Your fruit is not on the list')
    break

'''Використайте цикл for, щоб вивести на екран в окремих рядках значення списку [5, 4, 3, 2, 1, 0, 'GO!'].'''
readout = [5, 4, 3, 2, 1, 0, 'GO!']
for item in readout:
    print(item)

'''Використайте функцію zip(), щоб створити словник movies, який об’єднує у пари списки: seasons = ['summer', 'autumn'] і 
months = [ 'july', 'november']. Виведіть вміст словника.'''

