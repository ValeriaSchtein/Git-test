"""Тесты для обработчиков (роутеров) aiogram.

Здесь мы не запускаем настоящий Telegram, а подменяем объект Message
простым «фейковым» классом с методом answer.
"""

import asyncio
from typing import Any, Dict, List, Optional

from aiogram.types import ReplyKeyboardMarkup

from src.bot.routers.start import cmd_start
from src.bot.routers.help import cmd_help
from src.bot.routers.echo import echo_handler
from src.bot.routers.chatgpt import cmd_chatgpt
from src.bot.routers.image import cmd_image
from src.bot.routers.history import cmd_history
from src.bot.services.text import (
    build_start_message,
    build_help_message,
    build_echo_reply,
    build_chatgpt_message,
    build_image_message,
    build_history_message,
)


class DummyMessage:
    """Простой заменитель aiogram.types.Message для тестов.

    Мы храним только то, что нам важно:
    - текст входящего сообщения (text)
    - список ответов, которые «отправил» обработчик.
    """

    def __init__(self, text: Optional[str] = None) -> None:
        self.text = text
        self.answers: List[Dict[str, Any]] = []

    async def answer(
        self, text: str, reply_markup: Optional[ReplyKeyboardMarkup] = None
    ) -> None:
        """Сохраняем параметры вызова answer в список для последующих проверок."""
        self.answers.append({"text": text, "reply_markup": reply_markup})


def test_cmd_start_sends_start_message_with_keyboard() -> None:
    """Обработчик /start должен отправлять приветственный текст и клавиатуру."""
    message = DummyMessage()

    # Запускаем асинхронную функцию через asyncio.run
    asyncio.run(cmd_start(message))  # type: ignore[arg-type]

    assert len(message.answers) == 1
    answer = message.answers[0]

    # Текст должен совпадать с тем, что генерирует сервис
    assert answer["text"] == build_start_message()
    # Должна быть отправлена клавиатура
    assert isinstance(answer["reply_markup"], ReplyKeyboardMarkup)


def test_cmd_help_sends_help_message_without_keyboard() -> None:
    """Обработчик /help должен отправлять help-текст без клавиатуры."""
    message = DummyMessage()

    asyncio.run(cmd_help(message))  # type: ignore[arg-type]

    assert len(message.answers) == 1
    answer = message.answers[0]

    assert answer["text"] == build_help_message()
    # В help-команде мы не ожидаем отдельную клавиатуру
    assert answer["reply_markup"] is None


def test_echo_handler_sends_echo_text() -> None:
    """Эхо-обработчик должен отправлять текст, сформированный сервисом."""
    user_text = "Текст для эхо"
    message = DummyMessage(text=user_text)

    asyncio.run(echo_handler(message))  # type: ignore[arg-type]

    assert len(message.answers) == 1
    answer = message.answers[0]

    # Проверяем, что используется сервисная функция build_echo_reply
    assert answer["text"] == build_echo_reply(user_text)
    # В эхо-обработчике мы не отправляем клавиатуру
    assert answer["reply_markup"] is None


def test_cmd_chatgpt_sends_placeholder_text() -> None:
    """Обработчик /chatgpt должен отправлять текст-заглушку из сервиса."""
    message = DummyMessage()

    asyncio.run(cmd_chatgpt(message))  # type: ignore[arg-type]

    assert len(message.answers) == 1
    answer = message.answers[0]

    assert answer["text"] == build_chatgpt_message()
    assert answer["reply_markup"] is None


def test_cmd_image_sends_placeholder_text() -> None:
    """Обработчик /image должен отправлять текст-заглушку из сервиса."""
    message = DummyMessage()

    asyncio.run(cmd_image(message))  # type: ignore[arg-type]

    assert len(message.answers) == 1
    answer = message.answers[0]

    assert answer["text"] == build_image_message()
    assert answer["reply_markup"] is None


def test_cmd_history_sends_placeholder_text() -> None:
    """Обработчик /history должен отправлять текст-заглушку из сервиса."""
    message = DummyMessage()

    asyncio.run(cmd_history(message))  # type: ignore[arg-type]

    assert len(message.answers) == 1
    answer = message.answers[0]

    assert answer["text"] == build_history_message()
    assert answer["reply_markup"] is None

