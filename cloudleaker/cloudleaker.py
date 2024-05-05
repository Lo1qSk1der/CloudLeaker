import requests
import execjs
import os

class CloudLeaker:
    
    # Initialize some important variable
    def __init__(self) -> None:
        self.header: dict = None
        self.data: dict = None
        self.savepath: str = None
        self.arg: str = None
        self.http: str = None
        self.ids: int = None

    def download(self,id,autoplay= False):
        self.ids = id
        self.http = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=a5ee7f9cd35f2d58788aae444130511b"
        self.arg = '{"ids":"[' + str(self.ids) +']","level":"standard","encodeType":"aac","csrf_token":""}'
        self.header = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/122.0.0.0'}
        with open('core.js','r',encoding='utf-8') as Script: self.data = execjs.compile(Script.read()).call('test',self.arg)
        request = requests.post(url=self.http,headers=self.header,data=self.data)
        url = request.json()['data'][0]['url']
        response = requests.get(url=url,headers=self.header)
        with open("D:\\pythonProject\\cloudleaker\\saves\\" + str(self.ids) + ".m4a","wb") as music: music.write(response.content)
        if autoplay: os.system("D:\\pythonProject\\cloudleaker\\saves\\" + str(self.ids) + ".m4a")
