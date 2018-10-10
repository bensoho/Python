#_*_coding:utf-8_*_
import requests, sys
import time
from bs4 import BeautifulSoup

"""
类说明:下载《笔趣看》网小说《一念永恒》
"""
class downloader(object):
    def __init__(self):
        self.server = 'https://www.sbiquge.com'
        self.target = 'https://www.sbiquge.com/7_7852'
        self.names = [] #save chapter name
        self.urls = [] #save chapter url
        self.nums = 0 #save chapter numbers

        '''
        函数说明:获取下载链接
        '''
    def get_download_url(self):
        req = requests.get(url = self.target)
        html = req.text
        div_bf = BeautifulSoup(html,features='lxml')
        div = div_bf.find_all('div',class_ = 'listmain')
        a_bf = BeautifulSoup(str(div[0]),features='lxml')
        a = a_bf.find_all('a')
        self.nums = len(a[9:-1])
        for each in a[9:-1]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))
            #print(each.string)

    '''
    函数说明:获取章节内容
    '''
    def get_contents(self,target):
        req = requests.get(url = target)
        html = req.text
        bf = BeautifulSoup(html,features='lxml')
        texts = bf.find_all('div',class_ = 'showtxt')
        texts = texts[0].text.replace('\xa0'*8,'\n\n')
        return texts

    '''
    函数说明:将爬取的文章内容写入文件
    '''
    def writer(self,name,path,text):
        write_flag = True
        with open(path,'a',encoding = 'utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')



if __name__ == "__main__":
    d1 = downloader()
    d1.get_download_url()
    print('《一年永恒》开始下载：')
    for i in range(d1.nums):
        d1.writer(d1.names[i],'一念永恒.txt',d1.get_contents(d1.urls[i]))
        sys.stdout.write("  已下载:{0:.1f}%\r".format(float(i/d1.nums)*100))
        sys.stdout.flush()
        #time.sleep(1)
    print('《一年永恒》下载完成')