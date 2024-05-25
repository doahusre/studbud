from flask import Flask, render_template, request
import folium

app = Flask(__name__)

# Create custom icons
boy_icon = folium.CustomIcon(icon_image='icons/boy_buddy.png', icon_size=(30, 30))
girl_icon = folium.CustomIcon(icon_image='icons/girl_buddy.png', icon_size=(30, 30))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map', methods=['POST'])
def map_view():
    # Coordinates for UVic Campus
    uvic_latitude = 48.4634
    uvic_longitude = -123.3117
    zoom_start = 17

    map = folium.Map(location=[uvic_latitude, uvic_longitude], zoom_start=zoom_start)
    folium.Marker([48.464, -123.314], popup='Girl Buddy', icon=girl_icon).add_to(map)
    folium.Marker([uvic_latitude, uvic_longitude], popup='Boy Buddy', icon=boy_icon).add_to(map)
    map.save('templates/map.html')
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)

