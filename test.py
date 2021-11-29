import pytest
from services.property_service import *

# Archivo para crear los diferentes pruebas unitarias dentro de la aplicacion
def test_sql_get_all_properties():
    sql_all = "SELECT p.address ,p.city ,s.name ,p.price ,p.description " \
              "FROM property p, status_history sh, status s " \
              "WHERE p.id = sh.property_id AND sh.status_id = s.id " \
              "AND sh.id = (SELECT MAX(id) FROM status_history sh2 WHERE sh2.property_id=p.id) " \
              "AND s.id IN (3,4,5)"

    assert (get_sql({})) == sql_all

