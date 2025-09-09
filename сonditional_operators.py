# 1. Умовні оператори if, else, elif
# Напиши програму, яка питає у користувача число і виводить:
# "Додатнє", якщо число > 0
# "Від’ємне", якщо число < 0
# "Нуль", якщо число == 0

def check_number ():
    try:
        user_num = int(input("Введіть ваше число: "))
        if user_num > 0:
            print(f"Ваше число {user_num} — додатнє")
        elif user_num < 0:
            print(f"Ваше число {user_num} — від'ємне")
        else:
            print(f"Ваше число {user_num} — це нуль")
    except ValueError:
        print("Будь ласка, введіть саме число!")


check_number()


# 2. Користувач вводить вік. Якщо < 18 → "Доступ заборонено", якщо 18–65 → "Доступ дозволено", якщо >65 → "Особливий доступ".

def check_age():
    try:
        user_age = int(input("Будь ласка, введіть ваш вік: "))
        if user_age < 0:
            print("Вік не може бути від'ємним!")
        elif user_age < 18:
            print("Вибачте, але доступ заборонено. Вам менше 18 років.")
        elif user_age <= 65:
            print("Вітаємо, доступ дозволено!")
        else:
            print("Вітаємо, вам надано обмежений доступ!")
    except ValueError:
        print("Будь ласка, введіть ваш вік числом!")

check_age()

# 3. Напиши програму, яка питає день тижня і виводить, чи це робочий день чи вихідний (використай elif).
def chack_day ():
        user_day = str(input("Введіть день тижня для перевірки: ")).strip().lower()
        work_days = {"понеділок", "вівторок", "середа", "четвер", "п'ятниця"}
        weekend_days = {"субота", "неділя"}
        if user_day in work_days:
            print(f'{user_day} - це робочий день')
        elif user_day in weekend_days:
            print(f'{user_day} - це вихідний день')
        else:
            print("Це не схоже на день тижня")


chack_day()