def greet_user():
    first_name = input("Введіть ваше ім'я: ")
    last_name = input("Введіть ваше прізвище: ")
    greeting = "Привіт {} {}! Радий вас вітати!"
    result = greeting.format(first_name, last_name)
    print(result)


def password():
    user_password = input("Введіть ваш пароль: ")
    if user_password == "Qwerty123":
        print("Ласкаво просимо!")
    else:
        print("Нажаль ваш пароль неправильний!")


def user_country():
    country = input("Введіть країну вашого проживання: ")
    if country.lower() == "росія":
        print("Кацап, іди нахуй!")
    else:
        greet_user()
        password()


user_country()


