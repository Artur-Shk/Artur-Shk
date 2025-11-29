# # Є два набори учнів:
# # Знайди тих, хто є в обох групах.
# # Знайди тих, хто є лише в одній групі.
#
# group1 = {"Аріна", "Анна", "Ігор", "Олег"}
# group2 = {"Марія", "Ігор", "Світлана", "Аріна"}
# both = group1 & group2          # спільні імена (& — перетин)
# only_group1 = group1 - group2   # тільки в першій групі (- — різниця)
# only_group2 = group2 - group1   # тільки в другій групі
# only_one = group1 ^ group2      # унікальні імена в одній із груп (^ — симетрична різниця)
#
# for name in sorted(both):
#     print((f"В обох групах є студент(и) з іменем: {name}"))
#
# for name in sorted(only_group1):
#     print(f"{name} є лише в group1")
#
# for name in sorted(only_group2):
#     print(f"{name} є лише в group2")
#
# for name in sorted(only_one):
#     print(f"Студент(ка) {name} є лише в одній із груп")

# # Є список чисел:
# numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6]
#
# # перетворюємо список у множину → залишаються лише унікальні числа
# unique_numbers = set(numbers)
#
# # виводимо унікальні числа
# print(unique_numbers)
#
# # рахуємо, скільки різних чисел у списку
# print(len(unique_numbers))
#
# # Напиши програму, яка читає список слів і виводить унікальні слова.
# words = [
#     "apple", "banana", "cherry", "dog", "cat",
#     "apple", "banana", "fish", "grape", "house",
#     "ice", "juice", "kite", "lion", "moon",
#     "cat", "dog", "nest", "orange", "pear",
#     "queen", "rain", "sun", "tree", "umbrella",
#     "violet", "water", "xray", "yellow", "zebra"
# ]
#
# # створюємо множину з усіх слів → дублікати прибираються
# unique_words = set(words)
#
# # виводимо унікальні слова, відсортовані за алфавітом
# print(f'Унікальні слова зі списку - це: {", ".join(sorted(unique_words))}')
#
# # Є два слова: "programming" та "gaming"
# # Знайди всі літери, які є в обох словах.
# # Знайди всі літери, які є лише в одному слові.
#
# word1 = "programming"
# word2 = "gaming"
#
# word1_letters = set(word1)  # множина літер першого слова
# word2_letters = set(word2)  # множина літер другого слова
#
# same_letters = word1_letters & word2_letters   # спільні літери (& — перетин)
# unique_letters = word1_letters ^ word2_letters # унікальні літери (^ — симетрична різниця)
#
# # ", ".join — об’єднує символи через кому
# # sorted — сортує їх за алфавітом
# print(f'В обох словах є букви: {", ".join(sorted(same_letters))}')
# print(f'Букви {", ".join(sorted(unique_letters))} є лише в одному зі слів')
#
# # Дні тижня
# # work_days = {"Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця"}
# # weekend = {"Субота", "Неділя"}
# # Об’єднай множини у all_days.
# # Перевір, чи "Середа" є робочим днем.
# # Перевір, чи "Неділя" є вихідним.
# def days_of_week():
#     day = input("Введіть день тижня: ").capitalize()
#     work_days = {"Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця"}
#     weekend = {"Субота", "Неділя"}
#
#     if day in work_days:
#         print(f'{day} - робочий день :-(')
#     elif day in weekend:
#         print(f'{day} - вихідний :-)')
#     else:
#         print("Такого дня тижня не існує!!!")
#
#     all_days_ordered = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
#
#     # тільки ті дні, які реально є в множинах (для "чистоти" перевірок)
#     all_days = [d for d in all_days_ordered if d in work_days.union(weekend)]
#
#     print("Всі дні тижня:", ", ".join(all_days))
#
#
# days_of_week()

# Є три гуртки:
#
# football = {"Аріна","Анна", "Ігор", "Олег"}
# chess = {"Ігор", "Марія", "Олег"}
# dance = {"Анна", "Світлана", "Аріна"}
#
# Знайди учнів, які ходять і на футбол, і на шахи.
# Знайди учнів, які ходять лише на один гурток.
# Знайди учнів, які ходять хоча б на два гуртки.

# Множини учнів, які відвідують різні гуртки
football = {"Аріна", "Анна", "Ігор", "Олег"}  # футбол
chess = {"Ігор", "Марія", "Олег"}             # шахи
dance = {"Анна", "Світлана", "Аріна"}         # танці

# Учні, які відвідують одночасно футбол і шахи
football_and_chess = football & chess  # & — перетин множин

# Учні, які відвідують лише один гурток
only_one = football ^ chess ^ dance  # ^ — симетрична різниця (ті, хто в одній множині, але не в двох одночасно)

# Учні, які відвідують хоча б два гуртки
at_least_two = (football & chess) | (football & dance) | (chess & dance)  # | — об’єднання множин, аналог union()

# Вивід результатів
print(f'{", ".join(football_and_chess)} ходять і на футбол, і на шахи.')
print(f'{", ".join(only_one)} ходять лише на один гурток.')
print("Учні, які ходять хоча б на два гуртки:", at_least_two)
