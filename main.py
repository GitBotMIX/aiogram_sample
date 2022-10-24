from aiogram.utils import executor
from create_bot import dp, bot
from data_base.sqlite_db import Database
import asyncio


async def start(*args):
    print('DOLJNIK bot start')
    Database.sql_start()


from handlers import authorization
authorization.register_handlers_client(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start)
