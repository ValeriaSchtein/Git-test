import asyncio

from .main import main


if __name__ == "__main__":
    # Позволяет запустить бота командой:
    # python -m src.bot
    asyncio.run(main())

