"""
Consulta método render_template

"""

from flask import Blueprint, Response

prods = Blueprint('prods',__name__,url_prefix='/prod')

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


