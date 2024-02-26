from flask import Flask, request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    year = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age}, year={self.year})"

@app.route('/students', methods=['POST'])
def create_student():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.json.get('age')
        year = request.form.get('year')
        created_at = datetime.utcnow()
        student = Student(name=name, age=age, year=year, created_at=created_at)
        db.session.add(student)
        db.session.commit()
        return 'Student created successfully'
    else:
        return 'Invalid request method'
    
@app.route('/students/<int:id>', methods=['GET'])
def show_student(id):
    student = Student.query.all()
    print(student)

@app.route('/students/<int:id>', methods=['POST'])
def update_student(id):
    student = Student.query.get(id)
    if student:
        name = request.form.get('name')
        age = request.json.get('age')
        year = request.form.get('year')
        student.name = name
        student.age = age
        student.year = year
        db.session.commit()
        return 'Student updated successfully'
    else:
        return 'Student not found'

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if student:
        db.session.delete(student)
        db.session.commit()
        return 'Student deleted successfully'
    else:
        return 'Student not found'
    
