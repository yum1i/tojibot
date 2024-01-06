import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram import types
from aiogram import F
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from aiogram import Router
import keyboards

my_router = Router(name=__name__)

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6861161340:AAH-65tGo2DNLbXKBQyFLrj1G39jyfp7IJg")
dp = Dispatcher()


@my_router.message()
async def message_handler(message: types.Message):
    if message.text.lower == 'toji':
        await message.answer('I am here!')



@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"Привет, <b>{message.from_user.full_name}</b>",
        parse_mode=ParseMode.HTML,
        reply_markup=keyboards.kb
    )

    
@dp.message()
async def echo(message: Message):
    msg = message.text
    if msg == "📚 Учиться":
        await message.answer("Каналы для начинающих", reply_markup=keyboards.kb_link)

    elif msg == "Discord и TikTok 💻":
        await message.answer("Переходите по ссылке ниже", reply_markup=keyboards.link)



@dp.message(F.new_chat_members)
async def somebody_added(message: Message):
    for user in message.new_chat_members:
        await message.reply(f"Привет {user.full_name}, я 𝙏𝙤𝙟𝙞 𝘽𝙊𝙏")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


