from flask import Flask
from flask_restful import Resource,Api
from models import db

app=Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///control.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)

