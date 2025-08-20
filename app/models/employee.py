# app/models/employee.py
from app import db
from flask_login import UserMixin

class Employee(UserMixin, db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # hashed password recommended

    def __repr__(self):
        return f"<Employee {self.username}>"
  # store hashed password

