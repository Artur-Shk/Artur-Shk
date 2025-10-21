# from dataclasses import replace
#
# from pyexpat.errors import messages
#
from math import radians
seconds_in_minute = 60
seconds_per_hour = 60 * seconds_in_minute
seconds_per_day = 24 * seconds_per_hour
s = seconds_per_day / seconds_per_hour
d = seconds_per_day // seconds_per_hour

# user_name = input("Enter your name: ")
# print(user_name.upper(), user_name.lower(), user_name.title(), user_name.swapcase())
#
# """Збережіть будь-яке повідомлення у змінній і виведіть це повідомлення. Потім замініть значення змінної іншим повідомленням
#  і виведіть нове повідомлення. Програму збережіть у файлі, ім’я якої підпорядковується стандартним правилам Python по використанню
#   малих літер і символів підкреслення - наприклад, simple_messages.py."""
#
# message = "Рейки-рейки. Шпали-шпали"
# replace_message = message.replace(message, "Заміна")
# print(replace_message)
#
# # Конвертер відстаней: з метрів у різні одиниці
# # Константи (SI/ISO):
# # 1 inch = 0.0254 m
# # 1 foot = 0.3048 m
# # 1 yard = 0.9144 m
# # 1 mile (statute) = 1609.344 m
# # 1 nautical mile = 1852 m
# # 1 kilometer = 1000 m
# # 1 centimeter = 0.01 m
# # 1 millimeter = 0.001 m
'''Виконайте переведення одиниць вимірювання відстаней. Значення відстані вказано у метрах. У кожному новому рядку 
програма виводить значення відстані, представлене у: дюймах, футах, милях, ярдах тощо. 
Числові дані на екрані мають бути у відформатованому вигляді: два знаки після десяткової крапки.
Використайте функцію format(). Потрібні значення одиниць вимірювання знайдіть у мережі Інтернет.'''
# m = float(input("Введіть відстань у метрах: "))
#
# inch = m / 0.0254
# foot = m / 0.3048
# yard = m / 0.9144
# mile = m / 1609.344
# n_mile = m / 1852
# km = m / 1000
# cm = m / 0.01
# mm = m / 0.001
#
# print("Довжина у дюймах:        ", format(inch, ".2f"))
# print("Довжина у футах:         ", format(foot, ".2f"))
# print("Довжина у ярдах:         ", format(yard, ".2f"))
# print("Довжина у статутних милях:", format(mile, ".2f"))
# print("Довжина у морських милях: ", format(n_mile, ".2f"))
# print("Довжина у кілометрах:    ", format(km, ".2f"))
# print("Довжина у сантиметрах:   ", format(cm, ".2f"))
# print("Довжина у міліметрах:    ", format(mm, ".2f"))

'''Обчисліть тривалість якоїсь події. Припустимо, учнівські канікули тривали кілька днів. На екран треба вивести
 у відформатованому вигляді (вирівнювання за лівим краєм, ширина поля: 10 знаків) загальну тривалість цієї події 
 у годинах, хвилинах, секундах.'''
vacations = float(input("Введіть тривалість канікул у днях: "))
in_seconds = vacations * seconds_per_day
in_minutes = vacations * (24 * 60)
in_hours = vacations * 24

print("Канікули тривали:")
print("Години:  {0:<10.2f}".format(in_hours))
print("Хвилини: {0:<10.2f}".format(in_minutes))
print("Секунди: {0:<10.2f}".format(in_seconds))

'''Виконайте перетворення значення температури у градусах Цельсія (C) для інших температурних шкал: Фаренгейта (F) і
 Кельвіна (K). Програма повинна відображати еквівалентну температуру у градусах Фаренгейта (F = 32 + 9/5 * C). 
 Програма повинна відображати еквівалентну температуру у градусах Кельвіна (K = C + 273,15). Результати потрібно 
 вивести на екран у відформатованому вигляді: з використанням двох знаків після десяткової крапки, 
 мінімальною довжиною поля (15), вирівнюванням по центру. Зверніть увагу, у дійсних числах для розділення 
 дробової і цілої частин використовують крапку.'''

temperature_in_celsius = float(input("Введіть температуру у цельсіях: "))
temperature_in_fahrenheit = 32 + 9/5 * temperature_in_celsius
temperature_in_kelvin = temperature_in_celsius + 273.15
print("Температура у Фаренгейтах: {0:^15.2f}".format(temperature_in_fahrenheit))
print("Температура у Кельвінах: {0:^15.2f}".format(temperature_in_kelvin))

'''Виконайте розкладання чотирицифрового цілого числа і виведіть на екран суму цифр у числі. Наприклад, якщо обрали число 6259, 
то програма повинна вивести на екран повідомлення: 6 + 2 + 5 + 9 = 22. Використайте функцію format() для відображення результату
або f-рядки.'''
#рішення 1
user_number = input("Введіть ваше число:")
count = 0
for number in user_number:
    if number.isdigit():
        count += int(number)

print(f"Сума цифр числа {user_number}: {'+'.join(str(number) for number in user_number)} = {count}")

#Рішення 2
user_number = input("Введіть ваше число: ")
digits = [int(d) for d in user_number if d.isdigit()]
print(f"{' + '.join(str(d) for d in digits)} = {sum(digits)}")

x1 = 39.9075000
y1 = 116.3972300
x2 = 50.4546600
y2 = 30.5238000

x1_rad = radians(x1)
y1_rad = radians(y1)
x2_rad = radians(x2)
y2_rad = radians(y2)

