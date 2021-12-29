from db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True) #username
    password = db.Column(db.String(100))
    name = db.Column(db.String(250))
