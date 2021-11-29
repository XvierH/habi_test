# Modelo usado para encapsular las diferentes propiedades obtenidas de la consulta
class Property:

    address = None
    city = None
    state = None
    price = None
    description = None
    dict_property = None

    def __init__(self, address, city, state, price, description):
        self.state = state
        self.address = address
        self.city = city
        self.price = price
        self.description = description

    def get_dict_property(self):
        self.dict_property = {
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'price': self.price,
            'description': self.description
        }
        return self.dict_property
