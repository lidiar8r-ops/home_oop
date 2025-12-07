from typing import Any, Dict, Self

from src.myexception import MyException
from src.order import BaseCategory
from src.product import Product


class Category(BaseCategory):
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
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        # def __init__(self, name: str, description: str, products: list) -> None:
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
        self.__products = products.copy() if products else []
        if len(products) == 0:
            raise MyException("Товар с нулевым количеством не может быть добавлен")
        # Обновляем статические счётчики
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        count_products = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {count_products} шт."

    @property
    def products(self) -> str:
        """геттер, который будет выводить список товаров в виде строк в формате:
        Название продукта, 80 руб. Остаток: 15 шт.
        #"""
        str_products = ""
        for product in self.__products:
            str_products += str(product) + "\n"
        return str_products

    def add_product(self, product: Product) -> None:
        """
        Добавляет товар в категорию.
        Args:
            product_data: Словарь с данными товара (name, price, description, quantity).
        """
        try:
            if product.quantity == 0:
                raise MyException("Товар с нулевым количеством не может быть добавлен")
        except MyException as e:
            print(e)

        if not isinstance(product, Product):
            raise TypeError("Можно складывать только объекты класса Product или его наследников")

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
        Category.product_count = len(self.__products)

    def get_product_list(self) -> list[Product]:
        # def get_product_list(self) -> list:
        """Возвращает список объектов Product для внутренней работы."""
        return self.__products

    # @classmethod
    def middle_price(self) -> list[Product]:
        product_cost = sum(product.price for product in self.get_product_list())
        try:
            return round(product_cost / Category.product_count, 2)
        except ZeroDivisionError:
            return 0.0

class ProductIterator:
    def __init__(self, category: Category):
        self.category = category
        self.index = 0

    def __iter__(self) -> Self:
        # def __iter__(self):
        self.index = 0
        return self

    def __next__(self) -> Product:
        products = self.category.get_product_list()
        if self.index >= len(products):
            raise StopIteration
        product = products[self.index]
        self.index += 1
        return product
