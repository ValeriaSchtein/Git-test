from dataclasses import dataclass
from dotenv import load_dotenv
import os

# Загружаем переменные окружения из файла .env
load_dotenv()


@dataclass
class Settings:
    """
    Настройки приложения.

    dataclass — простой способ хранить связанные данные.
    """

    bot_token: str


def get_settings() -> Settings:
    """
    Возвращает объект настроек.

    Здесь мы читаем переменную окружения BOT_TOKEN.
    Если токен не найден — сразу даём понятную ошибку.
    """
    bot_token = os.getenv("BOT_TOKEN")

    if not bot_token:
        raise ValueError(
            "Не найден BOT_TOKEN. "
            "Создайте файл .env в корне проекта и добавьте строку BOT_TOKEN=..."
        )

    return Settings(bot_token=bot_token)

