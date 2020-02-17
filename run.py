import logging
import json
import numba
from aiogram import Bot, Dispatcher, executor, types
from app.login import LoginInput



with open('conf.json') as conf:
    data: dict = json.load(conf)
    Token: str = data['Telegram']['Token']


API_TOKEN = Token
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@numba.jit(nopython=True, parallel=True)
@dp.message_handler(commands=['ping'])
async def ping(message: types.Message):
    await message.reply("pong!")

@numba.jit(nopython=True, parallel=True)
@dp.message_handler(commands=['login'])
async def LightningLogin(message: types.Message):
    args = message.get_args()
    if args:
        try:
            ID = args.split(' ')[0]
            PW = args.split(' ')[1]
            Credentials = LoginInput(ID=ID, PW=PW)
            json_loginPayload = json.dumps(Credentials, indent=4, ensure_ascii=False)
            await message.reply(json_loginPayload)
        except Exception as LoginError:
            print(str(LoginError))
            await message.reply(str(LoginError))
    else:
        await message.reply("Error")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)