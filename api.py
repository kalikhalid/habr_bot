from bs4 import BeautifulSoup
from config import *
import requests
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.mes

if __name__ == "__main__":
    executor.start_polling(dp)