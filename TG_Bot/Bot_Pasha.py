from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin, other # Импортируем клиенскую, админскую и остальную часть кода


async def on_startup(_): # Сбытие которое должно выполнится 1 раз при запуске
    pass

admin.register_handlers_admins(dp)  # админские функции
client.register_handlers_client(dp)  # клиенские функции
other.register_handlers_other(dp)  # остальные функции


if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True, on_startup=on_startup)  # запуск бота
    except Exception as exc:
        print(exc)

