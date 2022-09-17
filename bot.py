from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from redactor import photoredactor
from datetime import datetime
from random import choice
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
signs = open('signs.txt', encoding="utf-8").readlines()

# Ответ бота на команду /start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nОтправь мне любое фото")

# Действия бота при отправке пользователем фотографии
@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
    # Присланная пользователем фотография сохраняется в папку userphotos
    # Затем вызывается функция-обработчик фотографий и после завершения ее работы уже измененное фото
    # отправляется обратно пользователю
    dt = datetime.now().strftime("%d-%m-%Y_%H-%M")
    await message.photo[-1].download(destination_file=f'userphotos//{dt}_{message.from_user.id}.jpg')
    await bot.send_message(message.from_user.id, "Обрабатываем ваше фото...")
    photoredactor(f"{dt}_{message.from_user.id}", choice(signs).strip())
    photo = open(f'processedphotos//{dt}_{message.from_user.id}processed.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo)
    await bot.send_message(message.from_user.id, "Поделитесь этой фотографией с друзьями!")


if __name__ == '__main__':
    executor.start_polling(dp)
