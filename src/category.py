from src.product import Product


class Category:
    # название
    name: str
    # описание
    description: str
    #список товаров категории
    products : List[Product]
    count_categories: int
    count_categories = 0
    count_products: int
    count_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.count_categories += 1
        Сategory.count_products += len(products)
