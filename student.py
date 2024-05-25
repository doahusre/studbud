# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class Student(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     latitude = db.Column(db.Float, nullable=False)
#     longitude = db.Column(db.Float, nullable=False)

class Student:
    def __init__(self, name, latitude, longitude, status='Studying'):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.status = status