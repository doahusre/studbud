from typing import List

class Student:
    def __init__(self, id, name, latitude, longitude, courses=[], program="Computer Science", status='Studying'):
        self.id = id
        self.name = name
        self.courses = courses
        self.program = program
        self.latitude = latitude
        self.longitude = longitude
        self.status = status
    
class User:
    name: str
    program: str
    courses: List[str]
