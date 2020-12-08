# Pygroup Web
El presente repositorio contendrá todos los talleres solicitados para el grupo de trabajo universitario pygroup web.

## Pre-requisitos
1. Sistema operativo Windows 10 o basado en linux apto para descargar la última versión de python. En mi caso utilizo un sistema operativo Windows 7, que no es apto para descargar la última versión de python.

2. Instalación de python 3.9 para trabajar entornos virtuales de la manera dictada en el curso. En mi caso utilizo python 3.7.9, que posee comandos un tanto diferentes.

Python posee instaladores de diferentes versiones para diferentes sistemas operativos y en múltiples formatos en su página web.

3. Un IDE para facilitar el uso de python. En mi caso utilizo Visual Studio Code.

Visual Studio Code puede ser instalado desde internet.


## Versionado
Utilizo Git a través de GitHub para el manejo de las versiones.

Mi cuenta de GitHub es https://github.com/carlospardoo

El nombre del repositorio es pygroup-web-pardo-carlos y se encuentra disponible en https://github.com/carlospardoo/pygroup-web-pardo-carlos

## Autores
Carlos Pardo

## Talleres

### 1. Hola_Mundo_Test - Taller creación de primer entorno virtual y repositorio en GitHub
Taller para aprender como crear primer entorno virtual de python y para aprender uso básico de git a través de GitHub.

#### Instalación

##### Creando entorno virtual

1. Instalar paquete del entorno virtual. Se mostrarán los comandos para versiones de python 3.7.9 y 3.9.

* python 3.7.9:
```
    pip3 install virtualenv
 ``` 

 * python 3.9:
```
    pip install venv
 ``` 

 2. Crear directorio **test** de entorno virtual. Se mostrarán los comandos para versiones de python 3.7.9 y 3.9.

* python 3.7.9:
```
    python -m virtualenv test
 ``` 

 * python 3.9:
```
    python -m venv test
 ``` 

 3. Activar entorno virtual. Se mostrarán los comandos para Sistemas Operativos Windows y Linux.

* Windows:
```
    test\Scripts\activate
 ``` 

 * Linux:
```
    source venv/bin/activate
 ``` 

Una vex hecho esto, aparecerá al inicio de la línea en la consola, el nombre de la carpeta que contiene el entorno virtual.

4. Instalación de paquete de prueba en el entorno virtual.

* Se crea un archivo que contendrá los paquetes a instalar con sus respectivas versiones. En este caso se creó el archivo **requirements.txt** que contiene lo siguiente:

```
    Flask==1.1.2
 ``` 

Se puede apreciar el paquete a instalar con su respectiva versión.

* En el entorno virtual se procede a instalar los paquetes definidos en el archivo con el siguiente comando:

```
    pip install -r requirements.txt
 ``` 

5. Desactivar entorno virtual.

```
    deactivate
 ``` 

Con ello se cierra el entorno virtual y la consola vuelve a su estado base.

#### Ejecutando las pruebas

1. Se verifica que el usuario definido en Git Bash sea correcto.

```
    git config --global user.name
 ``` 

2. Se verifica que el correo definido en Git Bash sea correcto.

```
    git config --global user.email
 ``` 

3. Se ejecuta el siguiente comando antes y después de instalar los paquetes sobre el entorno virtual para comprobar que fue modificado.

```
    pip list
 ``` 

#### Construido con

* [virtualenv] - Utilizado para crear entornos virtuales de python.

* [Flask] - Paquete agregado para probar el entorno virtual.

#### Versionado - Comandos básicos de Git utilizados

1. Definiendo usuario en el GitBash

```
    git config --global user.name "Carlos Pardo"
 ``` 

2. Definiendo correo en el Git Bash. Tener en cuenta que se utiliza un correo proporcionado por GitHub, más no el propio correo.

```
    git config --global user.email "28719833+carlospardoo@users.noreply.github.com"
 ``` 

3. Creando repositorio. Ubicarse en el directorio pygroup-web-pardo-carlos y escribir:

```
    git init
 ```

4. Revisando el estado actual del repositorio (archivos agregados, sin agregar y modificados del repositorio).

```
    git status
 ```

5. Agregando todos los archivos al repositorio.

```
    git add .
 ```

6. Creando un commit.

```
    git commit -m "Creación del repositorio. Agregado taller de la
primera sesion"
 ```

7. Haciendo un push sobre el repositorio.

```
    git push https://github.com/carlospardoo/pygroup-web-pardo-carlos.git
 ```

8. Clonando repositorio.

```
    git clone 
 ```

### 2. Semana2-HTTP - Investigación HTTP

