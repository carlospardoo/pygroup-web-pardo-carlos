from flask import Flask
from products.views import prods
#from app.products.views import products

#Migraciones para mi
#https://flask-migrate.readthedocs.io/en/latest/

import sys
sys.path.append('..')

#import conf

from conf.config import DevelopmentConfig
from db import db, ma

from flask_migrate import Migrate, MigrateCommand#
from flask_script import Manager #

from flask_wtf import CSRFProtect

#app.register_blueprint(prods)
ACTIVE_ENDPOINTS = [('/products',prods)]

def create_migrations():
    """
    Call it only when need to do a migrate
    """
    #Migraciones
    migrate = Migrate(app,db)#
    manager = Manager(app)
    manager.add_command('db',MigrateCommand)
    manager.run()

def createApp(config=DevelopmentConfig):
    app = Flask(__name__,instance_relative_config=False)

    #Only uncomment if need a migrate
    #create_migrations()

    #Proteccion CSRF
    csrf = CSRFProtect(app)

    app.config.from_object(config)
    
    db.init_app(app)
    #ma = MarshMellow
    ma.init_app(app)

    csrf.init_app(app)

    @app.template_filter('datetimeformat')
    def datetimeformat(value,format='%B'):
        return value.strftime(format)

    with app.app_context():#Contexto es db, serializacion, logs
        db.create_all()#Crea todas las tablas del contexto

    for url,blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint,url_prefix=url)
    
    print("Token: "+config.SECRET_KEY)
    return app

if __name__ == '__main__':
    app_flask = createApp()
    app_flask.run()
    

