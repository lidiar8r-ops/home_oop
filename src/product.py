
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
    def new_product(cls, product: dict, products_list: list = []) -> None:
        """
        Если товар с таким же именем уже существует в списке, объединяет их:
        - складывает количество на складе;
        - выбирает максимальную из двух цен.

        :param product: словарь с данными продукта (обязательно: name, price, description, quantity)
        :param products_list: список существующих товаров для проверки дубликатов (опционально)
        :return: экземпляр cls ( Product)
        """
        # Валидация и коррекция данных
        if product.get("price") is not None and product["price"] < 0:
            product["price"] = 0
            print("Цена не должна быть нулевая или отрицательная")

        if product.get("quantity") is not None and product["quantity"] < 0:
            product["quantity"] = 0
            print("Количество товара не должно быть отрицательным")

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
        print(f"Товар '{product['name']}' уже существует. Объединяем данные...")

        # Складываем количество
        find_product.quantity += product["quantity"]

        # Выбираем максимальную цену
        if product["price"] > find_product.price:
            find_product.price = product["price"]
            print(f"Цена обновлена до {find_product.price} руб.")

        return find_product
