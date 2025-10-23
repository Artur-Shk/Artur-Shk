'''Створи список з 5 чисел.
Додай ще одне число в кінець.
Видали другий елемент.
Виведи список у зворотному порядку.'''


list_1 = [10, 20, 30, 40, 50]
list_1.append(60)
list_1.pop(1)
list_reverse = list_1[::-1]
print(list_1)
print(list_reverse)


'''Є список імен: ["Анна", "Ігор", "Марія", "Олег"].
Перевір, чи є в ньому "Ігор".
Замініть "Марія" на "Маша".'''

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

'''Є список чисел.
Знайди середнє значення всіх чисел.
Створи новий список тільки з тих чисел, які більші за середнє.'''

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

'''Є список з повторюваними елементами.
Виведи унікальні значення у вигляді нового списку.
Для кожного елемента підрахуй, скільки разів він зустрічається.'''

names = ["Анна", "Ігор", "Анна", "Марія", "Ігор", "Олег", "Анна"]
unique_names = list(set(names))
for n in unique_names:
    print(f"{n}: {names.count(n)}")


# ПРАКТИКА list comprehension

# Створи список квадратів чисел від 1 до 10.
squares_of_numbers = [n**2 for n in range(1,11)]
print(f'Список квадратів чисел від 1 до 10: {squares_of_numbers}')

#Створи список усіх парних чисел від 0 до 20.
# numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# even_numbers = [n for n in numbers_list if n % 2 == 0]
even_numbers = [n for n in range(0, 21, 2)]
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

'''Створи порожній список з назвою empty_list.'''
empty_list = []
'''Створи список днів тижня з назвою weekdays і виведи другий елемент списку.'''
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(weekdays[1])
'''Створи список animals з 5 назвами тварин і виведи довжину списку.'''
animals = ['dog', 'cat', 'rabbit', 'cat', 'rabbit']
print (len(animals))
'''Створи список names з кількома іменами, де деякі повторюються.
Виведи, скільки разів кожне ім’я зустрічається у списку за допомогою count().'''
names = ['Олена', 'Іван', 'Олена', 'Петро', 'Марія', 'Іван', 'Катерина', 'Олег']
print(names.count('Іван'))

'''Створи список numbers 
Створи копії цього списку трьома способами.
Зміни перший елемент у numbers і перевір, чи змінились копії.'''
numbers = [1, 2, 3, 4, 5]
numbers_1 = numbers.copy()
numbers_2 = list(numbers)
numbers_3 = numbers[:]
numbers[0] = "Один"
print('.'.join(map(str, numbers)))
print('.'.join(map(str, numbers_1)))
print('.'.join(map(str, numbers_2)))
print('.'.join(map(str, numbers_3)))

'''Створи список planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter'].
Заміни 'Venus' на 'Neptune' і виведи оновлений список.'''
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter']
planets[1] = "Neptune"
print(planets)

'''Створи список cars 
Виведи перший, третій і останній елемент.
Спробуй звернутись до неіснуючого індекса (щоб побачити помилку).'''
cars = ['BMW', 'Audi', 'Toyota', 'Mazda', 'Ford']
cars_1 = []
cars_1.extend([cars[0], cars[2], cars[4]])
try:
    print(cars[5])
except IndexError:
    print ("Такий елемент відсутній")
print(', '.join(cars_1))

'''Створи три списки:
fruits = ['apple', 'banana']
colors = ['red', 'yellow']
prices = [10, 15]
Створи список all_info = [fruits, colors, prices]
Виведи елемент 'yellow', використовуючи подвійний індекс.'''

fruits = ['apple', 'banana']
colors = ['red', 'yellow']
prices = [10, 15]
all_info = [fruits, colors, prices]
print(all_info[1][1])

'''Створи список numbers = [10, 20, 30, 40, 50, 60].
Отримай новий список із перших трьох елементів.
Отримай кожен другий елемент.
Отримай список у зворотному порядку.'''
num = [10, 20, 30, 40, 50, 60]
num_1 = num[0:3]
print(num_1)
print(num[1::2])
print(num[::-1])

