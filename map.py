from flask import Flask, jsonify, render_template, request, redirect, url_for
import folium
from db import db, Buddy, populate_dummy_data

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/studybuddy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create custom icons
boy_icon = folium.CustomIcon(icon_image='icons/boy_buddy.png', icon_size=(30, 30))
girl_icon = folium.CustomIcon(icon_image='icons/girl_buddy.png', icon_size=(30, 30))

@app.route('/')
def index():
    return redirect(url_for('cards_view'))

@app.route('/map', methods=['GET'])
def map_view():
    # Coordinates for UVic Campus
    uvic_latitude = 48.4634
    uvic_longitude = -123.3117
    zoom_start = 17

    map = folium.Map(location=[uvic_latitude, uvic_longitude], zoom_start=zoom_start)
    buddies = Buddy.query.all()
    for buddy in buddies:
        icon = boy_icon if buddy.gender == 'boy' else girl_icon
        folium.Marker([buddy.latitude, buddy.longitude], popup=buddy.name, icon=icon).add_to(map)
    
    map.save('templates/map.html')
    return render_template('map.html')

@app.route('/cards', methods=['GET'])
def cards_view():
    users = Buddy.query.all()  # You can adjust this query to fetch non-buddies if needed
    return render_template('card.html', users=users)

@app.route('/add_buddy', methods=['POST'])
def add_buddy():
    data = request.get_json()
    user_id = data.get('user_id')
    # Here you should add logic to associate the user with the current user's buddy list
    # For now, we'll just add them to the Buddy table again for simplicity
    user = Buddy.query.get(user_id)
    if user:
        # Update your buddy list logic here
        db.session.commit()
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error'}), 400

@app.route('/update_buddy', methods=['POST'])
def update_buddy():
    buddy_id = request.form.get('buddy_id')
    buddy = Buddy.query.get(buddy_id)
    if buddy:
        buddy.name = request.form.get('name')
        buddy
        db.session.commit()
        return redirect(url_for('cards_view'))
    return jsonify({'status': 'error'}), 400

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not Buddy.query.first():
            populate_dummy_data()
    app.run(debug=True)
