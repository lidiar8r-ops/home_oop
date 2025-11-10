import os

from src.config import DATA_DIR
from src.utils import read_products_from_json


def test_read_products_from_json():
    path_file = os.path.abspath(os.path.join(DATA_DIR,"products.json"))
    result = read_products_from_json(path_file)

    # Выводим первую категорию
    first_category = result[0]
    assert first_category.name == "Смартфоны"

    # Выводим список продуктов в первой категории
    products_in_category = first_category.products
    assert [p.name for p in products_in_category] == ['Samsung Galaxy C23 Ultra', 'Iphone 15', 'Xiaomi Redmi Note 11']

    # Выводим первый продукт из первой категории
    first_product = products_in_category[0]
    assert first_product.name == "Samsung Galaxy C23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"


def test_read_products_from_json_raises():
    path_file = os.path.abspath(os.path.join(DATA_DIR,"pr.json"))
    result = read_products_from_json(path_file)
    assert result == []
