from services.property_service import *
from handlers.route_handler import *
from handlers.response_handler import *
import traceback


# Clase para el manejo de las peticiones de tipo post en el servidor
class ServerHandler(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):
        # - request -
        content_length = int(self.headers['Content-Length'])
        print('content_length:', content_length)

        if content_length:
            input_json = self.rfile.read(content_length)
            payload = json.loads(input_json)
        else:
            payload = None
        try:
            RouteHandler(self.path, 'POST')
            status_code, response = get_properties(payload)
            ResponseHandler.get_response(self, status_code, response)
        except PathNotFoundError as e:
            traceback.print_exc()
            ResponseHandler.get_response(self, INTERNAL_SERVER_ERROR, str(e))
        except MethodNotAllowedError as e:
            traceback.print_exc()
            ResponseHandler.get_response(self, METHOD_NOT_ALLOWED, str(e))
        except NotInstanceSimpleHttpRequest as e:
            traceback.print_exc()
            ResponseHandler.get_response(self, INTERNAL_SERVER_ERROR, str(e))
        except Exception as e:
            traceback.print_exc()
            ResponseHandler.get_response(self, INTERNAL_SERVER_ERROR, str(e))
