import requests
import json
from hashlib import sha1
from .utils.Validator import PhoneNumberValidator
from .utils._Pwsha1 import pwhash


def LoginInput(ID, PW) -> dict:
    return Login(access_token=GetAccessToken(ID=PhoneNumberValidator(numberi=ID), PW=pwhash(arg=PW)))

def GetAccessToken(ID: str, PW: str) -> str:
    """
    ```
    Host: api.bunjang.co.kr
    User-Agent: Mozilla/5.0 (Linux; Android 10.0.0; SM-F700NZPAKOO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36
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
        "User-Agent": "Mozilla/5.0 (Linux; Android 10.0.0; SM-F700NZPAKOO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36",
        "Content-Type": "application/json;charset=utf-8",
        "Origin": "https://m.bunjang.co.kr"
    }
    return requests.post(url, json=loginPayload, headers=headers, verify=False).json()["access_token"]

def Login(access_token):
    """
    ```http
    Host: api.bunjang.co.kr
    User-Agent: Mozilla/5.0 (Linux; Android 10.0.0; SM-F700NZPAKOO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36
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
        "User-Agent": "Mozilla/5.0 (Linux; Android 10.0.0; SM-F700NZPAKOO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36",
        "Content-Type": "application/json;charset=utf-8",
        "Origin": "https://m.bunjang.co.kr",
        "Connection": "keep-alive",
        "Referer": "https://m.bunjang.co.kr/",
        "TE": "Trailers"
    }
    request = requests.Session()
    return request.post(url=url, json=loginPayload, headers=headers, verify=False).json()
    
