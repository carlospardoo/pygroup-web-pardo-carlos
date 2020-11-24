"""
Consulta método render_template

Método utilizado para renderizar como salida de una ruta, una plantilla 
(página web) almacenada en un archivo. Flask utiliza por defecto el motor 
de plantillas jinja2.

Argumentos: 
    Nombre de la plantilla.
    Variables dinámicas enviadas como argumentos adicionales.

render_template ingresará a la carpeta templates y buscará la plantilla.
Si la aplicación es un módulo, la carpeta templates irá al lado del módulo.
    /aplicacion.py
    /templates
        /hello.html
Si la aplicación es un paquete, la carpeta templates irá dentro del paquete.
    /aplicacion
        /__init__.py
        /templates
            /hello.html

El método render_template se importa de la siguiente manera:
    from flask import render_template

Se utiliza así:
    @render.route("/")
    def ejemplo():
        variable = [7,4,3,2]
        return render_template("hola.html",vars=variable)
"""

from flask import Blueprint, Response, request, render_template, redirect, url_for

from products.models import get_all_categories, create_new_category, get_all_products, create_new_product, get_product_by_id

from products.forms import CreateCategoryForm

prods = Blueprint('prods',__name__,url_prefix='/prod')#estos nombre de rutas son ignorados

#Estándares de nuestro proyecto
EMPTY_SHELVE_TEXT = "Empty shelve!"
PRODUCTS_TITLE = "<h1> Products </h1>"
DUMMY_TEXT = "Dummy method to show how Response works"
RESPONSE_BODY = {
    "message": "",
    "data": [],
    "errors": [],
    "metadata": []
}

@prods.route('/<name>',methods=['GET'])
def tareaVistas(name):
    
    """
    Description:    
        Method assembled for the homework \"Tarea Vistas en Proyecto Flask\", 
        where the server will guarantee a successful response if the 
        parameter is different of \"pygroup\".

    params:
        name:   Parameter given by the web page.

    return: 
        Response    200 The name is suitable for a successful execution.
                    400 The selected name was pygroup, which was unvalid. 

    """
    if name != 'pygroup':
        return Response('Felicitaciones! Trabajo exitoso {}'.format(name),status=200)
    else:
        return Response('Error! No se puede utilizar el nombre pygroup',status=400)

@prods.route('/categories')
def get_categories():
    """
    
    """
    categories=get_all_categories()
    RESPONSE_BODY["message"] = "OK"
    RESPONSE_BODY["data"] = categories

    return RESPONSE_BODY, 200

@prods.route('/add-category',methods=["POST"])
def addCategory():
    """
    
    """
    if request.method=="POST":
        data = request.json
        category = create_new_category(data["name"])

        RESPONSE_BODY["message"] = "Category Created"
        return RESPONSE_BODY, 201
        #return Response("Category created",status=201)#Manera alterna de responder

@prods.route('/productlist',methods=["GET"])
def get_products():
    """
    
    """
    productos = get_all_products()
    RESPONSE_BODY["data"] = productos
    RESPONSE_BODY["message"] = "Products list"

    return RESPONSE_BODY, 200

@prods.route('/add-product',methods=["POST"])
def addProduct():
    """
    
    """
    if request.method == "POST" :
        data = request.json
        create_new_product(data["name"],data["price"],data["weight"],data["description"],data["refundable"],data["category_id"])

        RESPONSE_BODY["message"] = "Producto creado"
        return RESPONSE_BODY, 200
    RESPONSE_BODY["message"] = "Datos mal recibidos"
    return RESPONSE_BODY, 400

@prods.route('/search-product/<int:id>',methods=["GET"])
def buscarProducto(id):
    """
    
    """
    product = get_product_by_id(id)

    RESPONSE_BODY["data"] = product
    RESPONSE_BODY["message"] = "Producto encontrado"

    return RESPONSE_BODY,200

@prods.route('/success')
def categoria_exitosa():
    """
    
    """
    return render_template('category_success.html')

@prods.route('/create_category_form',methods=['GET','POST'])
def create_category_form():
    """
    """
    form_category = CreateCategoryForm()

    if request.method == 'POST' and form_category.validate():
        create_new_category(name=form_category.name.data)
        return redirect(url_for('prods.categoria_exitosa'))

    return render_template('create_category_form.html',form=form_category)

