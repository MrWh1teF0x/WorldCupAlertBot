import asyncio
import logging
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "👋 Привет! Я бот для WorldCupAlert!\n\n"
        "Доступные команды:\n"
        "/start - показать это сообщение\n"
        "/help - помощь\n"
        "/setavatar - установить аватар (для админа)"
    )


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "📖 Помощь по боту:\n\n"
        "Я умею отвечать на команды и менять аватар.\n"
        "Просто напиши мне что-нибудь!"
    )


@dp.message()
async def echo(message: types.Message):
    """
    Отвечает на все остальные сообщения
    """
    await message.answer(f"Вы сказали: {message.text}")


async def main():
    print("🤖 Бот запущен и готов к работе!")
    print("Нажмите Ctrl+C для остановки")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Бот остановлен")
