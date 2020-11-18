#Configuración del entorno de desarrollo

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///shop.sqlite3" #Direccion de la BD. Como la BD se crea desde flask, va así como está
    SQLALCHEMY_TRACK_MODIFICATION = False #Para no registrar cada transacción hecha

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql:///user@localhost/foo" #Direccion de la BD

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

