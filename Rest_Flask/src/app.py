from flask import Flask, jsonify, request
from Student import Student
from StudentManagementSystem import StudentManagementSystem

app = Flask(__name__)
sms = StudentManagementSystem()

# API endpoint to get all students
@app.route('/students', methods=['GET'])
def get_students():
    students = sms.get_all_students()
    student_list = []
    for student in students:
        student_list.append({
            'name': student.name,
            'roll_number': student.roll_number
        })
    return jsonify(student_list)

# API endpoint to get a specific student
@app.route('/students/<int:roll_number>', methods=['GET'])
def get_student(roll_number):
    student = sms.get_student_by_roll_number(roll_number)
    if student:
        return jsonify({
            'name': student.name,
            'roll_number': student.roll_number
        })
    return jsonify({'message': 'Student not found'}), 404

# API endpoint to add a new student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    name = data['name']
    roll_number = data['roll_number']
    student = Student(name, roll_number)
    sms.add_student(student)
    return jsonify({'message': 'Student added successfully'})

# API endpoint to update a student
@app.route('/students/<int:roll_number>', methods=['PUT'])
def update_student(roll_number):
    data = request.get_json()
    name = data['name']
    student = sms.get_student_by_roll_number(roll_number)
    if student:
        student.name = name
        return jsonify({'message': 'Student updated successfully'})
    return jsonify({'message': 'Student not found'}), 404

# API endpoint to delete a student
@app.route('/students/<int:roll_number>', methods=['DELETE'])
def delete_student(roll_number):
    result = sms.remove_student(roll_number)
    if result:
        return jsonify({'message': 'Student deleted successfully'})
    return jsonify({'message': 'Student not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
