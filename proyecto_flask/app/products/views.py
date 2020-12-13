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

from products.models import (
    get_all_categories, 
    create_new_category, 
    get_all_products, 
    create_new_product, 
    get_product_by_id, 
    create_new_stock,
    update_stock
)

from products.forms import CreateCategoryForm, CreateProductForm

from http import HTTPStatus

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

@prods.route('/add-category-old',methods=["GET","POST"])
def addCategoryOld():
    """
    """

    if request.method == 'POST':
        create_new_category(request.form["txtNombre"])
        RESPONSE_BODY["data"] = request.form["txtNombre"]
        RESPONSE_BODY["message"] = 'Se agregó la categoría {} con éxito'.format(request.form["txtNombre"])
        
        return RESPONSE_BODY, 200
    return render_template('category_old_form.html')

@prods.route("/register-product-stock/<int:id>", methods=["PUT", "POST"])
def register_product_refund_in_stock(id):

    # TODO Complete this view to update stock for product when a register for
    # this products exists. If not create the new register in DB
    status_code = HTTPStatus.CREATED
    if request.method == "PUT":
        data = request.json
        stock = update_stock(id,data["product_id"],data["quantity"])
        #RESPONSE_BODY["data"] = stock
        RESPONSE_BODY["message"] = \
            "Stock for this product were updated successfully!"
        status_code = HTTPStatus.OK
    elif request.method == "POST":
        data = request.json
        #print('Datos: product id:'+str(id)+', quantity: '+str(data["quantity"]))
        stock = create_new_stock(
            id,
            data["quantity"]
        )

        #RESPONSE_BODY["data"] = stock

        RESPONSE_BODY["message"] = "Stock for this product were created successfully!"
        #pass
        #return RESPONSE_BODY, HTTPStatus.CREATED
    else:
        RESPONSE_BODY["message"] = "Method not Allowed"
        status_code = HTTPStatus.METHOD_NOT_ALLOWED
    
    return RESPONSE_BODY, status_code

@prods.route('/create-product-old-form',methods=["GET","POST"])
def create_new_product_old_form():
    """
    """
    if request.method == "POST":
        #print('code for post')
        data = request.form
        #print(data)
        reembol = False
        #print(data["cmbReembolso"])
        #print(type(data["txtNombre"]))
        if data["cmbReembolso"] == 'true':
           reembol = True
        producto = create_new_product(
                str(data["txtNombre"]),
                int(data["txtPrecio"]),
                int(data["txtPeso"]),
                str(data["txtDescripcion"]),
                reembol,
                int(data["cmbCategoria"])
                )

        RESPONSE_BODY["data"] = producto
        RESPONSE_BODY["message"] = "Producto creado"
        return RESPONSE_BODY, 201
    return render_template('create_product_simple.html')

@prods.route('/create-product-wtf-form',methods=["GET","POST"])
def create_new_product_wtf_form():
    """
    """
    form_product = CreateProductForm()

    if request.method == "POST" :
        # print('code for post')
        # #data = request
        # print(type(form_product.nombre.data))
        # print(type(form_product.precio.data))
        # print(type(form_product.peso.data))
        # print(type(form_product.descripcion.data))
        # print(type(form_product.reembolso.data))
        # print(type(form_product.categoria.data))
        #print(form_product)
        reembol = False
        #print(data["cmbReembolso"])
        #print(type(form_product.categoria.data))
        if form_product.reembolso.data == 'true':
           reembol = True
        # print(type(form_product.categoria.data))
        validado = form_product.validate()
        #print('validado?: '+str(validado))
        if form_product.validate():
            
            
            #data = request.json
            create_new_product(
                form_product.nombre.data,
                form_product.precio.data,
                form_product.peso.data,
                form_product.descripcion.data,
                reembol,
                form_product.categoria.data
                )

            RESPONSE_BODY["message"] = "Producto creado"
            return RESPONSE_BODY, 201
        #print(form_product.errors)
        RESPONSE_BODY["message"] = "Datos mal recibidos"
        return RESPONSE_BODY, 400
    categories = get_all_categories()
    #print(categories[0]['name'])
    cats_formato = []
    for temporal in categories:
        cats_formato.append((str(temporal['id']),temporal['name']))
    form_product.categoria.choices = cats_formato
    return render_template('create_product_new.html',formul=form_product)

#<input type="hidden" name="csrf_token" value="{{ csrf_token() }}">

@prods.route('/show-catalog',methods=["GET"])
def show_products_catalog():
    """
    1. Consultar la BD y extraer todos los productos disponibles
    2. Almacenar la información en una variable de contexto
    3. Renderizar la plantilla que tengamos en HTML e insertar los datos
    de nuestra variable de contexto
    """
    #1.
    products = get_all_products()
    #2.
    my_info = {"productos":products,"pygroup":"Pygroup hoy","carlos":1598}
    return render_template('catalog.html',my_info=my_info)

