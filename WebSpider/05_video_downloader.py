import requests, re, json
from bs4 import BeautifulSoup

class video_downloader():
    def __init__(self, url):
        self.server = 'hhttp://v.xfsub.com'
        self.api = 'http://v.xfsub.com/?url='
        self.get_url_api = 'http://v.xfsub.com/sfsub_api/url.php'
        self.url = url.split('#')[0]
        self.target = self.api + self.url
        self.s = requests.session()

    def get_key(self):
        req = self.s.get(url=self.target)
        req.encoding = 'utf-8'
        print(req.text)
        self.info = json.loads(re.findall('"url.php",\ (.+),',req.text[0]))
if __name__ == '__main__':
    url = 'https://www.iqiyi.com/v_19rr7p365w.html'
    vd = video_downloader(url)
    vd.get_key()

