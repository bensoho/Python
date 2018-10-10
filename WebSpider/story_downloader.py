#_*_coding:utf-8_*_
import requests,sys,time
from bs4 import BeautifulSoup

class story_downloader(object):

    def __init__(self):
        self.server = 'https://www.biqukan.com'
        self.target = 'https://www.biqukan.com/1_1408'
        self.names = []
        self.urls = []
        self.nums = 0
        self.title = ''

    def get_names_urls(self):
        req = requests.get(url = self.target)
        html = req.text
        div_bf = BeautifulSoup(html,features='lxml')
        t_bf = div_bf.find_all('h2')
        self.title = t_bf[0].text
        div = div_bf.find_all('div',class_='listmain')
        a_bf = BeautifulSoup(str(div[0]),features='lxml')
        a = a_bf.find_all('a')
        self.nums = len(a[12:-1])
        for each in a[12:-1]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))
            #print(each.string,self.server + each.get('href'))


    def get_contents(self,target):
        req = requests.get(url=target)
        html = req.text
        div_bf = BeautifulSoup(html,features='lxml')
        texts = div_bf.find_all('div',class_='showtxt')
        texts = texts[0].text.replace('\xa0'*8,'\n\n')
        return texts
        
    def write_to_file(self,name,path,text):
        with open(path,'a',encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')



if __name__ == "__main__":
    dl = story_downloader()
    dl.get_names_urls()
    print(dl.title + '开始下载：')
    for i in range(dl.nums):

        dl.write_to_file(dl.names[i],dl.title,dl.get_contents(dl.urls[i]))
        sys.stdout.write("  已下载:{0:.1f}%\r".format(float(i/dl.nums)*100))
        sys.stdout.flush()

    print(dl.title + '下载完成')