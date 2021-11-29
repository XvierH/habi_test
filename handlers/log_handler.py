import logging
from constants import TYPE_ERRORS_LOGGER

logger = logging.getLogger()
logger.setLevel(logging.INFO)


# Funcion para manejo de log de registros en la aplicacion
def log_handler(severity='INFO', messagge=''):
    name_function = next((name_function for sev, name_function in TYPE_ERRORS_LOGGER.items() if sev == severity), None)
    logger_func = 'logger.' + name_function
    eval(logger_func)(messagge)

