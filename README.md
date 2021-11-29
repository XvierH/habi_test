# habi_test
Prueba Tecnica Habi

# Servicio de consulta
* Los usuarios pueden consultar los inmuebles con los estados: “pre_venta”, “en_venta” y “vendido” (los inmuebles con estados distintos nunca deben ser visibles por el usuario).
* Los usuarios pueden filtrar estos inmuebles por: Año de construcción, Ciudad, Estado.
* Los usuarios pueden aplicar varios filtros en la misma consulta.
* Los usuarios pueden ver la siguiente información del inmueble: Dirección, Ciudad, Estado, Precio de venta y Descripción.

# Tecnologias a usar:
  - jsonschema==3.2.0 -> "Para validaciones en la entrada de los datos"
  - mysqlclient -> "Para manejo de conecciones y consultas a la base de datos"
  - pytest -> "Pruebas unitarias"
  - http.server -> "liberia nativa de Python para manejo de peticiones HTTP"
  - traceback -> "libreria nativa de Python para visualizar en consola la traza de las excepciones"
  - logging -> "liberia nativa de Python para imprimir log de registros en consola"  
  - socketserver -> "Un framework para servidores de red de Python"

## Steps
* Para iniciarl el servidor, se debe ejecutar primero la funcion main.py
* Para consumir el servicio 
  * La ruta http://0.0.0.0:PORT/property  (PORT esta por defecto en el puerto 8094 si se quiere modificar editar la variable SERVER_PORT en el archivo de constans.py)
  * El método Http de consumo es POST

* _year_: año de construccion del inmueble
* _city_: ciudad de ubicacion del inmueble
* _state_: estado del inmueble

    **Ejemplo:**

    ```json
    {
      "state": 3,
      "city": "bogota",
      "year": "2011"
    }
    ```

## Notas
* las propiedades mostradas en el json no son obligatorias
* para realizar la peticion sin datos como minimo se debe enviar el json vacio {}
* En caso de no cumplir con las condiciones del esquema _json_ presentado anteriormente, la función devolverá un código de estado 400 (Bad Request).
  * _year_ (string, must be in the format yyyy and between 1900 - 2099)
  * _city_ (string, minimo de un caracter).
  * _state_ (number, el numero debe ser 3,4 o 5)
* Si el _json_ contiene propiedades adicionales a las presentadas anteriormente, la función devolverá un código de estado 400 (Bad Request).


## Variables de entorno

* **DBNAME**: Nombre de la base de datos.
* **DBUSER**: Nombre del usuario de la base de datos.
* **DBPASSWORD**: Clave de acceso a la base de datos.
* **DBPORT**: Puerto disponible de la base de datos.
* **DBHOST**: Direccion de host donde se encuentra alojada la base de datos 


## Modelo Segundo servicio

* Primera tabla es la de likes_history 
  * 
  '''
  CREATE TABLE `like_history` (
      `id` <integer>,
      `user_id` <integer>,
      `property_id` <integer>,
      `update_date` <datetime>
    );
  '''
* Segunda table tabla de user
  '''
  CREATE TABLE `user` (
    `id` <integer>,
    `firstname` <varchar>,
    `lastname` <varchar>,
    `username` <varchar>,
    `created_date` <datetime>,
    `password` <ty# habi_test
Prueba Tecnica Habi

# Servicio de consulta
* Los usuarios pueden consultar los inmuebles con los estados: “pre_venta”, “en_venta” y “vendido” (los inmuebles con estados distintos nunca deben ser visibles por el usuario).
* Los usuarios pueden filtrar estos inmuebles por: Año de construcción, Ciudad, Estado.
* Los usuarios pueden aplicar varios filtros en la misma consulta.
* Los usuarios pueden ver la siguiente información del inmueble: Dirección, Ciudad, Estado, Precio de venta y Descripción.

# Tecnologias a usar:
  - jsonschema==3.2.0 -> "Para validaciones en la entrada de los datos"
  - mysqlclient -> "Para manejo de conecciones y consultas a la base de datos"
  - pytest -> "Pruebas unitarias"
  - http.server -> "liberia nativa de Python para manejo de peticiones HTTP"
  - traceback -> "libreria nativa de Python para visualizar en consola la traza de las excepciones"
  - logging -> "liberia nativa de Python para imprimir log de registros en consola"  
  - socketserver -> "Un framework para servidores de red de Python"

## Steps
* Para iniciarl el servidor, se debe ejecutar primero la funcion main.py
* Para consumir el servicio 
  * La ruta http://0.0.0.0:PORT/property  (PORT esta por defecto en el puerto 8094 si se quiere modificar editar la variable SERVER_PORT en el archivo de constans.py)
  * El método Http de consumo es POST

* _year_: año de construccion del inmueble
* _city_: ciudad de ubicacion del inmueble
* _state_: estado del inmueble

    **Ejemplo:**

    ```json
    {
      "state": 3,
      "city": "bogota",
      "year": "2011"
    }
    ```

## Notas
* las propiedades mostradas en el json no son obligatorias
* para realizar la peticion sin datos como minimo se debe enviar el json vacio {}
* En caso de no cumplir con las condiciones del esquema _json_ presentado anteriormente, la función devolverá un código de estado 400 (Bad Request).
  * _year_ (string, must be in the format yyyy and between 1900 - 2099)
  * _city_ (string, minimo de un caracter).
  * _state_ (number, el numero debe ser 3,4 o 5)
* Si el _json_ contiene propiedades adicionales a las presentadas anteriormente, la función devolverá un código de estado 400 (Bad Request).


## Variables de entorno

* **DBNAME**: Nombre de la base de datos.
* **DBUSER**: Nombre del usuario de la base de datos.
* **DBPASSWORD**: Clave de acceso a la base de datos.
* **DBPORT**: Puerto disponible de la base de datos.
* **DBHOST**: Direccion de host donde se encuentra alojada la base de datos 


## Modelo Segundo servicio

* Primera tabla es la de likes_history

  CREATE TABLE `like_history` (
      `id` <integer>,
      `user_id` <integer>,
      `property_id` <integer>,
      `update_date` <datetime>
      PRIMARY KEY (`id`),
      UNIQUE KEY `like_history_id_uindex` (`id`),
      KEY `like_history_property_id_fk` (`property_id`),
      KEY ` like_history_user_id_fk` (`user_id`),
      CONSTRAINT `like_history_property_id_fk` FOREIGN KEY (`property_id`) REFERENCES `property` (`id`),
      CONSTRAINT `like_history_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
  );

* Segunda table tabla de user

    CREATE TABLE `user` (
      `id` <integer>,
      `firstname` <varchar>,
      `lastname` <varchar>,
      `username` <varchar>,
      `created_date` <datetime>,
      `password` <varchar>,
      `email` <varchar>
  );

  * Se propone este modelo ya que la relacion que existiria entre las propiedades y los likes es de uno a muchos asi como de usuarios a likes, ya que los usuarios pueden darle like a distintas propiedades 
  * El modelo se puede ver en el archivo Diagrama_prueba_habi.png en este repositorio

## Oportunidades de Mejora
* Se pueden realizar vistas en la base de datos con la informacion filtrada para optimizar los tiempos de las consultas
* Se puede retornar el año en el servicio de consulta de propiedades ya que este dato es opcional para las consultas pero parece importante para el usuario


