from .echo import router as echo_router
from .start import router as start_router
from .help import router as help_router

# Список всех роутеров бота.
# Здесь собираем обработчики команд и сообщений.
all_routers = [
    start_router,
    help_router,
    echo_router,
]

