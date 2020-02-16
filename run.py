import logging
import json

from aiogram import Bot, Dispatcher, executor, types


with open('conf.json') as conf:
    data: dict = json.load(conf)
    Token: str = data['Telegram']['Token']


API_TOKEN = Token
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['ping'])
async def ping(message: types.Message):
    await message.reply("pong!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
