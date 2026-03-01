"""Тесты для модуля конфигурации config."""

import os

import pytest

from src.bot.config import Settings, get_settings


def test_get_settings_returns_settings_with_bot_token(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """
    Если переменная окружения BOT_TOKEN установлена,
    функция должна вернуть объект Settings с этим токеном.
    """
    test_token = "TEST_BOT_TOKEN"
    # Подменяем переменную окружения только в рамках этого теста
    monkeypatch.setenv("BOT_TOKEN", test_token)

    settings = get_settings()

    assert isinstance(settings, Settings)
    assert settings.bot_token == test_token


def test_get_settings_raises_value_error_when_bot_token_missing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """
    Если BOT_TOKEN не установлен,
    должна быть выброшена понятная ошибка ValueError.
    """
    # Удаляем переменную окружения, если она была установлена
    monkeypatch.delenv("BOT_TOKEN", raising=False)

    with pytest.raises(ValueError) as exc_info:
        get_settings()

    # В тексте ошибки должно быть упоминание BOT_TOKEN,
    # чтобы разработчику было проще понять причину.
    assert "BOT_TOKEN" in str(exc_info.value)

