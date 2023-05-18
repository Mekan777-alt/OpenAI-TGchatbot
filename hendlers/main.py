from config import dp, db
from aiogram import types
from aiogram.types import ContentType


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    chat_id = db.fetchone("SELECT id FROM users WHERE chat_id = ?", str(message.chat.id),)
    if chat_id != message.chat.id:
        db.query("INSERT INTO users VALUES (NULL, ?, ?, ?, ?, ?, NULL, NULL)",
                 (str(message.chat.id),
                  str(message.date),
                  message.chat.username if message.chat.username else "-",
                  message.chat.first_name if message.chat.first_name else "-",
                  message.chat.last_name if message.chat.last_name else "-",
                  ))
    await message.answer("""Приветствую ✌

Я - ChatGPT, крупнейшая языковая модель, созданная OpenAI. 

Я разработана для обработки естественного языка и могу помочь вам ответить на вопросы, 
обсудить темы или предоставить информацию на различные темы.

🔥В том числе на русском языке🔥

👇Я постараюсь ответить на твои вопросы👇
""")


@dp.message_handler(content_types=ContentType.TEXT)
async def text(message: types.Message):
    pass
