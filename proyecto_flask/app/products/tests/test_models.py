
def test_should_get_product_id_when_product_exists_in_db(app, product):
    with app.app_context():
        result = get_product_by_id(product.id)
        assert result['name'] == product.name

def test_should_raise_error_exeption_when_product_does_not_exists_in_db(app):
    pass


