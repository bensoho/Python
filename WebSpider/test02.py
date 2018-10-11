#*_*_coding:utf-8*_*
from lxml import etree
import sys
text = '''
        <div class="nav">
            <ul class="navbar">
                <li><a href="/" data-act="home-click" >Home</a></li>
                <li><a href="/films" data-act="movies-click" >电影</a></li>
                <li><a href="/cinemas" data-act="cinemas-click" >影院</a></li> 
                <li><a href="/board" data-act="board-click"  class="active" >榜单</a></li>
                <li><a href="/news" data-act="hotNews-click" >热点</a></li>
            </ul>
        </div>
        '''
#html = etree.parse('./test.html',etree.HTMLParser(encoding='utf-8'))
html = etree.HTML(text)
result = html.xpath('//li[position()<4]/a/text()')
print(result)