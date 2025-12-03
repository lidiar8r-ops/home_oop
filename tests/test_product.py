from unittest.mock import patch

import pytest

from src.product import Product


def test_product(product_one):
    assert product_one.name == "Samsung Galaxy S23 Ultra"
    assert product_one.description == "256GB, Серый цвет, 200MP камера"
    assert product_one.price == 180000.0
    assert product_one.quantity == 5


def test_product_new_product():
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_product_price(capsys, product_one):
    with pytest.raises(TypeError, match="Цена не должна быть нулевая или отрицательная"):
        Product('55" QLED 4K', "Фоновая подсветка", -133000.0, 3)
    # Product('55" QLED 4K', "Фоновая подсветка", -133000.0, 3)
    # message = capsys.readouterr()
    # assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    with pytest.raises(TypeError, match="Цена не должна быть нулевая или отрицательная"):
        Product.new_product(
            {
                "name": "Samsung Galaxy S23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": -10,
                "quantity": 5,
            }
        )
    # message = capsys.readouterr()
    # assert message.out.strip() == ("Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', "
    #                                "180000.0, 5)'\n")+'Цена не должна быть нулевая или отрицательная'

    # with pytest.raises(TypeError, match="Цена не должна быть нулевая или отрицательная"):
    #     product_one.price = 0
    # message = capsys.readouterr()
    # assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    # with pytest.raises(TypeError, match="Цена не должна быть нулевая или отрицательная"):
    #     product_one.price = -100
    # message = capsys.readouterr()
    # assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product_one.price == 180000.0
    product_one.price = 180001
    assert product_one.price == 180001


def test_product_quantity():
    with pytest.raises(TypeError, match="Количество товара не должно быть отрицательным"):
        Product.new_product(
            {
                "name": "Samsung Galaxy S23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": -5,
            }
        )
    # message = capsys.readouterr()
    # assert message.out.strip() == ('Количество товара не должно быть отрицательным\n'
    #                                "Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', "
    #                                "180000.0, 0)'")


def test_product_addition(capsys, category_one):
    Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 190000.0,
            "quantity": 5,
        },
        category_one.get_product_list(),
    )
    message = capsys.readouterr()
    assert (
        message.out.strip() == ("Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', "
                                 "180000.0, 5)'\n"
                                 "Product('Iphone 15', '512GB, Gray space', 210000.0, 8)'\n"
                                 'Товар Samsung Galaxy S23 Ultra уже существует. Объединяем данные...\n'
                                 'Цена обновлена до 190000.0 руб.\n'
                                 "Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', "
                                 "190000.0, 10)'")
    )


@patch("builtins.input", return_value="y")
def test_price_decrease_accepted(capsys, product_two):
    """Тест: понижение цены, пользователь ввёл 'y' → цена меняется."""
    # Пытаемся понизить цену с 210_000
    product_two.price = 80000.0
    assert product_two.price == 80000.0


def test_products_add(product_one, product_two):
    assert product_two + product_one == 2580000.0


def test_product_smarthone(smartphone_one):
    assert smartphone_one.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_one.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_one.price == 180000.0
    assert smartphone_one.quantity == 5
    assert smartphone_one.efficiency == 95.5
    assert smartphone_one.model == "S23 Ultra"
    assert smartphone_one.memory == 256
    assert smartphone_one.color == "Серый"


def test_product_smarthone_add(smartphone_one, smartphone_two):
    smartphone_sum = smartphone_one + smartphone_two
    assert smartphone_sum == 2580000.0


def test_product_grass(grass_one):
    assert grass_one.name == "Газонная трава"
    assert grass_one.description == "Элитная трава для газона"
    assert grass_one.price == 500.0
    assert grass_one.quantity == 20
    assert grass_one.country == "Россия"
    assert grass_one.germination_period == "7 дней"
    assert grass_one.color == "Зеленый"


def test_product_grass_add(grass_one, grass_two):
    grass_sum = grass_one + grass_two
    assert grass_sum == 16750.0


def test_product_smarthone_add_invalid(smartphone_one, grass_one):
    with pytest.raises(TypeError):
        smartphone_one + grass_one
