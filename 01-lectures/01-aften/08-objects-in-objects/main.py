"""
Example of objects in object
"""


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_grade_average(self):
        avg = 0
        for student in self.students:
            avg += student.get_grade()

        return avg / len(self.students)


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


course = Course("Udvidet programmering med Python")

s1 = Student("Anika", 24, 80)
s2 = Student("Jonas", 41, 40)
s3 = Student("Mette", 35, 80)

course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(course.get_grade_average())
