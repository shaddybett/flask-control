from flask import Flask
from server.models import db,Book,Student
from server.app import app

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///control.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)
app.app_context().push()
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

with db.session.begin():
    db.session.add(new_book)
    db.session.add(new_student)
    db.session.commit()    