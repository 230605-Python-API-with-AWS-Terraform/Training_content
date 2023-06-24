from database import db_session
from models import Student

class StudentDAO:
    @staticmethod
    def get_all_students():
        return db_session.query(Student).all()

    @staticmethod
    def create_student(name, email):
        student = Student(name=name, email=email)
        db_session.add(student)
        db_session.commit()
        return student

    @staticmethod
    def update_student(id, name, email):
        student = db_session.query(Student).get(id)
        if student:
            student.name = name
            student.email = email
            db_session.commit()
        return student

    @staticmethod
    def delete_student(id):
        student = db_session.query(Student).get(id)
        if student:
            db_session.delete(student)
            db_session.commit()
            return True
        return False
