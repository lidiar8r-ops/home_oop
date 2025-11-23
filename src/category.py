from typing import List, Dict, Any

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
        self.__products: list[Product] = []
        self.__products: List[Product] = products.copy() if products else []
        # Обновляем статические счётчики
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        count_products = 0
        for product in self.__products:
            count_products += product.quantity
        return f"{self.name}, количество продуктов: {count_products} шт."

        # goods_count = 0
        # for product in self.__products:
        #     goods_count += product.quantity
        # return f"{self.name}, количество продуктов: {goods_count} шт."
        #
        # for product in self.__products:
        #     str_products += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        # return str_products  # Название продукта, 80 руб. Остаток: 15 шт.

    @property
    def products(self) -> str:
        """геттер, который будет выводить список товаров в виде строк в формате:
        Название продукта, 80 руб. Остаток: 15 шт.
        # """
        str_products = ""
        for product in self.__products:
            str_products += str(product) + "\n"
        return str_products

    def add_product(self, product: list) -> None:
        """
        Добавляет товар в категорию.
        Args:
            product_data: Словарь с данными товара (name, price, description, quantity).
        """
        # Формируем словарь данных из объекта Product
        product_data: Dict[str, Any] = {
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "quantity": product.quantity,
        }

        # Используем new_product для возможного объединения с существующим товаром
        Product.new_product(product_data, self.__products)

        # Если товар новый (не был в списке), увеличиваем счётчик
        # if product not in self.__products:
        # self.__products.append(added_product)
        Category.product_count = len(self.__products)


    def get_product_list(self) -> list[Product]:
        """Возвращает список объектов Product для внутренней работы."""
        return self.__products


class ProductIterator:
    category: Category

    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index + 1 < len(self.category.products[self.index]):
            product = self.category.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
