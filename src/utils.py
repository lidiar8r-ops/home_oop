import json
import os
from typing import List

from src.category import Category
from src.product import Product


def read_products_from_json(file_path: str) -> List[Category]:
    """
    Читает JSON‑файл с данными о категориях и товарах, создаёт объекты Category и Product.

    Выполняет валидацию входных данных и обрабатывает возможные ошибки.

    Args:
        file_path (str): Полный путь к JSON‑файлу с данными о категориях и продуктах.


    Returns:
        List[Category]: Список объектов Category, каждый из которых содержит:
            - название, описание категории;
            - список объектов Product (товары в категории).

    Raises:
        FileNotFoundError: Если файл по указанному пути не найден.
        PermissionError: Если нет прав на чтение файла.
        json.JSONDecodeError: Если содержимое файла не является валидным JSON.
        KeyError: Если в JSON отсутствует ожидаемый ключ (например, "products").
        TypeError: Если данные в JSON не соответствуют ожидаемым типам для создания объектов Product/Category.
        ValueError: Если файл пуст или данные некорректны.


    """
    # Проверка существования файла
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл не найден: {file_path}")

    # Проверка прав на чтение
    if not os.access(file_path, os.R_OK):
        raise PermissionError(f"Нет прав на чтение файла: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            json_data = json.load(json_file)

            # Проверка на пустоту
            if not json_data:
                raise ValueError("JSON‑файл пуст")

            categories = []
            for category in json_data:
                # Проверка наличия обязательных ключей в категории
                if "products" not in category:
                    raise KeyError(f"Отсутствует ключ 'products' в категории: {category}")
                if "name" not in category:
                    raise KeyError(f"Отсутствует ключ 'name' в категории: {category}")

                products = []
                for product in category["products"]:
                    # Проверка наличия обязательных полей в продукте
                    if "name" not in product:
                        raise KeyError(f"Отсутствует ключ 'name' в продукте: {product}")
                    products.append(Product(**product))

                category["products"] = products
                categories.append(Category(**category))

        return categories

    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Ошибка парсинга JSON: {e}", e.doc, e.pos)


if __name__ == "__main__":
    path_file = os.path.abspath(os.path.join("..", "data\\products.json"))
    result = read_products_from_json(path_file)

    # Выводим первую категорию
    first_category = result[0]
    print(f"Категория: {first_category.name}")

    # Выводим список продуктов в первой категории
    products_in_category = first_category.products
    print(f"Продукты в категории: {[p.name for p in products_in_category]}")

    # Выводим первый продукт из первой категории
    first_product = products_in_category[0]
    print(f"Первый продукт: {first_product.name}")
    print(f"Описание: {first_product.description}")
