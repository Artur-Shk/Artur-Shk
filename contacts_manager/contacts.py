class Contacts:
    contacts_list = {}

    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def add_contact(self):
        key = f'{self.first_name} {self.last_name}'
        if key not in self.contacts_list:
            self.contacts_list[key] = {
                "Ім'я": self.first_name,
                "Прізвище": self.last_name,
                "Електронна пошта": self.email,
                "Номер телефону": self.phone_number
            }
            print(f"Контакт {key} додано")
        else:
            print(f"Контакт {key} вже існує у вашій телефонній книзі. Будь ласка зміть ім'я")

    def remove_contact(self):
        key = f"{self.first_name} {self.last_name}"
        if key in self.contacts_list:
            del self.contacts_list[key]
            print(f"Контакт {key} видалено!")
        else:
            print(f"Контакт {key} відсутній у списку!")

    @classmethod
    def show_alone_contact(cls, first_name, last_name):
        key = f"{first_name} {last_name}"
        if key in cls.contacts_list:
            contact = cls.contacts_list[key]
            print(
                f"🧍 Ім'я: {contact['Ім\'я']} | 👨‍💼 Прізвище: {contact['Прізвище']} | ✉️ {contact['Електронна пошта']} | 📞 {contact['Номер телефону']}")
        else:
            print(f"⚠️ Контакт {key} не знайдено!")

    @classmethod
    def show_contacts(cls):
        print("\n".join([
            f" ‍👨‍💼 {key}\n"
            f" ✉️ {info['Електронна пошта']}\n"
            f" 📞 {info['Номер телефону']}\n"
            f"{'-' * 30}"
            for key, info in cls.contacts_list.items()
        ]))


c1 = Contacts("Іван", "Іваненко", "ivan@example.com", "123456789")
c1.add_contact()

c2 = Contacts("Марія", "Петренко", "maria@example.com", "987654321")
c2.add_contact()

Contacts.show_alone_contact("Іван", "Іваненко")

c3 = Contacts("Марія", "Петренко", "maria@example.com", "987654321")
c3.remove_contact()

Contacts.show_contacts()
