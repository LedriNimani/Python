class Student:
    school_name = "Digital School"
    #student_name = "Student"

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


student_1 = Student("Alice",15,"Python")
print(student_1.course)

# student_1 = Student()
# print(student_1.school_name)
# print(student_1.student_name)

