import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def protuct_one():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def protuct_two():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture()
def protuct_three():
    return Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)


@pytest.fixture()
def category_one(protuct_one, protuct_two):
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для "
        "удобства жизни",
        products=[protuct_one, protuct_two],
    )


@pytest.fixture()
def category_two():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и "
        "помощником",
        products=Product[protuct_two],
    )


@pytest.fixture()
def VALID_DATA():
    return [
        {
            "name": "Смартфоны",
            "description": "Мобильные устройства",
            "products": [{"name": "Galaxy S23", "price": 79999.99, "quantity": 3}],
        }
    ]


@pytest.fixture()
def data_json():
    return {
        "name": "Смартфоны",
        "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для "
        "удобства жизни",
        "products": [
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5,
            }
        ],
    }


@pytest.fixture()
def missing_products():
    return [{"name": "Без продуктов"}]


@pytest.fixture()
def missing_name_cat():
    return [{"products": []}]


@pytest.fixture()
def missing_name_prod():
    return [{"name": "Электроника", "products": [{"price": 1000}]}]  # нет 'name' у продукта
