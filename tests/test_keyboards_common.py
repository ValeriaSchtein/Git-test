"""Тесты для модуля клавиатур common."""

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from src.bot.keyboards import get_main_keyboard


def test_get_main_keyboard_returns_reply_keyboard_markup() -> None:
    """Функция должна возвращать объект ReplyKeyboardMarkup."""
    keyboard = get_main_keyboard()

    assert isinstance(keyboard, ReplyKeyboardMarkup)


def test_get_main_keyboard_has_expected_buttons() -> None:
    """
    Основная клавиатура должна содержать нужные кнопки
    с ожидаемым текстом.
    """
    keyboard = get_main_keyboard()

    # keyboard.keyboard — это список списков кнопок
    all_button_texts = [
        button.text for row in keyboard.keyboard for button in row
    ]

    assert "/help" in all_button_texts
    assert "/chatgpt" in all_button_texts
    assert "/image" in all_button_texts
    assert "/history" in all_button_texts

