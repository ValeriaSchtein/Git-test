from aiogram import Router, F
from aiogram.types import Message

from ..services.text import build_echo_reply

# Router — объект, который собирает обработчики.
# Потом мы «подключим» его в диспетчер.
router = Router()


@router.message(F.text)
async def echo_handler(message: Message) -> None:
    """
    Эхо-обработчик.

    F.text — фильтр aiogram:
    обработчик срабатывает только на сообщения, где есть текст.
    Бот отправляет пользователю текст, сформированный сервисом.
    """
    reply_text = build_echo_reply(message.text)
    await message.answer(reply_text)

