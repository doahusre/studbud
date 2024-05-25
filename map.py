from flask import Flask, render_template, request
import folium

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map', methods=['POST'])
def map_view():
    # Coordinates for UVic Campus
    uvic_latitude = 48.4634
    uvic_longitude = -123.3117
    zoom_start = 15  # Adjust the zoom level as needed to focus on the campus

    folium_map = folium.Map(location=[uvic_latitude, uvic_longitude], zoom_start=zoom_start)
    folium.Marker([uvic_latitude, uvic_longitude], popup="UVic Campus").add_to(folium_map)
    folium_map.save('templates/map.html')
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)
