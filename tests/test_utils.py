import json
from unittest.mock import MagicMock, mock_open, patch

from src.utils import read_products_from_json


def test_read_products_from_json(data_json):
    # Создаём мок для open
    mock_file = mock_open(
        read_data=json.dumps([data_json])
    )  # Обернули в список, т.к. JSON-файл содержит массив категорий

    # Подменяем builtins.open на наш мок
    with patch("builtins.open", mock_file), patch("os.path.exists", return_value=True):

        # Вызываем тестируемую функцию
        result = read_products_from_json("test.json")

        # Проверяем результат
        assert len(result) == 1
        category = result[0]

        assert category.name == "Смартфоны"
        assert (
            category.description
            == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для "
            "удобства жизни"
        )

        assert category.products == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"

        product = category.get_product_list()[0]
        assert product.name == "Samsung Galaxy C23 Ultra"
        assert product.description == "256GB, Серый цвет, 200MP камера"
        assert product.price == 180000.0
        assert product.quantity == 5

        # Проверяем, что open был вызван с правильными аргументами
        mock_file.assert_called_once_with("test.json", "r", encoding="utf-8")


def test_file_not_found():
    """Тест: файл не существует → возвращается [] и логируется ошибка."""
    with (
        patch("os.path.exists", return_value=False),
        patch("src.utils.logger") as mock_logger,
    ):  # ← Патчим ГЛОБАЛЬНЫЙ logger из utils.py

        mock_error = MagicMock()
        mock_logger.error = mock_error  # Подменяем метод error

        result = read_products_from_json("not_exist.json")

        assert result == []
        assert mock_error.called  # error() был вызван
        assert "Файл не найден" in mock_error.call_args[0][0]


def test_empty_json_file():
    """Тест: JSON-файл пуст → возвращается [] и логируется ошибка."""
    mock_file = mock_open(read_data="[]")

    with (
        patch("os.path.exists", return_value=True),
        patch("builtins.open", mock_file),
        patch("src.utils.logger") as mock_logger,
    ):

        mock_error = MagicMock()
        mock_logger.error = mock_error

        result = read_products_from_json("empty.json")

        assert result == []
        assert mock_error.called, "logger.error() не был вызван"
        assert "JSON‑файл пуст" in mock_error.call_args[0][0], "Неверное сообщение в логе"


def test_json_decode_error():
    """Тест: ошибка парсинга JSON → возвращается [] и логируется ошибка."""
    mock_file = mock_open(read_data="{invalid json}")

    with (
        patch("os.path.exists", return_value=True),
        patch("builtins.open", mock_file),
        patch("src.utils.logger") as mock_logger,
    ):

        mock_error = MagicMock()
        mock_logger.error = mock_error

        result = read_products_from_json("bad.json")

        assert result == []
        assert mock_error.called, "logger.error() не был вызван"
        assert "Ошибка парсинга JSON" in mock_error.call_args[0][0], "Неверное сообщение в логе"


def test_missing_products_key(missing_products):
    """Тест: отсутствует ключ 'products' в категории → возвращается [] и логируется ошибка."""
    mock_file = mock_open(read_data=json.dumps(missing_products))

    with (
        patch("os.path.exists", return_value=True),
        patch("builtins.open", mock_file),
        patch("src.utils.logger") as mock_logger,
    ):

        mock_error = MagicMock()
        mock_logger.error = mock_error

        result = read_products_from_json("missing_products.json")

        assert result == []
        assert mock_error.called, "logger.error() не был вызван"
        assert "Отсутствует ключ 'products'" in mock_error.call_args[0][0], "Неверное сообщение в логе"


def test_missing_name_key_in_category(missing_name_cat):
    """Тест: отсутствует ключ 'name' в категории → возвращается [] и логируется ошибка."""
    mock_file = mock_open(read_data=json.dumps(missing_name_cat))

    with (
        patch("os.path.exists", return_value=True),
        patch("builtins.open", mock_file),
        patch("src.utils.logger") as mock_logger,
    ):

        mock_error = MagicMock()
        mock_logger.error = mock_error

        result = read_products_from_json("missing_name_cat.json")
        assert result == []
        assert mock_error.called, "logger.error() не был вызван"
        assert "Отсутствует ключ 'name' в категории" in mock_error.call_args[0][0], "Неверное сообщение в логе"


def test_missing_name_key_in_product(missing_name_prod):
    """Тест: отсутствует ключ 'name' в продукте → возвращается [] и логируется ошибка."""
    mock_file = mock_open(read_data=json.dumps(missing_name_prod))

    with (
        patch("os.path.exists", return_value=True),
        patch("builtins.open", mock_file),
        patch("src.utils.logger") as mock_logger,
    ):

        mock_error = MagicMock()
        mock_logger.error = mock_error

        result = read_products_from_json("missing_name_prod.json")

        assert result == []
        assert mock_error.called, "logger.error() не был вызван"
        assert "Отсутствует ключ 'name' в продукте" in mock_error.call_args[0][0], "Неверное сообщение в логе"
