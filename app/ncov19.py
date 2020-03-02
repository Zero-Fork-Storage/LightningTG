import requests
import json

class nCov19:
    def __init__(self):
        self.headers = {
            "Host": "m.search.naver.com",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10.0.0; SM-F700NZPAKOO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Referer": "https://m.search.naver.com/search.naver?sm=mtp_hty.top&where=m&query=%EC%BD%94%EB%A1%9C%EB%82%98",
            "TE": "Trailers"
        }
        self.url = "https://m.search.naver.com/p/csearch/content/nqapirender.nhn"
        self.payload = {
            "where": "m",
            "pkid": "9005",
            "key": "regionAPI",
            "sort": "sort_1",
            "direction": "desc",
            "u1": "13867393"
        }

    def InfectiousDisease(self):
        NaverApi = requests.get(url=self.url, params=self.payload, headers=self.headers).json()
        data = NaverApi['result']['regions']
        length = len(data)
        ID = []
        for i in range(length):
            ID.append(f"지역: {data[i]['title']} 확진환자수: {str(data[i]['count'])}, 비율: {str(data[i]['rate'])}")
        return ID
    

