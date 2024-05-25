import folium

def create_popup(student):
    popup_html = f"""
        <div style="font-family: Arial, sans-serif; text-align: center;">
            <h4>{student.name}</h4>
            <h5>Status: {student.status}</h5>
        </div>
    """
    return folium.Popup(popup_html, max_width=2650)

def create_map(students):
    # Coordinates for UVic Campus
    uvic_latitude = 48.4634
    uvic_longitude = -123.3117
    zoom_start = 16

    map = folium.Map(location=[uvic_latitude, uvic_longitude], zoom_start=zoom_start, tiles='cartodbpositron')

    for student in students:
        boy_icon = folium.CustomIcon(icon_image='icons/boy_buddy.png', icon_size=(30, 30))
        folium.Marker(
            location=[student.latitude, student.longitude],
            popup=create_popup(student),
            icon=boy_icon
        ).add_to(map)

    return map._repr_html_()
