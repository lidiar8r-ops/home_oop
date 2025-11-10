# Настройки БД
import os
from logging import CRITICAL, INFO

# Пути к файлам
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
LOG_DIR = os.path.join(PARENT_DIR, "logs")
DATA_DIR = os.path.join(PARENT_DIR, "data")
# TEMP_DIR = os.path.join(CURRENT_DIR, "tmp")

# # Логирование
S_LOG_FORMAT: str = "%(asctime)s - [%(levelname)s] - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
LOG_LEVEL = INFO
LOG_LEVEL_STREAM = CRITICAL

# # LOG_FILE = "app.log"
#
# # # Функциональные флаги
# # DEBUG = True
# # ENABLE_CACHING = False
