from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from ..services.text import build_history_message


# Отдельный роутер для команды /history
router = Router()


@router.message(Command("history"))
async def cmd_history(message: Message) -> None:
    """
    Обработчик команды /history.

    В дальнейшем здесь может появиться логика показа истории запросов.
    Пока отправляем текст-заглушку.
    """
    await message.answer(build_history_message())

