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
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