'''Створи список cities = ['Kyiv', 'London', 'Rome', 'Paris'].
→ Використай reverse() для зміни порядку елементів.'''
cities = ['Kyiv', 'London', 'Rome', 'Paris']
cities.reverse()
print(cities)

'''Створи список planets = ['Mercury', 'Earth'].
→ Додай 'Mars' у кінець за допомогою append().
→ Додай 'Venus' на початок за допомогою insert().
→ Додай 'Jupiter' після 'Earth' (у позицію 2).'''
planets = ['Mercury', 'Earth']
planets.append('Mars') # додаємо 'Mars' у кінець
planets.insert(0,'Venus') # додаємо 'Venus' на початок
planets.insert(3,'Jupiter') # додаємо 'Jupiter' після 'Earth'
print(planets)
'''Створи два списки:
planets = ['Earth', 'Mars']
satellites = ['Moon', 'Phobos']
Об’єднай їх спочатку через extend(), потім через +=.
А потім спробуй через append() і подивись різницю.'''

planets = ['Earth', 'Mars']
satellites = ['Moon', 'Phobos']
planets.extend(satellites) #об'єднує списки
planets += satellites #об'єднує списки
planets += satellites
planets.append(satellites) #додає список у список, як окремий елемент
print(planets)

'''Створи список planets = ['Mercury', 'Jupiter', 'Earth', 'Mars', 'Venus'].
→ Видали 'Venus' за допомогою del.
→ Видали 'Earth' за допомогою remove().
→ Видали останній елемент через pop() і збережи його у змінну last_planet.'''

planets = ['Mercury', 'Jupiter', 'Earth', 'Mars', 'Venus']
del planets[4]
planets.remove('Earth')
last_planet = planets.pop()
print(last_planet)
print(planets)

'''Створи список numbers = [10, 20, 30, 40, 50].
Використай pop(2) і виведи, який елемент видалено.'''
numbers = [10, 20, 30, 40, 50]
print(numbers.pop(2))

'''Створи список countries = ['Ukraine', 'Poland', 'Germany', 'France'].
Перевір, чи є 'Italy' у списку.
Перевір, чи 'Ukraine' відсутня у списку.'''

countries = ['Ukraine', 'Poland', 'Germany', 'France']
print('Italy' in countries)
print('Ukraine' not in countries)

'''Створи список planets = ['Mercury', 'Venus', 'Earth', 'Mars'].
Знайди індекс планети 'Earth' за допомогою index()'''
planets = ['Mercury', 'Venus', 'Earth', 'Mars']
print(planets.index('Earth'))
'''Створи список clothes = ['shirt', 'hat', 'jeans', 'trainers'].
→ Відсортуй копію списку через sorted(), а оригінал залиш без змін.
→ Потім відсортуй сам оригінал за допомогою sort().'''
clothes = ['shirt', 'hat', 'jeans', 'trainers']
sorted_clothes = sorted(clothes)
print(sorted_clothes)  # копія
print(clothes)         # оригінал не змінився
clothes.sort()         # тепер змінимо оригінал
print(clothes)
'''Створи список чисел numbers = [5, 2, 9, 1, 7].
→ Відсортуй у порядку спадання (reverse=True).'''
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

'''Створи список numbers = list(range(1, 11)).
Виведи суму, мінімум і максимум цього списку.'''
numbers = list(range(1, 11))
print(f'Максимальне число списку: {max(numbers)}, мінімальне число списку: {min(numbers)}, сума усіх чисел списку: {sum(numbers)}')

'''Створи список парних чисел від 2 до 20.
→ Виведи його та перевір довжину через len().'''
numbers = list(range(2, 21, 2))
print(len(numbers))

сurrency_units = 'pound', 'dollar', 'euro'
print(сurrency_units)
p, d, e = сurrency_units
print(p)
print(d)
print(e)