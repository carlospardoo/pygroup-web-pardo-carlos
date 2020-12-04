from flask_wtf import FlaskForm
from wtforms import (
    StringField, 
    IntegerField, 
    TextAreaField, 
    SelectField, 
    SubmitField
    )
from wtforms.validators import DataRequired, NumberRange

class CreateCategoryForm(FlaskForm):
    """
    Define los campos que deberia tener el formulario y las validaciones 
    que estos deben tener
    """
    #Crea un input type text, que dice Name y requiere tener datos (validador DataRequired())
    name = StringField('Name',validators=[DataRequired()])

class CreateProductForm(FlaskForm):
    nombre = StringField('Nombre: ',validators=[DataRequired()])
    precio = IntegerField('Precio: ',validators=[DataRequired(), NumberRange(min=0)])
    peso = IntegerField('Peso: ',validators=[NumberRange(min=1)])
    descripcion = TextAreaField('Descripción: ')
    reembolso = SelectField('Reembolso: ',choices=[('true','Si'),('false','No')])
    categoria = SelectField('Categorías: ',choices=[])
    agregar = SubmitField('Agregar Producto')

