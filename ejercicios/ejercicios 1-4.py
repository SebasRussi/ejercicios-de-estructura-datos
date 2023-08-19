class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades: list = grades

    def add_grade(self, numero):
        self.grades.append(numero)

    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        total = sum(self.grades)
        average = total / len(self.grades)
        return average


if __name__ == "__main__":
    student1 = Student("Alice", 18, [85, 92, 78, 90])
    student2 = Student("Bob", 19, [70, 65, 80, 75])

    print(f"Name of student1: {student1.name}")
    print(f"Age of student1: {student1.age}")
    print(f"Grades of student1: {student1.grades}")
    student1.add_grade(88)
    print(f"Grades of student1 after adding: {student1.grades}")