from src.product import Product


class Category:
    # название
    name: str
    # описание
    description: str
    #список товаров категории
    products : List[Product]

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
