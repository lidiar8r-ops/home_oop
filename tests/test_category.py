import pytest

from src.category import Category
from src.myexception import MyException
from src.product import Product


def test_category(category_one, product_two, product_three):
    assert category_one.name == "Смартфоны"
    assert (
        category_one.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category_one.products) == 95
    assert category_one.category_count == 1
    assert category_one.product_count == 2

    category_one.add_product(product_two)
    assert category_one.product_count == 2

    category_one.add_product(product_three)
    assert category_one.product_count == 3


def test_category_str(category_one):
    assert str(category_one) == "Смартфоны, количество продуктов: 13 шт."


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(product_iterator).name == "Iphone 15"

    with pytest.raises(StopIteration):
        next(product_iterator)


def test_category_add_product_invalid(category_one):
    with pytest.raises(TypeError):
        category_one.add_product("Not a product")


def test_category_add_empty_product():
    with pytest.raises(MyException):
        Category("Пустая категория", "Категория без продуктов", [])


def test_category_midle_price(category_one):
    assert category_one.middle_price() == 35454.55


def test_category_midle_price_ZeroDivisionError():
    # никогда не случиться данная ситуация, тк идет проверка на добавление не пустого товара
    with pytest.raises(MyException):
        category_empty = Category("Пустая категория", "Категория без продуктов", [])
        category_empty.middle_price()

