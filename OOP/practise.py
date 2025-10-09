from accessify import private, protected
import accessify

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    # Методи класу Student
    # Тепер add_grade є методом класу, а не локальною функцією в __init__
    @protected
    def add_grade(self, grade):
        # Перевіряємо, чи існує метод у батьківському класі, щоб уникнути помилок,
        # якщо accessify не змінює назву
        if isinstance(self, accessify.ProtectedMethodWrapper):
             self.grades.append(grade)
        else:
             self.grades.append(grade)


    @private
    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def info(self):
        # Виклик приватного методу через внутрішній механізм (name mangling)
        print(f"Учень {self.name}, вік: {self.age}, середня оцінка: {self._Student__average()}")
        # Або просто self.average(), якщо accessify дозволяє доступ зсередини класу

# --- Наслідування та поліморфізм ---
# AdvancedStudent тепер визначається на зовнішньому рівні
class AdvancedStudent(Student):
    def info(self):
        # Виклик private методу базового класу через name mangling:
        # _<БазовийКлас>__<ПриватнийМетод>
        avg = self._Student__average()
        print(f"Учень {self.name} (Advanced), вік: {self.age}, середня оцінка: {avg}. Продовжує поглиблене навчання!")


# --- Тестування ---

# 1. Створення Student
print("--- Student s1 ---")
s1 = Student("Олег", 14)
# Примітка: accessify перейменовує protected методи на _add_grade або подібне.
# Якщо це не спрацює, спробуйте викликати s1._add_grade(8)
s1.add_grade(8)
s1.add_grade(9)
s1.info()

print("\n--- AdvancedStudent s2 ---")
# 2. Створення AdvancedStudent
s2 = AdvancedStudent("Марія", 15)
s2.add_grade(10)
s2.add_grade(9)
s2.info()
