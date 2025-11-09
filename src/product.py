
class Product:
    # название
    name : str
    # описание
    description : str
    # цена
    price : float
    # количество в наличии
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
