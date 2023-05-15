from aiogram import Dispatcher, Bot, types
from local_config import token
from data.db import Database
import os

path = os.getcwd() + "/data/database.db"
token = token
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
db = Database(path)
