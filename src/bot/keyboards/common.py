"""
Модуль с общими клавиатурами бота.

Здесь мы описываем, какие кнопки показывать пользователю.
"""

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_keyboard() -> ReplyKeyboardMarkup:
    """
    Создаёт основную клавиатуру с кнопками.

    Для простоты делаем две кнопки с командами:
    /start и /help. При нажатии просто отправляется текст
    команды, и срабатывают уже существующие обработчики.
    """
    keyboard = [
        [
            KeyboardButton(text="/start"),
            KeyboardButton(text="/help"),
        ]
    ]

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,  # клавиатура подстраивается под экран
        one_time_keyboard=False,  # не скрывать клавиатуру после нажатия
    )

