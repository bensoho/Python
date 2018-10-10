#ex05_find_max_min.py

# find some elements which are the max or min 
import heapq


nums = [1,8,2,23,7,-4,18,23,42,37,2]
# print(max(nums))
# print(min(nums))

print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))

portfolio = [
{'name':'IBM','Shares':100,'price':91.1},
{'name':'AAPL','Shares':50,'price':543.22},
{'name':'FB','Shares':200,'price':21.09},
{'name':'HPQ','Shares':35,'price':31.75},
{'name':'YAHOO','Shares':45,'price':16.35},
{'name':'ACME','Shares':75,'price':115.65}
]

cheap = heapq.nsmallest(3,portfolio,key=lambda s:s['price'])
expensive = heapq.nlargest(3,portfolio,key=lambda s:s['price'])


print(cheap)
print(expensive)

