import os
import re

contacts = []

def load_contacts():
    """Завантажує контакти з файлу у глобальний список contacts."""
    contacts.clear()
    if os.path.exists("doc/contacts.txt"):
        with open("doc/contacts.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    name, phone, email = line.split(",")
                except ValueError:
                    # некоректний рядок — пропускаємо
                    print(f"Пропущено некоректний рядок у файлі: {line}")
                    continue
                contacts.append({
                    "name": name.strip(),
                    "phone": phone.strip(),
                    "email": email.strip()
                })

def save_contacts():
    """Зберігає contacts у файл у папці doc (створює, якщо відсутня)."""
    os.makedirs("doc", exist_ok=True)
    with open("doc/contacts.txt", "w", encoding="utf-8") as f:
        for c in contacts:
            f.write(f"{c['name']},{c['phone']},{c['email']}\n")

def add_contact():
    """Додає новий контакт з валідацією номера і email."""
    user_name = input("Введіть ім'я нового контакту: ").strip()
    if not user_name:
        print("Ім'я не може бути порожнім.")
        return

    # Перевірка номера
    while True:
        user_phone = input("Введіть номер нового контакту (лише цифри): ").strip()
        if not user_phone.isdigit():
            print("❌ Помилка: номер телефону повинен містити лише цифри. Спробуйте ще раз.")
            continue
        if len(user_phone) < 7:
            print("❌ Помилка: номер телефону не може містити менше 7 цифр. Спробуйте ще раз.")
            continue
        break

    # Перевірка email
    email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    while True:
        user_email = input("Введіть email нового контакту: ").strip()
        if "@" not in user_email:
            print("❌ Помилка: email повинен містити символ '@'. Спробуйте ще раз.")
            continue
        domain_part = user_email.split("@")[-1]
        if "." not in domain_part:
            print("❌ Помилка: після '@' має бути крапка. Спробуйте ще раз.")
            continue
        if re.fullmatch(email_pattern, user_email) is None:
            print("❌ Помилка: email не відповідає формату. Спробуйте ще раз.")
            continue
        break

    contacts.append({
        "name": user_name,
        "phone": user_phone,
        "email": user_email
    })
    print("✅ Контакт успішно додано!")
    save_contacts()  # зберігаємо одразу

def show_contacts():
    """Виводить усі контакти у списку."""
    if not contacts:
        print("Список контактів порожній.")
        return
    print(f"Всього контактів: {len(contacts)}")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. Ім'я: {c['name']}, Телефон: {c['phone']}, Email: {c['email']}")

def search_contacts(search_name):
    """Повертає список контактів (словників) де search_name частково входить в name (нечутливо до регістру)."""
    results = []
    for c in contacts:
        if search_name.lower() in c['name'].lower():
            results.append(c)
    return results

def delete_contact(search_name):
    """
    Шукає контакти по імені, якщо знайдено кілька — пропонує вибір, потім видаляє вибраний.
    Повертає True якщо щось видалено, інакше False.
    """
    results = search_contacts(search_name)
    if not results:
        print(f"Контакт з ім'ям, що містить '{search_name}', не знайдено.")
        return False

    # Якщо один — підтвердження видалення
    if len(results) == 1:
        c = results[0]
        print(f"Знайдено 1 контакт: Ім'я: {c['name']}, Телефон: {c['phone']}, Email: {c['email']}")
        confirm = input("Видалити цей контакт? (y/n): ").strip().lower()
        if confirm == "y":
            contacts.remove(c)
            save_contacts()
            print("Контакт видалено.")
            return True
        else:
            print("Видалення скасовано.")
            return False

    # Якщо кілька — показуємо з індексами та просимо вибрати
    print(f"Знайдено {len(results)} контактів:")
    for idx, c in enumerate(results, start=1):
        print(f"{idx}. Ім'я: {c['name']}, Телефон: {c['phone']}, Email: {c['email']}")

    while True:
        choice = input("Введіть номер контакту для видалення або 'all' щоб видалити всі знайдені, або 'c' щоб скасувати: ").strip().lower()
        if choice == "c":
            print("Видалення скасовано.")
            return False
        if choice == "all":
            for c in results:
                if c in contacts:
                    contacts.remove(c)
            save_contacts()
            print(f"Видалено {len(results)} контактів.")
            return True
        if choice.isdigit():
            n = int(choice)
            if 1 <= n <= len(results):
                c = results[n-1]
                contacts.remove(c)
                save_contacts()
                print(f"Видалено контакт: {c['name']}")
                return True
        print("Невірний ввід. Спробуйте ще раз.")

def main_menu():
    """Меню користувача з вибором дій."""
    load_contacts()
    while True:
        print("\n--- Меню Контактів ---")
        print("1 — Додати контакт")
        print("2 — Показати всі контакти")
        print("3 — Пошук контакту за ім'ям")
        print("4 — Видалити контакт за ім'ям")
        print("5 — Вихід")
        choice = input("Оберіть дію (1-5): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_contacts()
        elif choice == "3":
            name = input("Введіть ім'я для пошуку (частково допускається): ").strip()
            if not name:
                print("Ім'я не може бути порожнім.")
                continue
            found = search_contacts(name)
            if found:
                print(f"Знайдено {len(found)} контакт(ів):")
                for c in found:
                    print(f"Ім'я: {c['name']}, Телефон: {c['phone']}, Email: {c['email']}")
            else:
                print("Контакт не знайдено.")
        elif choice == "4":
            name = input("Введіть ім'я для видалення (частковий збіг допускається): ").strip()
            if name:
                delete_contact(name)
            else:
                print("Ім'я не може бути порожнім.")
        elif choice == "5":
            print("Вихід. До побачення!")
            break
        else:
            print("Невірний вибір. Введіть цифру від 1 до 5.")

if __name__ == "__main__":
    main_menu()
