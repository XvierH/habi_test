from jsonschema import Draft7Validator
from constants import SCHEMA, BAD_REQUEST, OK
from handlers.log_handler import *
import MySQLdb
import json
import os
from models.property import Property

# Funcion que valida el json de entrada con el esquema alojado en archivo constants.py
def __validate_json(payload):
    validator = Draft7Validator(SCHEMA)
    validation_errors = sorted(validator.iter_errors(payload), key=lambda e: e.path)

    errors = []

    for error in validation_errors:
        message = error.message
        if error.path:
            if error.validator == 'pattern' and 'year' in error.path:
                message = "Date must be in the format yyyy and between 1900 - 2099"
            message = "[{}] {}".format(".".join(str(x) for x in error.absolute_path), message)
        errors.append(message)
    return errors

# Funcion que se encarga de manejar los datos de la peticion y dar respuesta de acuerdo a la consulta
def get_properties(payload):
    response = {
        'errors': [],
        'data': [],
        'success': False
    }

    validation_messages = __validate_json(payload)
    if len(validation_messages) > 0:
        response['errors'].append(validation_messages)
        str_response = json.dumps(response)
        log_handler('ERROR', str_response)
        return BAD_REQUEST, str_response

    with MySQLdb.connect(host=os.environ['DBHOST'], user=os.environ["DBUSER"],
                         passwd=os.environ["DBPASSWORD"], db=os.environ["DBNAME"],
                         port=int(os.environ["DBPORT"])) as client:

        sql = get_sql(payload)
        cursor = client.cursor()
        cursor.execute(sql)

        records = cursor.fetchall()
        quantity = len(records)

        for address, city, state, price, description in records:
            item_property = Property(address, city, state, price, description)
            response['data'].append(item_property.get_dict_property())
        response['success'] = True
        response['quantity'] = quantity
        str_response = json.dumps(response)
        log_handler('INFO', str_response)

    return OK, str_response

# Funcion que se ncarga de generar el sql de acuerdo a
# los datos que llegan de la peticion para aplicar los filtros conrrespondientes
def get_sql(payload):
    sql = "SELECT p.address ,p.city ,s.name ,p.price ,p.description " \
          "FROM property p, status_history sh, status s " \
          "WHERE p.id = sh.property_id AND sh.status_id = s.id " \
          "AND sh.id = (SELECT MAX(id) FROM status_history sh2 WHERE sh2.property_id=p.id) "

    if 'state' not in payload:
        sql += "AND s.id IN (3,4,5)"
    for name, value in payload.items():
        if name == 'state':
            sql += f' AND s.id = {value}'
        else:
            sql += f' AND p.{name} = "{value}"'
    log_handler('INFO', sql)
    return sql
