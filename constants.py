# Archivo para el manejo de las constantes que se usan dentrp de la aplicacion

SERVER_PORT = 8094

EMPTY_STRING = ''

SCHEMA = {
    'type': 'object',
    'additionalProperties': False,
    'properties': {
        'year': {
            'type': 'string',
            'pattern': '(19|20)\d{2}$'
        },
        'city': {
            'type': 'string',
            "minLength": 1,
        },
        'state': {
            'type': 'number',
            "minLength": 1,
            "enum": [3, 4, 5]
        }
    }
}

TYPE_ERRORS_LOGGER = {
    'INFO': 'info',
    'WARNING': 'warning',
    'ERROR': 'error'
}

NO_CONTENT = 204
NOT_MODIFIED = 304
BAD_REQUEST = 400
NOT_FOUND = 404
CONFLICT = 409
METHOD_NOT_ALLOWED = 405
INTERNAL_SERVER_ERROR = 500
OK = 200

ROUTES = {
    'property': ['POST']
}

