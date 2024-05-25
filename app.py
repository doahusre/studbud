from flask import Flask, render_template, request

from map import create_map

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map', methods=['POST'])
def view_map():
    create_map()
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)
