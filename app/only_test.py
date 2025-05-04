import asyncio
import logging
from aiogram import F
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.enums.dice_emoji import DiceEmoji
from datetime import datetime

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level = logging.INFO)
# Объект бота
bot = Bot(token = '7500138759:AAHNhDCCjrt9ZRHSBWxIBHlmplNT4lyrS70')
# Диспетчер
dp = Dispatcher()
dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Hello!")

@dp.message(Command("answer"))
async def cmd_answer(message: Message):
    await message.answer("Это простой ответ")

@dp.message(Command("reply"))
async def cmd_reply(message: Message):
    await message.reply('Это ответ с "ответом"')

@dp.message(Command("dice"))
async def cmd_dice(message: Message):
    await message.answer_dice(emoji="🎲")

@dp.message(Command("add_to_list"))
async def cmd_add_to_list(message: Message, mylist: list[int]):
    mylist.append(7)
    await message.answer("Добавлено число 7")

@dp.message(Command("add_to_list"))
async def cmd_add_to_list(message: Message, mylist: list[int]):
    mylist.append(7)
    await message.answer("Добавлено число 7")

@dp.message(Command("show_list"))
async def cmd_show_list(message: Message, mylist: list[int]):
    await message.answer(f"Ваш список: {mylist}")

@dp.message(Command("info"))
async def cmd_info(message: Message, started_at: str):
    await message.answer(f"Бот запущен {started_at}")

# Высылает в чат бота у пользователя id которого указан
#@dp.message(Command("dicer"))
#async def cmd_dice(message: Message, bot: Bot):
#    await bot.send_dice(21153576, emoji=DiceEmoji.DICE)

@dp.message(Command("photo"))
async def cmd_dice(message: Message):
    await message.answer_photo(photo='https://mimigram.ru/wp-content/uploads/2020/07/chto-takoe-foto.jpg')

# вывод сообщения с курсивом
@dp.message(F.text, Command("test"))
async def any_message(message: Message):
    await message.answer(
        "Hello, <b>world</b>!", 
        parse_mode=ParseMode.HTML
    )
    await message.answer(
        "Hello, *world*\!", 
        parse_mode=ParseMode.MARKDOWN_V2
    )

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot, mylist=[1, 2, 3])

if __name__ == "__main__":
    asyncio.run(main())