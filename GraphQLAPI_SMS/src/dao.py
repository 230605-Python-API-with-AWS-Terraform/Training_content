from models import Student, Course, Enrollment
from database import db_session

def create_student(name):
    student = Student(name=name)
    db_session.add(student)
    db_session.commit()
    return student

def get_student_by_id(student_id):
    return Student.query.get(student_id)

def create_course(name):
    course = Course(name=name)
    db_session.add(course)
    db_session.commit()
    return course

def get_course_by_id(course_id):
    return Course.query.get(course_id)

def enroll_student_in_course(student_id, course_id):
    student = get_student_by_id(student_id)
    course = get_course_by_id(course_id)
    enrollment = Enrollment(student_id=student.id, course_id=course.id)
    db_session.add(enrollment)
    db_session.commit()
    return enrollment

def get_enrollments_by_student(student_id):
    return Enrollment.query.filter_by(student_id=student_id).all()

def get_enrollments_by_course(course_id):
    return Enrollment.query.filter_by(course_id=course_id).all()
