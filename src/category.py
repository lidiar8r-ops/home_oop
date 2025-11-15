from src.product import Product


class Category:
    """
    Представляет категорию товаров .
    Класс отслеживает:
    - название и описание категории;
    - список входящих в неё товаров (объектов Product);
    - общее количество созданных категорий (статический счётчик);
    - общее количество товаров во всех категориях (статический счётчик).
    Атрибуты:
        name (str): Название категории (например, «Смартфоны»).
        description (str): Подробное описание категории.
        products (list[Product]): Список товаров, относящихся к категории.
        Category_count (int): Статический счётчик — общее число созданных категорий.
            Инициализируется 0, увеличивается на 1 при создании каждого экземпляра.
        product_count (int): Статический счётчик — суммарное количество товаров
            во всех категориях. Увеличивается на длину списка `products` при создании
            экземпляра.
    """

    name: str
    description: str
    products: list[Product]
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """
        Инициализирует категорию с заданным названием, описанием и списком товаров.
        При создании экземпляра:
        - увеличивает статический счётчик `Category_count` на 1;
        - увеличивает статический счётчик `product_count` на количество товаров в `products`.
        Args:
            name (str): Название категории. Должно быть непустой строкой.
            description (str): Описание категории.
            products (list[Product]): Список объектов Product, входящих в категорию.
                Может быть пустым списком.
        """
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        # Обновляем статические счётчики
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self) -> list[Product]:
        str_products = ""
        for product in self.__products:
            str_products += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return  str_products # Название продукта, 80 руб. Остаток: 15 шт.

    def add_product(self, product: list) -> None:
        self.__products.append(product)
        Category.product_count += 1





