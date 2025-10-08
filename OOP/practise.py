from accessify import private, protected

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    @protected
    def add_grade(self, grade):
        self.grades.append(grade)

    @private
    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def info(self):
        print(f"Учень {self.name}, вік: {self.age}, середня оцінка: {self.average()}")

# Наслідування та поліморфізм
class AdvancedStudent(Student):
    def info(self):
        avg = self._Student__average()  # виклик private методу базового класу
        print(f"Учень {self.name} (Advanced), вік: {self.age}, середня оцінка: {avg}. Продовжує поглиблене навчання!")


# --- Тестування ---
s1 = Student("Олег", 14)
s1.add_grade(8)
s1.add_grade(9)
s1.info()

s2 = AdvancedStudent("Марія", 15)
s2.add_grade(10)
s2.add_grade(9)
s2.info()
