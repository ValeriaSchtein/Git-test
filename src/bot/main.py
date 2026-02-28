import asyncio
import logging

from aiogram import Bot, Dispatcher

from .config import get_settings
from .routers import all_routers


async def main() -> None:
    """
    Главная асинхронная функция.

    Здесь происходит:
    1. Настройка логирования (видно, что делает бот).
    2. Загрузка настроек (в том числе токена).
    3. Создание объектов Bot и Dispatcher.
    4. Подключение роутеров с обработчиками.
    5. Запуск long polling — ожидание сообщений от Telegram.
    """
    # Включаем базовое логирование в консоль
    logging.basicConfig(level=logging.INFO)

    # Загружаем настройки (в том числе BOT_TOKEN)
    settings = get_settings()

    # Создаём объект бота и диспетчер
    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()

    # Подключаем все роутеры с обработчиками
    for router in all_routers:
        dp.include_router(router)

    # Удаляем вебхук (если был) и сбрасываем «зависшие» обновления
    await bot.delete_webhook(drop_pending_updates=True)

    # Запускаем бесконечный опрос Telegram-сервера
    await dp.start_polling(bot)


if __name__ == "__main__":
    # asyncio.run() запускает асинхронную функцию main()
    asyncio.run(main())

