class Person():
    def __init__(self, name):
        """Ініціалізація атрибутів персони - ім'я та вік"""
        self.name = name
        print(f"Об'єкт {self.name} створено")

    def __del__(self):
        print(f"Об'єкт {self.name} видалено")



man = Person("Fhneh")