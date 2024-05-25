from flask import Flask, render_template, request, jsonify
from entities import Student, User
import random
import string

from map import create_map

app = Flask(__name__)

dummy_students = []
def populate_dummy(n):
# Create dummy student data
    progams = ['Computer Science', 'Software Engineering', 'Electrical Engineering', 'Mechanical Engineering', 'Civil Engineering', 'Biomedical Engineering', 'Mathematics', 'Physics', 'Chemistry', 'Biology']
    courses = ['CSC 110', 'CSC 115', 'CSC 225', 'CSC 230', 'CSC 360', 'CSC 370', 'CSC 110', 'CSC 115', 'CSC 225', 'CSC 230', 'CSC 360', 'CSC 370']
    for i in range(n):
        name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        latitude = random.uniform(48.4620, 48.4639)
        longitude = random.uniform(-123.3120, -123.3100)
        sample_courses = random.sample(courses, random.randint(1, 3))
        program = random.choice(progams)
        student = Student(i, name, latitude, longitude, sample_courses, program)
        dummy_students.append(student)

buddies = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def view_map():
    map = create_map(buddies)
    return render_template('map.html', map=map)

@app.route('/cards', methods=['GET'])
def view_card():
    random.shuffle(dummy_students)
    return render_template('card.html', users=dummy_students)

@app.route('/swipe_right', methods=['POST'])
def swipe_right():
    data = request.get_json()
    print(data)
    user_id = int(data['user_id'])
    if user_id:
        for student in dummy_students:
            if student.id == user_id:
                buddies.append(student)
                dummy_students.remove(student)
                return jsonify({"message": "User added successfully"}), 200
    return jsonify({"message": "Invalid data"}), 400

@app.route('/buddies')
def view_buddies():
    return render_template('buddies.html', users=buddies)

# PLEASE USE THIS ENDPOINT TO REMOVE A BUDDY
@app.route('/remove_buddy', methods=['POST'])
def remove_buddy():
    data = request.get_json()
    print(data)
    user_id = int(data['user_id'])
    if user_id:
        for student in buddies:
            if student.id == user_id:
                dummy_students.append(student)
                buddies.remove(student)
                return jsonify({"message": "User removed successfully"}), 200
    return jsonify({"message": "Invalid data"}), 400

@app.route('/profile')
def view_profile():
    return render_template('profile.html')

if __name__ == '__main__':
    populate_dummy(20)
    app.run(debug=True)
