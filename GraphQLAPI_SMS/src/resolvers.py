import strawberry

from dao import create_student, create_course, enroll_student_in_course, get_enrollments_by_student, get_enrollments_by_course
from typing import List

from models import Enrollment

@strawberry.type
class Mutation:
    @strawberry.mutation
    def createStudent(self, info, name: str) -> str:
        student = create_student(name)
        return f"Student {student.name} created successfully."

    @strawberry.mutation
    def createCourse(self, info, name: str) -> str:
        course = create_course(name)
        return f"Course {course.name} created successfully."

    @strawberry.mutation
    def enrollStudent(self, info, student_id: int, course_id: int) -> str:
        enrollment = enroll_student_in_course(student_id, course_id)
        return f"Student with ID {enrollment.student_id} enrolled in Course with ID {enrollment.course_id}."

@strawberry.type
class Query:
    @strawberry.field
    def enrollmentsByStudent(self, info, student_id: int) -> List[Enrollment]:
        return get_enrollments_by_student(student_id)

    @strawberry.field
    def enrollmentsByCourse(self, info, course_id: int) -> List[Enrollment]:
        return get_enrollments_by_course(course_id)

schema = strawberry.Schema(query=Query, mutation=Mutation)
