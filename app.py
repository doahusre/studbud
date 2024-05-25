from flask import Flask, render_template, request
from student import Student

from map import create_map

app = Flask(__name__)

# Create dummy student data
dummy_students = [
    Student('Alice', 48.4634, -123.3117),
    Student('Bob', 48.4634, -123.311),
    Student('Charlie', 48.4629, -123.310),
    Student('Diana', 48.4630, -123.309),
    Student('Eve', 48.4632, -123.308),
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def view_map():
    return render_template('map.html', map=create_map(dummy_students))

@app.route('/cards', methods=['GET'])
def view_card():
    return render_template('card.html', users=dummy_students)

if __name__ == '__main__':
    app.run(debug=True)
