import json
import os
from typing import List

from src import app_logger
from src.category import Category
from src.product import Product

logger = app_logger.get_logger("utils.log")


def read_products_from_json(file_path: str) -> List[Category]:
    """
    Читает JSON‑файл с данными о категориях и товарах, создаёт объекты Category и Product.
    Выполняет валидацию входных данных и обрабатывает возможные ошибки.
    Args:
        file_path (str): Полный путь к JSON‑файлу с данными о категориях и продуктах.
    Returns:
        List[Category]: Список объектов Category, каждый из которых содержит:
            - название, описание категории;
            - список объектов Product (товары).
    """
    # Проверка существования файла
    if not os.path.exists(file_path):
        logger.error(f"Файл не найден: {file_path}")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            json_data = json.load(json_file)
            logger.info(f"Начало чтения файла {file_path}")

            # Проверка на пустоту
            if not json_data:
                logger.error("JSON‑файл пуст")
                return []

            categories = []
            for category in json_data:
                # Проверка наличия обязательных ключей в категории
                if "products" not in category:
                    logger.error(f"Отсутствует ключ 'products' в категории: {category}")
                    return []
                if "name" not in category:
                    logger.error(f"Отсутствует ключ 'name' в категории: {category}")
                    return []

                products = []
                for product in category["products"]:
                    # Проверка наличия обязательных полей в продукте
                    if "name" not in product:
                        logger.error(f"Отсутствует ключ 'name' в продукте: {product}")
                        return []
                    products.append(Product(**product))

                category["products"] = products
                categories.append(Category(**category))

        logger.info(f"Окончание чтения JSON-файла {file_path}")
        return categories

    except json.JSONDecodeError as e:
        logger.error(f"Ошибка парсинга JSON: {e}", e.doc, e.pos)
        return []


# if __name__ == "__main__":
#     path_file = os.path.abspath(os.path.join("..", "data\\products.json"))
#     result = read_products_from_json(path_file)
#
#     # Выводим первую категорию
#     first_category = result[0]
#     print(f"Категория: {first_category.name}")
#
#     # Выводим список продуктов в первой категории
#     products_in_category = first_category.products
#     print(f"Продукты в категории: {[p.name for p in products_in_category]}")
#
#     # Выводим первый продукт из первой категории
#     first_product = products_in_category[0]
#     print(f"Первый продукт: {first_product.name}")
#     print(f"Описание: {first_product.description}")
