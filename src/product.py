from abc import ABC, abstractmethod
from typing import Optional

from src.mixins import MixinPrint


class BaseProduct(ABC):
    name: str
    description: str
    quantity: int
    __price: float

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Создаёт экземпляр товара.
        Args:
            name (str): Название товара. Должно быть непустым.
            description (str): Описание товара.
            price (float): Цена за единицу. Должно быть ≥0.
            quantity (int): Количество на складе. Должно быть ≥0
        """
        self.name = name
        self.description = description
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.quantity = quantity
        if price < 0:
            # price = 0
            raise TypeError("Цена не должна быть нулевая или отрицательная")

        self.__price = price
        print(repr(self))

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self) -> float:
        """Геттер для price."""
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        """Сеттер для price: проверяет, что цена ≥ 0."""
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        elif price <= self.__price:
            if (
                input("Цена товара понижается. При согласии понизить цену введите y(значит yes) или n (значит no)?")
                == "y"
            ):
                self.__price = price
        else:
            self.__price = price

    def __add__(self, other: "Product") -> float:
        if type(other) is type(self):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError("можно складывать товары только из одинаковых классов продуктов")

    @classmethod
    @abstractmethod  # pragma: no cover
    def new_product(cls, product: dict, products_list: list = []) -> Optional["Product"]:
        pass


class Product(BaseProduct, MixinPrint):
    """
    Представляет товар в ассортименте.
    Атрибуты:
        name (str): Название товара (например, «Смартфон Xiaomi 13»).
        description (str): Подробное описание товара.
        price (float): Цена за единицу в рублях (должно быть ≥ 0).
        quantity (int): Количество единиц на складе (должно быть ≥ 0).
    """

    @classmethod
    def new_product(cls, product: dict, products_list: list = []) -> Optional["Product"]:
        """
        Создаёт новый продукт или объединяет с существующим по имени (
             - складывает количество на складе;
             - выбирает максимальную из двух цен)

         :param product: словарь с данными продукта ( name, price, description, quantity)
         :param products_list: список существующих товаров для проверки дубликатов (опционально)
         :return: экземпляр cls ( Product)
        """

        # Валидация и коррекция данных
        if product.get("price") is not None and product["price"] < 0:
            # product["price"] = 0
            raise TypeError("Цена не должна быть нулевая или отрицательная")

        if product.get("quantity") is not None and product["quantity"] < 0:
            # product["quantity"] = 0
            raise TypeError("Количество товара не должно быть отрицательным")

        # проверка наличия такого же товара схожего по имени
        # Если список товаров не передан — создаём новый товар без проверок
        if products_list == []:
            return cls(**product)

        # Поиск товара с таким же именем в списке
        find_product = None
        for item in products_list:
            if item.name == product["name"]:
                find_product = item
                break

        # Если товар не найден — создаём новый
        if not find_product:
            new_item = cls(**product)
            products_list.append(new_item)
            return new_item

        # Если товар найден — объединяем данные
        print(f"Товар {product['name']} уже существует. Объединяем данные...")

        # Складываем количество
        find_product.quantity += product["quantity"]

        # Выбираем максимальную цену
        if product["price"] > find_product.price:
            find_product.price = product["price"]
            print(f"Цена обновлена до {find_product.price} руб.")

        return cls(
            name=find_product.name,
            description=find_product.description,
            price=find_product.price,
            quantity=find_product.quantity,
        )


class Smartphone(Product):
    """класс Смартфон. Помимо имеющихся свойств Product есть
    Args:
       efficiency: производительность,
       model: модель,
       memory: объем встроенной памяти,
       color: цвет.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """класс Трава газонная. Помимо имеющихся свойств Product есть
    Args:
        country: страна-производитель,
        germination_period: срок прорастания,
        color: цвет.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
