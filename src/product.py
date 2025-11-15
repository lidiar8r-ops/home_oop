class Product:
    """
    Представляет товар в ассортименте.
    Атрибуты:
        name (str): Название товара (например, «Смартфон Xiaomi 13»).
        description (str): Подробное описание товара.
        price (float): Цена за единицу в рублях (должно быть ≥ 0).
        quantity (int): Количество единиц на складе (должно быть ≥ 0).
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Создаёт экземпляр товара.
        Args:
            name (str): Название товара. Должно быть непустым.
            description (str): Описание товара.
            price (float): Цена за единицу. Должно быть ≥0.
            quantity (int): Количество на складе. Должно быть ≥0
        """
        self.name = name
        self.description = description
        if  price < 0 :
            price = 0
            print("Цена не должна быть нулевая или отрицательная")
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для price."""
        return self.__price

    @price.setter
    def price(self, price):
        """Сеттер для price: проверяет, что цена ≥ 0."""
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif price <= self.__price:
            if input("Цена товара понижается. При согласии понизить цену введите y(значит yes) или n (значит no)?") == 'y':
                self.__price = price
        else:
            self.__price = price
        return self.__price

    @classmethod
    def new_product(cls, product: dict) -> None:
        """
        Создаёт объект продукта из словаря, корректируя отрицательные цены.
        :param product: словарь с данными продукта (обязательно: name, price)
        :return: экземпляр cls (например, Product)
        """
        # Валидация и коррекция данных
        if product.get("price") is not None and product["price"] < 0:
            product["price"] = 0
            print("Цена не должна быть нулевая или отрицательная")
        # Создание и возврат объекта класса
        return cls(**product)