Ivestigación referente a los tipos de peticiones de HTTP y los códigos de respuesta HTTP.

### 3. Tarea Vistas en Proyecto Flask

Taller donde se cargará en el navegador un mensaje u otro según el parámetro dado. Consulta adicional sobre el método render_template.

#### Instalación

1. Dirigirse a la carpeta **proyecto_flask** con el siguiente comando.

```
cd proyecto_flask
```
2. Ejecutar el siguiente comando para iniciar el entorno virtual **env**.

```
env\Scripts\activate
```
3. Si es la primera vez que se ejecuta el entorno virtual, instalar paquetes especificados en requirements.txt. en caso contrario, omitir este paso.

```
pip install -r requirements.txt
```

4. Iniciar la ejecución del proyecto con el siguiente comando.

```
python app\__init__.py
```

#### Despliegue

Cuando inicia la aplicación aparece la ruta por defecto donde correrá.

```
Running on http://127.0.0.1:5000/
```

Sin embargo, al cargar dicha ruta en el navegador no aparecerá nada. Ello es porque no se ha configurado ninguna vista para ser cargada en la ruta principal.

Para correr el taller se debe utilizar la siguiente ruta.

```
http://127.0.0.1:5000/prod/carlos
```
El taller correrá en la ruta prod seguido de cualquier nombre especificado (en este caso es **carlos**, pero puede ser cualquier otro nombre).

#### Ejecutando las pruebas

1. Cuando se carga la ruta con cualquier nombre como parámetro diferente de pygroup, por ejemplo **carlos** aparecerá el siguiente mensaje.

```
Felicitaciones! Trabajo exitoso carlos
```

2. Cuando se carga la ruta con el nombre **pygroup**, aparecerá el siguiente mensaje.

```
Error! No se puede utilizar el nombre pygroup
```

### 4. Tarea Formularios

1) Completar vista de registrar Stock (Métodos PUT y POST) que está en el repositorio marcada con un comentario TO-DO
2) Generar dos formularios para la creación de un producto en la tienda:
    a. Un formulario regular sin usar ninguna extensión de Flask
    b. Un formulario usando Flask-WTF con validadores de los campos y mensajes de error.

#### Instalación

1. Instalar paquetes: Ejecutar archivo requirements.txt para instalar paquetes requeridos con el siguiente comando.

```
pip install -r requirements.txt
```

2. Migraciones: Para las migraciones se utilizaron los siguientes comandos.

* Comando utilizado para crear directorio de migraciones. No volver a utilizar.

```
python app\__init__.py db init
```

El comando de flask es el siguiente.

```
flask db init
```

* Comando utilizado para crear una migración, definiendo los cambios a realizar sobre la base de datos.

```
python app\__init__.py db migrate -m "Mensaje"
```

El comando de flask es el siguiente.

```
flask db migrate -m "Mensaje"
```

* El comando para confirmar e implementar los cambios en la base de datos es el siguiente.

```
flask db upgrade
```

El comando de flask es el siguiente.

```
python app\__init__.py db upgrade
```

* Se debe tener en cuenta que se definió el método create_migrations() en el **__init__.py** para ejecutar migraciones. Sin embargo, debido a los conflictos de ejecución provocados por la librería que implementa, lo mejor es utilizarlo únicamente cuando se desee hacer una migración.

#### Ejecutando las pruebas

1. El primer punto de la tarea fue implementado en el método **register_product_refund_in_stock(id)** de views.py en el módulo products. Puede ser verificado en Postman o Imsomnia. Probado en Postman.

2. 
- Formulario sin uso de extensiones de flask puede ser accedido mediante la siguiente ruta.

```
http://localhost:5000/products/create-product-old-form
```

- Formulario que implementa Flask-WTF puede ser accedido mediante la siguiente ruta.

```
http://localhost:5000/products/create-product-wtf-form
```

Ambos formularios pueden ser implementados. Sin embargo, la carga y envío de las imágenes no se encuentra implementado.

#### Despliegue

1. Corriendo servidor y : Debido a que tengo problemas con las variable de entorno de flask, utilizo en mi máquina comandos de python para la ejecución. Sin embargo, se desconoce si los comandos de flask se pueden implementar apropiadamente.

#### Construido con

1. **flask-marshmallow** versión 0.14.0
2. **Flask-SQLAlchemy** versión 2.4.4
3. **marshmallow** versión 3.9.0
4. **marshmallow-sqlalchemy** versión 0.24.0
5. **six** versión 1.15.0
6. **SQLAlchemy** versión 1.3.20
7. **Flask-Migrate** versión 2.5.3
8. **Flask-WTF** versión 0.14.3
9. **Flask-Script** versión 2.0.6
