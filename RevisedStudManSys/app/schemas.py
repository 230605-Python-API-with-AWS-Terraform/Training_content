import strawberry
from typing import List
from dao import StudentDAO

@strawberry.type
class Student:
    id: int
    name: str
    age: int
    email: str

@strawberry.type
class Query:
    students: List[Student]

    def resolve_students(self) -> List[Student]:
        dao = StudentDAO()
        return dao.get_all_students()

schema = strawberry.Schema(query=Query)
