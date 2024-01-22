from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, Primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    pages = db.Column(db.Integer,nullable=False)

class Student(db.Model):
    id = db.Column(db.Integer,Primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    age = db.Column(db.Integer,nullable=False)    