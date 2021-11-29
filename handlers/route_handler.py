from constants import ROUTES
from errors.errors import *


# Clase para identificar las rutas habilitadas en el servidor
class RouteHandler:

    def __init__(self, path='', method=''):
        self.path = path[1:]
        self.method = method
        is_valid_path = self.__validate_path()
        if not is_valid_path:
            raise PathNotFoundError(f'the route {self.path} not found')
        is_valid_method = self.__validate_method()
        if not is_valid_method:
            raise MethodNotAllowedError(f'the method {self.method} is not allowed for this route')

    def __validate_path(self):
        exist = False
        for path, method in ROUTES.items():
            if self.path == path:
                exist = True
        return exist

    def __validate_method(self):
        exist = False
        for path, methods in ROUTES.items():
            for method in methods:
                if self.method == method:
                    exist = True
        return exist
