"""Тесты для сервисного модуля работы с текстами бота."""

from src.bot.services import text


def test_build_start_message_returns_string() -> None:
    """Функция build_start_message должна возвращать непустую строку."""
    message = text.build_start_message()

    assert isinstance(message, str)
    assert message != ""


def test_build_start_message_contains_greeting() -> None:
    """В приветственном сообщении должно быть упоминание приветствия."""
    message = text.build_start_message()

    assert "Привет" in message


def test_build_help_message_contains_commands() -> None:
    """В help-сообщении должны быть перечислены основные команды."""
    message = text.build_help_message()

    assert "/start" in message
    assert "/help" in message


def test_build_echo_reply_returns_same_text() -> None:
    """
    Для обычного текста эхо-ответ должен возвращать
    ровно тот же текст, что и пришёл от пользователя.
    """
    user_text = "Пример текста для эхо"

    reply = text.build_echo_reply(user_text)

    assert reply == user_text


def test_build_echo_reply_increments_integer_number() -> None:
    """Если в эхо приходит целое число, функция должна вернуть число + 1."""
    user_text = "10"

    reply = text.build_echo_reply(user_text)

    assert reply == "11"


def test_build_echo_reply_increments_negative_integer_number() -> None:
    """Если в эхо приходит отрицательное целое число, также увеличиваем его на 1."""
    user_text = "-5"

    reply = text.build_echo_reply(user_text)

    assert reply == "-4"


def test_build_chatgpt_message_contains_keyword() -> None:
    """Текст для /chatgpt должен содержать название команды."""
    message = text.build_chatgpt_message()

    assert "chatgpt" in message.lower()


def test_build_image_message_contains_keyword() -> None:
    """Текст для /image должен содержать название команды."""
    message = text.build_image_message()

    assert "image" in message.lower()


def test_build_history_message_contains_keyword() -> None:
    """Текст для /history должен содержать название команды."""
    message = text.build_history_message()

    assert "history" in message.lower()

