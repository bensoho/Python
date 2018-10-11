from pyquery import PyQuery as pq

html = '''
          <dl>
            <dt>资讯产品</dt>
            <dd class="th2">
              <p><a href="http://www.51cto.com/tag/practice/" target="_blank">实践录</a></p>
              <p><a href="http://zhuanlan.51cto.com/" target="_blank">专栏</a></p>
              <p><a href="http://www.51cto.com/tag/original/" target="_blank">原创</a></p>
              <p><a href="http://www.51cto.com/tag/translation/" target="_blank">译文</a></p>
              <p><a href="http://www.51cto.com/col/35/" target="_blank">专题</a></p>         
              <p><a href="http://www.cioage.com/cio.html" target="_blank" rel="nofollow">智享汇</a></p>
              <p><a href="http://www.51cto.com/tag/practice" target="_blank">足迹</a></p>
              <p><a href="http://www.51cto.com/tag/interviews" target="_blank">匠心</a></p>
              <p><a href="http://www.51cto.com/tag/huiyan" target="_blank">慧眼</a></p>
              <p><a href="http://www.51cto.com/tag/video/" target="_blank">视频</a></p>
            </dd>
          </dl>
          <dl>
'''
doc = pq(html)
# print(doc('dd'))
# doc = pq(url='https://cuiqingcai.com')
# print(doc('title').text())
# a = doc('.th2 p a')
# for item in a.items():
#     print(item.text())
target = doc('a')
target.addClass('active')
print(target)