import logging
import json
import numba
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from app.login import LoginInput
from app.findv2 import Product, Price, JsonData, dataL, productImg, location
from app.ncov19 import nCov19
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

@numba.jit(nopython=True, parallel=True)
@dp.message_handler(commands=['최저가'])
async def chlwjrrk(message: types.Message):
    data = JsonData()
    a = Product(o=dataL(JsonData=data))
    b = Price(l=dataL(JsonData=data))
    c = productImg(i=dataL(JsonData=data))
    d = location(x=dataL(JsonData=data))
    loop = len(a)
    for x in range(loop):
        await message.reply(text=f"{a[x]}   {b[x]} \n  {c[x]}  \n {d[x]}")

@numba.jit(nopython=True, parallel=True)
@dp.message_handler(commands=['코로나', 'ncov', '코로나19'])
async def ncov(message: types.Message):
    data = nCov19()
    db = data.InfectiousDisease()
    length = len(db)
    for i in range(length):
        await message.reply(text=db[i])



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)