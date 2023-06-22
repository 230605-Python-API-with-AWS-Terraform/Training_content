from flask import Flask, render_template, request, redirect
from Student import Student
from StudentManagementSystem import StudentManagementSystem

app = Flask(__name__)
sms = StudentManagementSystem()

@app.route('/')
def home():
    students = sms.get_all_students()
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        roll_number = request.form['roll_number']
        student = Student(name, roll_number)
        sms.add_student(student)
        return redirect('/')
    return render_template('add.html')

@app.route('/update', methods=['PUT'])
def update_student():
    data=request.get_json()

    student=sms.get_student_by_roll_number(roll_number)
    if student:
        student.name=data['name']
        student.roll_number=data['roll_number']
        return "Student updated successfully"
    return "Student not found",404

@app.route('/remove/<roll_number>')
def remove_student(roll_number):
    sms.remove_student(roll_number)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
