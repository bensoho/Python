from bs4 import BeautifulSoup
text = '''
        <div class="app-download">
          <a href="/app" target="_blank">
            <span class="iphone-icon"></span>
            <span class="apptext">APP下载</span>
            <span class="caret"></span>
            <div class="download-icon">
                <p class="down-title">扫码下载APP</p>
                <p class='down-content'>选座更优惠</p>
            </div>
          </a>
        </div>
        '''
soup = BeautifulSoup(text,'lxml')
print(soup.a.span.next_siblings)
for i in soup.a.span.next_siblings:
    print(i.string)