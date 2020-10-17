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
    git push 
 ```

8. Clonando repositorio.

```
    git clone 
 ```
