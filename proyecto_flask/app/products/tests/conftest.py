import pytest

from app import create_app
from conf.config import TestingConfig

@pytest.fixture #Puede tener parametros
def app():
    app = create_app(config = TestingConfig)
    with app.app_context():
        create_all()
        app.teardown_bkp = app.teardown_appcontext_funcs
        app.teardown_appcontext_funcs = []
        yield #Tener app disponible hasta que se necesite. Temporal
        drop_all()
    
    return app

@pytest.fixture
def product(app):
    """
    
    """
    with app.app_context():
        product = Product(name = 'fake-product', price = 1, description = 'hi', refundable = True)
        db.session.add(product)
        db.session.commit()
        return product

@pytest.fixture
def category(app):
    with app.app_context():
        category = Category(name = 'fake-category')
        db.session.add(category)
        db.session.commit()
        return category
