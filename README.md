# Python, Flask - REST API básico

## Descripción

El siguiente es un ejemplo básico, cuyo objetivo es comprender el concepto de REST API usando Python y su framework web Flask. 

Solo creamos un CRUD en memoria del servidor, basados en los datos del archivo `data.py`. En un caso real, esos datos son reemplazados por aquellos que obtengas de una base de datos. 

## Definiciones

- **REST**: is the acronym for **Representational State Transfer** (Internet Protocol). It is a software architectural style that describes a uniform interface between physically separate components, often across the Internet in a Client-Server architecture.
- **API** is the acronym for **Application Programming Interface**, which is a software intermediary that allows two applications to talk to each other.
- **CRUD** in computer programming, **Create, Read, Update, and Delete** are the four basic operations of persistent storage.
- **RESTful API** is an interface that two computer systems use to exchange information securely over the internet. Most business applications have to communicate with other internal and third-party applications to perform various tasks. REST APIs support this information exchange because they follow secure, reliable, and efficient software communication standards.
- **JSON** is an open standard file format and data interchange format that uses human-readable text to store and transmit data objects consisting of attribute–value pairs and arrays. JSON is an acronym for **JavaScript Object Notation**.

## Métodos HTTP

### GET

Con el método GET obtienes los datos.

En este ejemplo puedes listar toda la tabla, o buscar un registro o columna utilizando el campo `id` o el campo `name`.

    HTTP GET http://127.0.0.1:5000/rest
    HTTP GET http://127.0.0.1:5000/rest/1
    HTTP GET http://127.0.0.1:5000/rest/printer

### POST

Con el método POST puedes agregar una columna.

    HTTP POST http://127.0.0.1:5000/rest

En este caso, deberías enviar en formato JSON los atributos/valor necesarios mediante un cliente REST API.

### PUT

Con el método PUT puedes modificar una columna de la tabla identificada por un `id`.


    HTTP PUT http://127.0.0.1:5000/rest/3

En este caso, deberías enviar en formato JSON los atributos/valor necesarios mediante un cliente REST API

### DELETE

Con el método DELETE puedes eliminar una columna de la tabla identificada por un `id`.
    
    HTTP DELETE http://127.0.0.1:5000/rest/4

## Clientes REST API

Clientes REST API sugeridos: 
- **Postman** 
- **Insomnia**

# Enlaces

[Python](https://www.python.org) | 
[Flask](https://flask.palletsprojects.com/) |



# Muchas Gracias

[Héctor Chocobar Torrejón](http://chocobar.net)

![Avatar de Héctor](https://en.gravatar.com/userimage/146115819/41a333edd75fea5257a0a684c76cf977.png)
