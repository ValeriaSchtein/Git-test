from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from ..services.text import build_chatgpt_message


# Отдельный роутер для команды /chatgpt
router = Router()


@router.message(Command("chatgpt"))
async def cmd_chatgpt(message: Message) -> None:
    """
    Обработчик команды /chatgpt.

    Пока просто отправляет текст-заглушку из сервисного слоя.
    """
    await message.answer(build_chatgpt_message())

