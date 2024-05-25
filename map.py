from student import Student
import folium

# Create custom icons
girl_icon = folium.CustomIcon(icon_image='icons/girl_buddy.png', icon_size=(30, 30))

# Create dummy student data
dummy_students = [
    Student('Alice', 48.4634, -123.3117),
    Student('Bob', 48.4634, -123.311),
    Student('Charlie', 48.4629, -123.310),
    Student('Diana', 48.4630, -123.309),
    Student('Eve', 48.4632, -123.308),
]

def create_popup(student):
    popup_html = f"""
        <div style="font-family: Arial, sans-serif; text-align: center;">
            <h4>{student.name}</h4>
            <h5>Status: {student.status}</h5>
        </div>
    """
    return folium.Popup(popup_html, max_width=2650)

def create_map():
    # Coordinates for UVic Campus
    uvic_latitude = 48.4634
    uvic_longitude = -123.3117
    zoom_start = 17

    map = folium.Map(location=[uvic_latitude, uvic_longitude], zoom_start=zoom_start, tiles='cartodbpositron')


    for student in dummy_students:
        boy_icon = folium.CustomIcon(icon_image='icons/boy_buddy.png', icon_size=(30, 30))
        folium.Marker(
            location=[student.latitude, student.longitude],
            popup=create_popup(student),
            icon=boy_icon
        ).add_to(map)

    map.save('templates/map.html')
