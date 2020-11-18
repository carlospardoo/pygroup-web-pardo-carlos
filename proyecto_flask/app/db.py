
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy() #Para trabajar directamente con la base de datos
ma = Marshmallow() #Para serializar

def drop_all():
    """
    Drop all tables in DB
    :return:
    """
    db.drop_all()#Método de SQLAlchemy que borra todas las tablas de la BD

def create_all():
    """
    Create all tables in DB
    :return:

    Utilizado siempre que se quiera iniciar aplicación desde cero
    """
    db.create_all()#Método de SQLAlchemy que crea todas las tablas de la BD

def remove_session():
    """
    Removes DB Session
    :return:
    """
    db.session.remove()


