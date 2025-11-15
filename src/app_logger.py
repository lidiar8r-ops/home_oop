import logging
import os
from logging import Logger

from src.config import LOG_DIR, LOG_LEVEL, LOG_LEVEL_STREAM, S_LOG_FORMAT


def get_file_handler(name: str) -> logging.FileHandler:
    """
    Создаёт файловый обработчик логов.
    :param name: имя файла лога (без пути)
    :return: экземпляр FileHandler
    """
    file_handler = logging.FileHandler(os.path.join(LOG_DIR, name), mode="w", encoding="utf-8")
    file_handler.setLevel(LOG_LEVEL)
    file_handler.setFormatter(logging.Formatter(S_LOG_FORMAT))
    return file_handler


def get_stream_handler() -> logging.StreamHandler:
    """
    Создаёт обработчик вывода в консоль (только ошибки).
    :return: экземпляр StreamHandler
    """
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(LOG_LEVEL_STREAM)
    stream_handler.setFormatter(logging.Formatter(S_LOG_FORMAT))
    return stream_handler


def get_logger(name: str) -> Logger:
    """
    Создаёт логгер с файловым и консольным обработчиками.
    :param name: имя логгера (обычно __name__ модуля)
    :return: настроеннный экземпляр Logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)

    # Добавляем обработчики
    logger.addHandler(get_file_handler(name))
    logger.addHandler(get_stream_handler())

    return logger
