import io
import sys
import json
import requests

class Searcher:
    def __init__(self) -> None:
        self.input: str = None
        self.referer: str = None

    def deal(self, string: str):
        return string.replace(' ','%20')

    def search(self, input, page):
        
        # input = "Sea of problem"
        # referer = 'https://dev.iw233.cn/Music1/?name=Sea%20of%20problems&type=netease'

        self.input = input
        self.referer = 'https://dev.iw233.cn/Music1/?name=' + self.deal(self.input) + '&type=netease'

        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://dev.iw233.cn',
            'Referer': self.referer,
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'input': self.input,
            'filter': 'name',
            'type': 'netease',
            'page': str(page),
        }

        response = requests.post('https://dev.iw233.cn/Music1/', headers=headers, data=data)
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
        search_list = json.loads(response.content.decode('gbk', 'ignore'))['data']
        print("------------------------- Page " + str(page) + " -------------------------")
        for index in search_list:
            print("NAME: " + str(index['title']) + " AUTHOR: " + str(index['author']) + " ID: " + str(index['songid'])) # " URL:" + str(index['url']