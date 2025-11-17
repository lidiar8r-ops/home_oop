import pytest
from unittest.mock import patch

from src.product import Product


def test_product(product_one):
    assert product_one.name == "Samsung Galaxy S23 Ultra"
    assert product_one.description == "256GB, Серый цвет, 200MP камера"
    assert product_one.price == 180000.0
    assert product_one.quantity == 5


def test_product_new_product():
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5

def test_product_price(capsys, product_one):
    Product("55\" QLED 4K", "Фоновая подсветка", -133000.0, 3)
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": -10,
         "quantity": 5})
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    product_one.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    product_one.price = -100
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product_one.price == 180000.0

    product_one.price = 180001
    assert product_one.price == 180001


def test_product_quantity(capsys):
    Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": -5})
    message = capsys.readouterr()
    assert message.out.strip() == "Количество товара не должно быть отрицательным"


def test_product_addition(capsys, category_one):
    Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 190000.0,
         "quantity": 5}, category_one.get_product_list())
    message = capsys.readouterr()
    assert (message.out.strip() == "Товар Samsung Galaxy S23 Ultra уже существует. Объединяем данные...\n"
                                   "Цена обновлена до 190000.0 руб.")


@patch('builtins.input', return_value='y')
def test_price_decrease_accepted(capsys, product_two):
    """Тест: понижение цены, пользователь ввёл 'y' → цена меняется."""
    # Пытаемся понизить цену с 210_000
    product_two.price = 80000.0
    assert product_two.price == 80000.0