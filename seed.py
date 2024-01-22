from flask import Flask
from models import db,Book,Student
from flask_restful import Api

app = Flask(__name__)
api=Api(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///control.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)

with app.app_context():
    book_data={
        'name':'SCience',
        'pages':240
    }
    student_data={
        'name':'Bett',
        'age':18
    }

    new_book=Book(**book_data)
    new_student=Student(**student_data)

with app.db.begin():
    db.session.add(new_book)
    db.session.add(new_student)
    db.session.commit()    