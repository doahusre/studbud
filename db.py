from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Buddy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

def populate_dummy_data():
    dummy_buddies = [
        Buddy(name='Alice', gender='girl', latitude=48.464, longitude=-123.314),
        Buddy(name='Bob', gender='boy', latitude=48.4635, longitude=-123.3115),
        Buddy(name='Charlie', gender='boy', latitude=48.4636, longitude=-123.3125),
        Buddy(name='Diana', gender='girl', latitude=48.4637, longitude=-123.3135),
    ]
    db.session.bulk_save_objects(dummy_buddies)
    db.session.commit()
