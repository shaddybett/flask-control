from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    pages = db.Column(db.Integer,nullable=False)
    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'pages':self.pages
        }

class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    age = db.Column(db.Integer,nullable=False)    

    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'age':self.age
        }