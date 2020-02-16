import telegram

LightningTG_token = ''
LightningTG = telegram.Bot(token=LightningTG_token)
updates = LightningTG.getUpdates()
for u in updates:
    print(u.message)