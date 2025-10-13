import os
from contacts import Contacts

contacts_book = "contacts_book.txt"
def load_contacts_from_file(path: str = contacts_book):
    """Завантажує контакти з файлу у Contacts.contacts_list.
       Файл очікує формат: first_name,last_name,email,phone (по рядку)."""
    Contacts.contacts_list.clear()
    if not os.path.isfile(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = [p.strip() for p in line.split(",")]
            if len(parts) < 4:
                continue  # некоректний рядок — ігноруємо
            first, last, email, phone = parts[:4]
            key = f"{first} {last}"
            Contacts.contacts_list[key] = {
                "Ім'я": first,
                "Прізвище": last,
                "Електронна пошта": email,
                "Номер телефону": phone
            }
def test_pull():
    print ("!yess!ав")