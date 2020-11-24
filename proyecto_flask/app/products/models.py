from datetime import datetime
from flask import jsonify
from db import db, ma

class Product(db.Model):
    """
    """
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    price = db.Column(db.Integer,nullable=False)
    weight = db.Column(db.Integer,default=1)
    #image = db.Column(db.String(500),default="https://acortar.link/3ZXKy")
    description = db.Column(db.String(500),nullable=True)
    refundable = db.Column(db.Boolean,nullable=False)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    created_at = db.Column(db.DateTime,default=datetime.now())
    updated_at = db.Column(db.DateTime,default=datetime.now())

class Category(db.Model):
    """
    """
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    created_at = db.Column(db.DateTime,default=datetime.now())
    updated_at = db.Column(db.DateTime,default=datetime.now())

class Stock(db.Model):
    """
    """
    id = db.Column(db.Integer,primary_key=True)
    product_id = db.Column(db.Integer,db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer,nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.now())
    updated_at = db.Column(db.DateTime,default=datetime.now())

#Schema es para serializar los datos a una forma manipulable por python
class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:#Meta es información adicional para python
        model = Category
        fields = ["id","name"]#Para que muestre solo los campos que se quieran

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product

def get_all_categories():
    categories = Category.query.all()#query select *from category
    category_schema = CategorySchema()#Definiendo el esquema para serializar
    categories = [category_schema.dump(category) for category in categories]#Poner información en arreglo
    return categories

def get_all_products():

    products = Product.query.all()#query select *from product 
    product_schema = ProductSchema()#Lo formatea como un objeto
    produs = [product_schema.dump(product) for product in products]
    return produs

def create_new_category(name):
    """
    """
    category = Category(name=name)
    db.session.add(category)#Método de flask para insertar

    if db.session.commit():
        return category
    
    return None

def create_new_product(name,price,weight,description,refundable,category_id):
    """
    """
    category = Category.query.filter(id==category_id)

    if category != [] :
        producto = Product(name=name,price=price,weight=weight,description=description,refundable=refundable,category_id=category_id)
        db.session.add(producto)

        if db.session.commit():
            return producto


    return None


def get_product_by_id(id):
    product_qs = Product.query.filter_by(id=id).first()
    product_schema = ProductSchema()
    p = product_schema.dump(product_qs)
    return p

