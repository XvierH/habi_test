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
* Si el correo que llega en el cuerpo de la solicitud no se encuentra en la base de datos, la función devolverá un código de estado 404 (Not Found).


## Variables de entorno

* **DBNAME**: Nombre de la base de datos.
* **DBUSER**: Nombre del usuario de la base de datos.
* **DBPASSWORD**: Clave de acceso a la base de datos.
* **DBPORT**: Puerto disponible de la base de datos.
* **DBHOST**: Direccion de host donde se encuentra alojada la base de datos 
