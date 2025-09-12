# Створи список з 5 чисел.
# Додай ще одне число в кінець.
# Видали другий елемент.
# Виведи список у зворотному порядку.

list_1 = [10, 20, 30, 40, 50]
list_1.append(60)
list_1.pop(1)
list_reverse = list_1[::-1]
print(list_1)
print(list_reverse)


# Є список імен: ["Анна", "Ігор", "Марія", "Олег"].
# Перевір, чи є в ньому "Ігор".
# Замініть "Марія" на "Маша".

name_list = ["Анна", "Ігор", "Марія", "Олег"]
for n in name_list:
    if n == "Ігор":
        print(n)

name_list = ["Анна", "Ігор", "Марія", "Олег"]
print("Ігор" in name_list)

name_list = ["Анна", "Ігор", "Марія", "Олег"]
name_list[2] = "Маша"
print(name_list)

name_list = ["Анна", "Ігор", "Марія", "Олег"]
if "Марія" in name_list:
    index = name_list.index("Марія")
    name_list[index] = "Маша"
    print(name_list)

# Є список чисел.
# Знайди середнє значення всіх чисел.
# Створи новий список тільки з тих чисел, які більші за середнє.

number_list = [10, 20, 30, 40, 50, 60, 140]
number_list_2 = []
arith_mean = int(sum(number_list) / len(number_list))
for n in number_list:
    if n > arith_mean:
        number_list_2.append(n)
print("Середнє значення:", arith_mean)
print("Числа більші за середнє:", number_list_2)

#варіант рішення через list comprehension
number_list_1 = [10, 20, 30, 40, 50, 60, 140]
arith_mean_1 = sum(number_list_1) / len(number_list_1)
number_list_2 = [n for n in number_list_1 if n > arith_mean_1] #це list comprehension — «спискове включення». У Python це дуже зручний спосіб створювати нові списки з уже наявних, відфільтровані або змінені.
print("Середнє значення:", arith_mean)
print("Числа більші за середнє:", number_list_2)

# Є список з повторюваними елементами.
# Виведи унікальні значення у вигляді нового списку.
# Для кожного елемента підрахуй, скільки разів він зустрічається.

names = ["Анна", "Ігор", "Анна", "Марія", "Ігор", "Олег", "Анна"]
unique_names = list(set(names))
for n in unique_names:
    print(f"{n}: {names.count(n)}")


# ПРАКТИКА list comprehension

# Створи список квадратів чисел від 1 до 10.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_of_numbers = [n**2 for n in numbers]
print(f'Список квадратів чисел від 1 до 10: {squares_of_numbers}')

#Створи список усіх парних чисел від 0 до 20.
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
even_numbers = [n for n in numbers_list if n % 2 == 0]
print(f'Список усіх парних чисел від 0 до 20: {even_numbers}')

#Створи новий список з довжинами цих слів.
words = ["apple", "banana", "kiwi", "watermelon"]
word_length = [len(n) for n in words]
print(word_length)

#Створи список, де всі імена будуть великими літерами.
names_1 = ["Анна", "Ігор", "Марія", "Олег"]
uppercase = [n.upper() for n in names_1]
print(uppercase)

#Створи новий список тільки з тих чисел, які діляться на 5.
numbers_list_2 = [5, 12, 17, 24, 31, 40, 55]
divided_numbers = [n for n in numbers_list_2 if n % 5 == 0]
print(divided_numbers)



