import requests,re,json

def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    res = requests.get(url,headers=headers)
    if res.status_code == 200:
        return res.text
    else:
        return None


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?class="star">\n\s*(.*?)\n\s*?</p>.*?"releasetime">(.*?)</p>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield{
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3],
            'time':item[4]
        }

def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

if __name__ == '__main__':
    url = 'http://maoyan.com/board/4?offset=10'
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)