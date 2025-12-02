import pytest

from src.category import Category, ProductIterator
from src.product import LawnGrass, Product, Smartphone


@pytest.fixture()
def product_one():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def product_two():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture()
def product_three():
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture()
def category_one(product_one, product_two):
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для "
        "удобства жизни",
        products=[product_one, product_two],
    )


@pytest.fixture()
def category_two():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и "
        "помощником",
        products=Product[product_two],
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


@pytest.fixture()
def product_iterator(category_one):
    return ProductIterator(category_one)


@pytest.fixture()
def smartphone_one():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture()
def smartphone_two():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture()
def grass_one():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture()
def grass_two():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
