from models import Student
from database import db

class StudentDAO:
    @staticmethod
    def get_all_students():
        return Student.query.all()

    @staticmethod
    def get_student_by_id(id):
        return Student.query.get(id)

    @staticmethod
    def create_student(name, age, email):
        student = Student(name=name, age=age, email=email)
        db.session.add(student)
        db.session.commit()
        return student

    @staticmethod
    def update_student(student, name, age, email):
        student.name = name
        student.age = age
        student.email = email
        db.session.commit()
        return student

    @staticmethod
    def delete_student(student):
        db.session.delete(student)
        db.session.commit()
