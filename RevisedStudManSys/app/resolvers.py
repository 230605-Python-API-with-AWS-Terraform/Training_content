from dao import StudentDAO

def resolve_students():
    return StudentDAO.get_all_students()

def resolve_student(info, id):
    return StudentDAO.get_student_by_id(id)

def resolve_create_student(info, name, age, email):
    return StudentDAO.create_student(name, age, email)

def resolve_update_student(info, id, name, age, email):
    student = StudentDAO.get_student_by_id(id)
    if student:
        return StudentDAO.update_student(student, name, age, email)

def resolve_delete_student(info, id):
    student = StudentDAO.get_student_by_id(id)
    if student:
        StudentDAO.delete_student(student)
        return True
    return False
