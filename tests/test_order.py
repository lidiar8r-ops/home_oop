import pytest

from src.myexception import MyException
from src.order import Order


def test_order_product(order1) -> None:
    assert str(order1) == "заказ товара Samsung Galaxy S23 Ultra в количестве 10 шт., итоговая стоимость = 1800000.0"


def test_order_add_product(order1, product_one) -> None:
    order1.add_product(product_one)
    assert str(order1) == ("заказ товара Samsung Galaxy S23 Ultra в количестве 15 шт., итоговая стоимость = 2700000.0")


def test_order_add_other_product(order1, product_two) -> None:
    with pytest.raises(TypeError, match="В заказе может быть указан только один товар"):
        order1.add_product(product_two)

    with pytest.raises(TypeError, match="Можно складывать только объекты класса Product или его наследников"):
        order1.add_product("Not a product")

    with pytest.raises(TypeError, match="В заказе может быть указан только один товар"):
        order1 = Order("Iphone 15", 10, 15_000.0)


def test_order_add_empty_product():
    with pytest.raises(MyException):
        order1 = Order("Samsung Galaxy S23 Ultra", 0, 180000.0)
