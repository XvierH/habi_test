from errors.errors import *
import http.server


# Clase para generar respuesta del servidor
class ResponseHandler:

    @classmethod
    def get_response(cls, simplehttprequest, status_code, response):
        if not isinstance(simplehttprequest, http.server.SimpleHTTPRequestHandler):
            raise NotInstanceSimpleHttpRequest(f'The  class not instance from http.server.SimpleHTTPRequestHandler')
        simplehttprequest.send_response(status_code)
        simplehttprequest.send_header('Content-type', 'text/json')
        simplehttprequest.end_headers()
        simplehttprequest.wfile.write(response.encode('utf-8'))
