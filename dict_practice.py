# # Створи словник з інформацією про книгу (назва, автор, рік видання). Виведи всі ключі та значення без дужок.
# books = {"Назва": "1984", "Автор": "Джордж Орвелл", "Рік видання": 1949}
# for k, v in books.items():
#     print(f'{k}: {v}')
#
# # Є словник з англійськими словами та їх перекладом. Додай нове слово й переклад.
#
# dictionary = {
#     "apple": "яблуко",
#     "book": "книга",
#     "dog": "собака",
#     "house": "дім",
#     "car": "машина",
#     "sun": "сонце",
#     "water": "вода",
#     "friend": "друг",
#     "school": "школа",
#     "computer": "комп’ютер"
# }
# # dictionary.update({"cup": "кружка"})
# dictionary["cup"] = "кружка"
# print(dictionary)
#
#
# # Є словник товарів: {"яблуко": 25, "банан": 30, "апельсин": 40}. Виведи ціну для "банан".
# price = {"яблуко": 25, "банан": 30, "апельсин": 40}
# fruit = input("Введірть назву фрукта: ")
#
# # print(f'Ціна банану - {price["банан"]} грн.')
#
# # Перевір, чи є ключ "груша" у словнику з попереднього завдання.
# if fruit in price:
#     print(f'Ціна {fruit} - {price[fruit]} грн.')
# else:
#     print(f'Товару з назвою "{fruit}" не існує!')
#
# # Є словник студентів:
# # students = {"Ігор": 85, "Анна": 92, "Олег": 78, "Марія": 95}
# # Знайди середній бал усіх студентів.
#
# students = {"Ігор": 85, "Анна": 92, "Олег": 78, "Марія": 95}
# scores = students.values()
# print(scores)
# # Розрахунок середнього балу
# average_score = sum(scores) / len(scores)
#
# print("Середній бал:", average_score)
#
# # Є словник зарплат: salaries = {"Оксана": 1200, "Андрій": 1500, "Катерина": 1700}
# # Збільш зарплату кожному працівнику на 10%.
#
# salaries = {"Оксана": 1200, "Андрій": 1500, "Катерина": 1700}
#
# for name, salary in salaries.items():
#     new_salary = round(salary * 1.1, 2)  # підняли на 10%
#     print(f"З 01.10.2025 р. {name} отримуватиме {new_salary} євро.")
#
#
# # Є список кортежів: data = [("apple", 3), ("banana", 2), ("apple", 4), ("orange", 1)]
# # Перетвори його у словник, де ключ — назва фрукта, а значення — загальна кількість.
#
# data = [("apple", 3), ("banana", 2), ("apple", 4), ("orange", 1)]
# result = {}
# for fruit, count in data:
#     data = [("apple", 3), ("banana", 2), ("apple", 4), ("orange", 1)]
#     result = {}
#     for fruit, count in data:
#         result[fruit] = result.get(fruit, 0) + count
#
# print(result)

# Є словник: words = {"apple": 3, "banana": 5, "cherry": 9, "pear": 7}
# Знайди ключ із найбільшим значенням.

words = {"apple": 3, "banana": 5, "cherry": 9, "pear": 7}
max_key = max(words, key=words.get)

print("Ключ із найбільшим значенням: 2", max_key)