import logging
import os
import django
from aiogram import executor

from loader import dp, db

from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    # Уведомляет о запуске
    await on_startup_notify(dispatcher)
    logging.info(f'Создаем подключение...')

    logging.info(f'Подключение успешно!')
    logging.info(f'База загружена успешно!')


def setup_django():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "django_project.telegrambot.telegrambot.settings"
    )
    os.environ.update({'DJANGO_ALLOW_ASYNC_UNSAFE': "true"})
    django.setup()


if __name__ == '__main__':
    setup_django()
    from middlewares.language_middleware import setup_middleware
    setup_middleware(dp)

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
