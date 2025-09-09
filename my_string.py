def greet_user():
    first_name = input("Введіть ваше ім'я: ")
    last_name = input("Введіть ваше прізвище: ")
    greeting = "Привіт {} {}! Радий вас бачити!"
    result = greeting.format(first_name, last_name)
    print(result)


def user_country():
    country = str(input("Введіть країну вашого проживання:" ))
    if country.lower() == "росія":
        print("Кацап, іди нахуй")
    else:
        greet_user()

user_country()