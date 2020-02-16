import requests
import json
from hashlib import sha1
from utils.Validator import PhoneNumberValidator
from utils._Pwsha1 import pwhash

ID = PhoneNumberValidator(numberi=input("ID :"))
PW = pwhash(arg=input("PW :"))

def GetAccessToken(ID, PW):
    """
    ```
    Host: api.bunjang.co.kr
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0
    Accept: application/json, text/plain, */*
    Accept-Language: ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate, br
    Content-Type: application/json;charset=utf-8
    Content-Length: 123
    Origin: https://m.bunjang.co.kr
    {
        "userid":"전화번호",
        "userpw":"sha1",
        "device":"w",
        "oauth_token":"",
        "join_method":""
    }
    ```
    """
    url = "https://api.bunjang.co.kr/api/1/auth/access_token"
    loginPayload: dict = {
        "userid": ID,
        "userpw": PW,
        "device":"w",
        "oauth_token":"",
        "join_method":""
    }
    headers = {
        "Host": "api.bunjang.co.kr",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0",
        "Content-Type": "application/json;charset=utf-8",
        "Origin": "https://m.bunjang.co.kr"
    }

    resp = requests.post(url, json=loginPayload, headers=headers).json()
    access_token = resp["access_token"]
    return access_token

def Login(access_token):
    """
    ```http
    Host: api.bunjang.co.kr
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0
    Content-Type: application/json;charset=utf-8
    Origin: https://m.bunjang.co.kr
    Connection: keep-alive
    Referer: https://m.bunjang.co.kr/
    TE: Trailers
    {
        "token":"access_token"
    }
    ```
    """
    url = "https://api.bunjang.co.kr/login_with_token"
    loginPayload: dict = {
        "token": access_token
    }
    headers = {
        "Host": "api.bunjang.co.kr",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0",
        "Content-Type": "application/json;charset=utf-8",
        "Origin": "https://m.bunjang.co.kr",
        "Connection": "keep-alive",
        "Referer": "https://m.bunjang.co.kr/",
        "TE": "Trailers"
    }
    request = requests.Session()
    auth = request.post(url=url, json=loginPayload, headers=headers).json()
    return auth

access_token = GetAccessToken(ID=ID, PW=PW)
app = Login(access_token=access_token)
print(app)
