from flask import Flask, render_template, request, jsonify
from student import Student
import random
import string

from map import create_map

app = Flask(__name__)

dummy_students = []
def populate_dummy(n):
# Create dummy student data
    for i in range(n):
        name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        latitude = random.uniform(48.4629, 48.4634)
        longitude = random.uniform(-123.3116, -123.3106)
        student = Student(i, name, latitude, longitude)
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

if __name__ == '__main__':
    populate_dummy(20)
    app.run(debug=True)
