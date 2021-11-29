# Archivo para creacion de excepciones personalizadas

class PathNotFoundError(Exception):
    pass


class MethodNotAllowedError(Exception):
    pass


class NotInstanceSimpleHttpRequest(Exception):
    pass
