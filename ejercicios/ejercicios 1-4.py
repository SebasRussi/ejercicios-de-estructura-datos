class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades: list = [2, 3, 4, 5, 4]

    def add_grade(self, numero):
        self.grades.append(numero)

    def average_grade(self):
        for i in self.grades:
            suma = suma + i
            average = suma/i



if __name__ == "__main__":
    est1 = Student("jorge", 14)
    est1.add_grade(5)
    print(est1)