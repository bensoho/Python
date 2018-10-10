#re.py

import re
print(re.match('www','www.w3cschool.cn').span())
print(re.search('com','www.w3cschool.com').span())

line = 'Usually cats are smarter than dogs.'
searchObj = re.search(r'(.*) are (.*?) .*',line)
print(searchObj.group())

