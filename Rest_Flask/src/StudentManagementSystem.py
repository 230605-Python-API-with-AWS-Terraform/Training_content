class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                return True
        return False

    def get_all_students(self):
        return self.students
    
    def get_student_by_roll_number(self, roll_number):
        for student in self.students:
            print(student.roll_number)
            if student.roll_number == roll_number:
                return student
        return None