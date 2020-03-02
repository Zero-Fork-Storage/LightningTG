import requests
import json

def JsonData():
    app = requests.get("http://api.bunjang.co.kr/api/1/find_v2.json?f_category_id=600700&page=0&order=price_asc&request_id=2020227164235&stat_uid=8781372&stat_device=w&n=100&version=4")
    return app.json()['list']


def listappend(JsonData):
    for i in range(len(JsonData)):
        price = JsonData[i]['price']
        name = JsonData[i]['name']
        if (price == '0') == True:
            del price, name
        else:
            x = str(name), int(price)
            yield x

def dataL(JsonData):
    data = []
    for i in listappend(JsonData):
        data.append(i)
    data.sort(key=lambda element : element[1])
    dp = []
    for px in data:
        dp.append(px)
    return dp

def Product(o):
    product = []    
    for p in o:
        print(p)
        product.append(p[0])
    return product

def Price(l):
    price = []
    for pr in l:
        price.append(pr[1])
    return price


    


 