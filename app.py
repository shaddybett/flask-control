from flask import Flask
from flask_restful import Resource,Api
from models import db,Book,Student

app=Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///control.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)

class BookData(Resource):
    def get(self):
       books = Book.query.all()
       return books
    
class StudentData(Resource):
    def get(self):
        students = Student.query.all()
        return students
    
        