import requests
import re

# data = {
#     'name':'benjamin',
#     'age':22
# }
# r = requests.post('http://httpbin.org/post',data=data)
# # # print(type(r))
# # # print(r.status_code)
# # # print(type(r.text))
# print(r.text)
# # print(r.cookies)
# print(r.json())
headers = {
    'User-Agent':'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, Like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
# r = requests.get('https://www.zhihu.com/explore',headers=headers)
# print(r.text)
r = requests.get('https://www.jianshu.com',headers=headers)
# print(type(r.status_code),r.status_code)
# print(type(r.headers),r.headers)
# print(type(r.cookies),r.cookies)


# if not r.status_code == requests.codes.ok:
#     exit()
# else:
#     print('Request Successfully')

r = requests.get("https://www.baidu.com")
for k,v in r.cookies.items():
    print(k + " " + v)
    