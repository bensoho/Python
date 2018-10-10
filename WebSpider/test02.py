#*_*_coding:utf-8*_*
from lxml import etree
import sys
text = '''
        <div class="nav">
            <ul class="navbar">
                <li class="li li-first" name="item"><a href="/" data-act="home-click">首页</a></li>
            </ul>
        </div>
        '''
# html = etree.parse('./test.html',etree.HTMLParser(encoding='utf-8'))
html = etree.HTML(text)
result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
print(result)