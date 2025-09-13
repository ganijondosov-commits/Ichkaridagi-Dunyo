import logging
from aiogram import Bot, Dispatcher, executor, types
import os

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN o'rnatilmagan!")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Assalomu, hamma! Men 24/7 ishlaydigan botman 🤖")

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    text = "/start — botni boshlash\n/help — yordam\n/echo <matn> — yozganingni qaytarish"
    await message.answer(text)

@dp.message_handler(commands=['echo'])
async def echo_command(message: types.Message):
    args = message.get_args()
    if args:
        await message.answer(args)
    else:
        await message.answer("Matn yozmadingiz!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


---

2. requirements.txt

aiogram==2.25.1
python-dotenv
