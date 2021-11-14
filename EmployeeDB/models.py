from EmployeeDB import db
from datetime import datetime

class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(6), nullable=False)
    role = db.Column(db.String(40), nullable=False)
    department = db.Column(db.String(40), nullable=False)
    joining_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return self.name
