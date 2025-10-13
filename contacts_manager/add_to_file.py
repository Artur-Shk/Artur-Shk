import os
from contacts import Contacts

contacts_book = "contacts_book.txt"
def load_contacts_from_file(path: str = contacts_book):
    """Завантажує контакти з файлу у Contacts.contacts_list.
       Файл очікує формат: first_name,last_name,email,phone (по рядку)."""
    Contacts.contacts_list.clear()  # очищаємо словник контактів у пам'яті перед завантаженням
    if not os.path.exists(path):  # перевіряємо, чи існує файл за вказаним шляхом
        return  # якщо файл не знайдено — виходимо з функції

    # відкриваємо файл для читання у кодуванні UTF-8
    with open(path, "r", encoding="utf-8") as f:
        for line in f:  # проходимо по кожному рядку файлу
            line = line.strip()  # видаляємо пробіли та символи переносу рядка спереду і ззаду
            if not line:  # пропускаємо порожні рядки
                continue
            # розбиваємо рядок на частини по комі та обрізаємо пробіли
            parts = [p.strip() for p in line.split(",")]
            if len(parts) < 4:  # якщо рядок некоректний (менше ніж 4 частини) — пропускаємо
                continue
            first, last, email, phone = parts[:4]  # розпаковуємо перші 4 частини
            key = f"{first} {last}"  # формуємо ключ для словника (ім'я + прізвище)
            # додаємо контакт у словник Contacts.contacts_list
            Contacts.contacts_list[key] = {
                "Ім'я": first,
                "Прізвище": last,
                "Електронна пошта": email,
                "Номер телефону": phone
            }


def delete_contact_from_file_by_name(name: str, path: str = "contacts.txt"):
    """Видаляє всі рядки, де зустрічається ім'я (case-insensitive).
    Повертає кількість видалених рядків."""
    if not os.path.exists(path):
        print("❌ Файл контактів не знайдено.")
        return 0
    # 1. Зчитуємо всі рядки з файлу
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    # 2. Відфільтровуємо — залишаємо лише ті, де ім'я НЕ зустрічається
    filtered = [l for l in lines if name.lower() not in l.lower()]
    # 3. Рахуємо, скільки рядків було видалено
    deleted_count = len(lines) - len(filtered)
    # 4. Перезаписуємо файл без видалених рядків
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(filtered)
    # 5. Повідомляємо користувача
    if deleted_count > 0:
        print(f"🗑️ Видалено {deleted_count} контакт(ів) з ім'ям '{name}'.")
    else:
        print(f"ℹ️ Контакт з ім'ям '{name}' не знайдено.")

    return deleted_count

