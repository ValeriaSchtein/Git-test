"""
Модуль с общими клавиатурами бота.

Здесь мы описываем, какие кнопки показывать пользователю.
"""

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_keyboard() -> ReplyKeyboardMarkup:
    """
    Создаёт основную клавиатуру с кнопками.

    Для простоты делаем набор кнопок с командами:
    /help, /chatgpt, /image, /history.
    При нажатии просто отправляется текст команды,
    и срабатывают уже существующие обработчики (если они есть).
    """
    keyboard = [
        [
            KeyboardButton(text="/help"),
            KeyboardButton(text="/chatgpt"),
        ],
        [
            KeyboardButton(text="/image"),
            KeyboardButton(text="/history"),
        ],
    ]

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,  # клавиатура подстраивается под экран
        one_time_keyboard=False,  # не скрывать клавиатуру после нажатия
    )

