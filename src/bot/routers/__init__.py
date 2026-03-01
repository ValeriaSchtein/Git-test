from .echo import router as echo_router
from .start import router as start_router
from .help import router as help_router
from .chatgpt import router as chatgpt_router
from .image import router as image_router
from .history import router as history_router

# Список всех роутеров бота.
# Здесь собираем обработчики команд и сообщений.
all_routers = [
    start_router,
    help_router,
    chatgpt_router,
    image_router,
    history_router,
    echo_router,
]

