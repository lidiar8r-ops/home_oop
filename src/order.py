from abc import ABC, abstractmethod

from src.product import Product


class BaseCategory(ABC):

    @abstractmethod # pragma: no cover
    def add_product(self, product: Product) -> None:
        pass

class Order(BaseCategory):
    NAME_PRODUCT = None
    cost: float

    def __init__(self, product: str, quantity: int, price: float):
        """Создаёт экземпляр купленного  товара.
                       Args:
                           name (str): Название купленного товара. Должно быть непустым.
                           quantity (int): Количество купленного товара. Должно быть ≥0
                           price (float): Цена товара
                       """
        if not Order.NAME_PRODUCT or product in Order.NAME_PRODUCT:
            self.product = product
            self.quantity = quantity
            self.price = price
            Order.NAME_PRODUCT = product
            Order.cost = price * quantity
        else:
            raise TypeError("В заказе может быть указан только один товар")

    def __str__(self):
        return (f"заказ товара {self.product} в количестве {self.quantity} шт., итоговая стоимость = "
                f"{self.price * self.quantity}")


    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно складывать только объекты класса Product или его наследников")

        if not Order.NAME_PRODUCT or product.name in Order.NAME_PRODUCT:
            self.product = product.name
            self.quantity += product.quantity
            Order.cost += product.price * product.quantity
            Order.NAME_PRODUCT = product.name
        else:
            raise TypeError("В заказе может быть указан только один товар")
