from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class CreateCategoryForm(FlaskForm):
    """
    Define los campos que deberia tener el formulario y las validaciones 
    que estos deben tener
    """
    #Crea un input type text, que dice Name y requiere tener datos (validador DataRequired())
    name = StringField('Name',validators=[DataRequired()])
