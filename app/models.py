from datetime import datetime

from app import db

class Reading(db.Model):
    __tablename__ = 'readings'
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(64))
    therm_id = db.Column(db.Integer)
    channel = db.Column(db.Integer)
    battery = db.Column(db.String(64))
    brand = db.Column(db.String(64))
    model = db.Column(db.String(64))
    time = db.Column(db.DateTime, default=datetime.utcnow)
    temp_c = db.Column(db.Numeric)

    def __repr__(self):
        return f'<Reading: thermometer id {self.therm_id}, {self.temp_c}°C>'