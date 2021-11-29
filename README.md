# habi_test
Prueba Tecnica Habi

Servicio de consulta
* Los usuarios pueden consultar los inmuebles con los estados: “pre_venta”, “en_venta” y “vendido” (los inmuebles con estados distintos nunca deben ser visibles por el usuario).
* Los usuarios pueden filtrar estos inmuebles por: Año de construcción, Ciudad, Estado.
* Los usuarios pueden aplicar varios filtros en la misma consulta.
* Los usuarios pueden ver la siguiente información del inmueble: Dirección, Ciudad, Estado, Precio de venta y Descripción.

- Tecnologias a usar:
  - jsonschema==3.2.0 -> "Para validaciones en la entrada de los datos"
  - mysqlclient -> "Para manejo de conecciones y consultas a la base de datos"
  - pytest -> "Pruebas unitarias"
  - http.server -> "liberia nativa de Python para manejo de peticiones HTTP"
  - traceback -> "libreria nativa de Python para visualizar en consola la traza de las excepciones"
  - logging -> "liberia nativa de Python para imprimir log de registros en consola"  
  - socketserver -> "Un framework para servidores de red de Python"

