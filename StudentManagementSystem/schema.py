import strawberry
from typing import List
from dao import StudentDAO


@strawberry.type
class StudentType:
    id: int
    name: str
    email: str


@strawberry.type
class Query:
    @strawberry.field
    def get_students(self) -> List[StudentType]:
        return StudentDAO.get_all_students()


@strawberry.type
class Mutation:
    @strawberry.mutation
    def createStudent(self, name: str, email: str) -> StudentType:
        return StudentDAO.create_student(name, email)

    @strawberry.mutation
    def updateStudent(self, id: int, name: str, email: str) -> StudentType:
        return StudentDAO.update_student(id, name, email)
# Create the GraphQL schema
schema = strawberry.Schema(query=Query, mutation=Mutation)

























