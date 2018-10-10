import re
# content = '''Hello 12345678 wor.ld_This
# is a Regex demo
# '''
# #decorator sign
# result = re.match('^He.*?(\d+).*?demo$',content,re.S)

# print(result.group(1))
# #re.S always used in webpages
#match() always used to process the string from the begining,if not, then cause error
# content = 'http(百度)www.baidu.com'
# result = re.search('[a-z]*.{4}[a-z]*',content)
# print(result)
html = '''
<div id="songs_list">
<h2 class="title">class old song</h2>
<li data-view="4" class="active">
<a href="/3.mp3" singer="QiQin">Gone with the wind</a>
<a href="/4.mp3" singer="WangFeng">Beautiful life</a>
<a href="/5.mp3" singer="Michael Jackson">Dangerous</a>
'''
# result = re.findall('<a.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
# for each in result:
#     print(each)

content1 = '2018-12-15 12:00'
content2 = '2018-12-17 12:55'
content3 = '2016-12-22 13:21'

pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern,'',content1)
result2 = re.sub(pattern,'',content2)
result3 = re.sub(pattern,'',content3)
print(result1,result2,result3)