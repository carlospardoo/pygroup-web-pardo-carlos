from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange, TextAreaField

class CreateCategoryForm(FlaskForm):
    """
    Define los campos que deberia tener el formulario y las validaciones 
    que estos deben tener
    """
    #Crea un input type text, que dice Name y requiere tener datos (validador DataRequired())
    name = StringField('Name',validators=[DataRequired()])

class CreateProductForm(FlaskForm):
    nombre = StringField('txtNombre',validators=[DataRequired()])
    precio = IntegerField('txtPrecio',validators=[DataRequired(), NumberRange(min=0)])
    peso = IntegerField('txtPeso',validators=[NumberRange(min=1)])
    descripcion = TextAreaField('txtDescripcion')

