#import library
from main import bot, dp
from aiogram import types
from aiogram.types import Message

keyboard_markup = types.ReplyKeyboardMarkup(row_width=2)

#Send message to admin
async  def send_to_admin(dp):
    await bot.send_message(chat_id=833156204, text="Bot start")

#Start bot using func
@dp.message_handler(commands=['start'])
async def send_welcome(message:types.Message):
    text = f"Асаламалекум🫡, {message.from_user.full_name}, " \
      f"факт: работа программиста и шамана имеет много общего - оба бормочут непонятные слова, совершают непонятные действия и не могут объяснить, как оно работает."
    await message.answer(text=text)

array_keyboard = ['Button1', 'Button2']

# Send message to admin
async def send_to_admin(dp):
    await bot.send_message(chat_id=833156204, text="Bot start")

# Function of start bot
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard_markup.add(*(types.KeyboardButton(text) for text in array_keyboard))
    await message.answer(text='Hello', reply_markup=keyboard_markup)

