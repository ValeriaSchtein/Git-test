from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from ..services.text import build_start_message
from ..keyboards import get_main_keyboard

# Отдельный роутер для команды /start
router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message) -> None:
    """Приветственное сообщение при команде /start.

    Эту функцию можно воспринимать как «обработчик события»:
    когда пользователь отправляет команду /start, aiogram вызывает её.
    """
    await message.answer(
        build_start_message(),
        reply_markup=get_main_keyboard(),
    )

