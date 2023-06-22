from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(
    host='localhost',
    port='5432',
    database='day2_demo',
    user='postgres',
    password='Sreealee@2609'
)
cursor = conn.cursor()

# GET /students
@app.route('/students', methods=['GET'])
def get_all_students():
    query = "SELECT name, roll_number FROM students"
    cursor.execute(query)
    rows = cursor.fetchall()
    students = []
    for row in rows:
        name, roll_number = row
        student = {'name': name, 'roll_number': roll_number}
        students.append(student)
    return jsonify(students)

# GET /students/<roll_number>
@app.route('/students/<int:roll_number>', methods=['GET'])
def get_student(roll_number):
    query = "SELECT name, roll_number FROM students WHERE roll_number = %s"
    value = (roll_number,)
    cursor.execute(query, value)
    row = cursor.fetchone()
    if row:
        name, roll_number = row
        student = {'name': name, 'roll_number': roll_number}
        return jsonify(student)
    return jsonify({'message': 'Student not found'})

# POST /students
@app.route('/students', methods=['POST'])
def add_student():
    student = request.get_json()
    name = student.get('name')
    roll_number = student.get('roll_number')
    query = "INSERT INTO students (name, roll_number) VALUES (%s, %s)"
    values = (name, roll_number)
    cursor.execute(query, values)
    conn.commit()
    return jsonify({'message': 'Student added successfully'})

# PUT /students/<roll_number>
@app.route('/students/<int:roll_number>', methods=['PUT'])
def update_student(roll_number):
    student = request.get_json()
    name = student.get('name')
    query = "UPDATE students SET name = %s WHERE roll_number = %s"
    values = (name, roll_number)
    cursor.execute(query, values)
    conn.commit()
    return jsonify({'message': 'Student updated successfully'})

# DELETE /students/<roll_number>
@app.route('/students/<int:roll_number>', methods=['DELETE'])
def remove_student(roll_number):
    query = "DELETE FROM students WHERE roll_number = %s"
    value = (roll_number,)
    cursor.execute(query, value)
    conn.commit()
    return jsonify({'message': 'Student removed successfully'})

if __name__ == '__main__':
    app.run(debug=True)
