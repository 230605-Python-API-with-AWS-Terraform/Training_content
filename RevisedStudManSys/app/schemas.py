import strawberry
from database import db
from dao import StudentDAO
from typing import List, Union


@strawberry.type
class Student:
    id: int
    name: str
    age: int
    email: str

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_student(self, name: str, age: int, email: str) -> Student:
        # Create a new student using the DAO
        student = StudentDAO.create_student(name, age, email)
        return student

    @strawberry.mutation
    def update_student(self, id: int, name: str, age: int, email: str) -> Student:
        # Get the student by ID
        student = StudentDAO.get_student_by_id(id)
        if student:
            # Update the student using the DAO
            student = StudentDAO.update_student(student, name, age, email)
            return student
        else:
            raise ValueError(f"Student with ID {id} not found")

    @strawberry.mutation
    def delete_student(self, id: int) -> bool:
        # Get the student by ID
        student = StudentDAO.get_student_by_id(id)
        if student:
            # Delete the student using the DAO
            StudentDAO.delete_student(student)
            return True
        else:
            raise ValueError(f"Student with ID {id} not found")

@strawberry.type
class Query:
    @strawberry.field
    def students(self) -> List[Student]:
        # Get all students using the DAO
        return StudentDAO.get_all_students()

    @strawberry.field
    def student(self, id: int) -> Union[Student, None]:
        # Get the student by ID using the DAO
        return StudentDAO.get_student_by_id(id)


schema = strawberry.Schema(query=Query, mutation=Mutation)
