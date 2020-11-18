from flask import Flask
from products.views import prods
#from app.products.views import products

import sys
sys.path.append('..')

#import conf

from conf.config import DevelopmentConfig
from db import db, ma

#app.register_blueprint(prods)
ACTIVE_ENDPOINTS = [('/products',prods)]

def createApp(config=DevelopmentConfig):
    app = Flask(__name__)

    app.config.from_object(config)
    
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():#Contexto es db, serializacion, logs
        db.create_all()#Crea todas las tablas del contexto

    for url,blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint,url_prefix=url)
    
    return app

if __name__ == '__main__':
    app_flask = createApp()
    app_flask.run()
