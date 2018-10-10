#ex02_split_records.py
#在变量名前加上✳️号，表示这个变量是一个序列变量 - 扩展分解操作
record = ('Dave', 'dave@example.com','773-555-1212','847-8988')

name, email, *phone_numbers = record

print(name)
print(email)
print(phone_numbers)

#计算前7个季度的平均值和最近一个季度的销售额来进行比较

sales_record = [10,8,7,1,9,5,10,3]
*trailing_qtrs, current_qtr = sales_record
trailing_avg = sum(trailing_qtrs)/len(trailing_qtrs)

print(current_qtr)
print(trailing_qtrs)
