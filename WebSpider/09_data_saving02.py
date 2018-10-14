#MYSQL usage
import pymysql
db = pymysql.connect(host='localhost',user='root',password='yjtmue',port=3306,db='spiders')

cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data =  cursor.fetchone()
print(data)

#create database

#cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')


#create table

# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
# cursor.execute(sql)

#insert data
# id = '200343982'
# user = 'Benjamin Liu'
# age = 30
# sql = 'INSERT INTO students(id,name,age) values(%s,%s,%s)'

data = {
    'id':'200817653',
    'name':'Bob Li',
    'age':20
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s']*len(data))

sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)

try:
    if cursor.execute(sql,tuple(data.values())):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()



db.close()
