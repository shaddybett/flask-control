from flask import Flask,jsonify
from flask_restful import Resource,Api
from models import db,Book,Student
from flask_migrate import Migrate

app=Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///control.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)
migrate = Migrate(app,db)
class BookData(Resource):
    def get(self):
       books = Book.query.all()
       return jsonify([book.__dict__ for book in books ])
    
class StudentData(Resource):
    def get(self):
        students = Student.query.all()
        return [student.__dict__ for student in students]

api.add_resource(BookData,'/books')
api.add_resource(StudentData,'/students')

if __name__=='__main__':
    app.run(debug=True,port=4000)