"""
Пакет с клавиатурами бота.

Сюда можно добавлять разные типы клавиатур:
- обычные (ReplyKeyboardMarkup)
- inline-кнопки (InlineKeyboardMarkup)
"""

from .common import get_main_keyboard

__all__ = ["get_main_keyboard"]

