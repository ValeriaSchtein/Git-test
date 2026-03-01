from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from ..services.text import build_image_message


# Отдельный роутер для команды /image
router = Router()


@router.message(Command("image"))
async def cmd_image(message: Message) -> None:
    """
    Обработчик команды /image.

    Сейчас это заглушка, которая отправляет статичный текст.
    """
    await message.answer(build_image_message())

