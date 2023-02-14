
class Student:

    def __init__(self, id_arg, name_arg, faculty_arg):
        self.id = id_arg
        self.name = name_arg
        self.faculty = faculty_arg

    def show_faculty(self):
        msg = f"{self.id} - {self.name} - {self.faculty}"
        print('show_faculty:', msg)


student = Student(0, "Vitalii Honchar", "Radio Engineering")
kate = Student(1, "Kate Biliak", "Computer Science")

student.show_faculty()
kate.show_faculty()
