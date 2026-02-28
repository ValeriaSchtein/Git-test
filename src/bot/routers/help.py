from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from ..services.text import build_help_message

# Отдельный роутер для команды /help
router = Router()


@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    """Ответ на команду /help.

    Здесь мы просто объясняем пользователю, что бот умеет.
    """
    await message.answer(build_help_message())

