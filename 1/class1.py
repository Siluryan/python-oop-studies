class Student:
    def __init__(self, name, age, grade):
        self.name  = name
        self.age   = age
        self.grade = grade

    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, course_name, max_students):
        self.course_name  = course_name
        self.max_students = max_students
        self.students     = list()

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = int()
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)
    
course = Course('Science', 10)

student1 = Student('Arlindo', 47, 7.5)
student2 = Student('Bernardo', 35, 6.8)

course.add_student(student1)
course.add_student(student2)