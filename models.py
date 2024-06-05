from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Heartbeat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    ping = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Heartbeat {self.time} - {self.ping}>'
