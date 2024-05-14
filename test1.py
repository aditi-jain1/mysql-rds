#Database name: database-3
#Master username: admin
#Password: 2wsxcft6
#Database port: 3306
#Hostname:database-3.cv2w86es0oma.us-east-2.rds.amazonaws.com

import pymysql

connection = pymysql.connect(
        host='database-3.cv2w86es0oma.us-east-2.rds.amazonaws.com',
        user='admin',
        password='2wsxcft6'
    )
print("Connected to MySQL database")

# Create a cursor object
cursor = connection.cursor()

print(cursor.execute("select version()"))

data = cursor.fetchall()
print(data)

# Create a Database

sql = '''drop database users'''
cursor.execute(sql)

sql = '''create database users'''
cursor.execute(sql)

# Create a Table
sql = '''use users'''
cursor.execute(sql)

sql = '''create table person (
id int not null auto_increment, 
name text,
primary key (id)
)'''
print(cursor.execute(sql))

sql = '''show tables'''
cursor.execute(sql)
print(cursor.fetchall())

#Insert Data

sql = '''
insert into person(name) values('%s')''' % ('maya')

print(cursor.execute(sql))
connection.commit()

sql = '''
insert into person(name) values('%s')''' % ('leo')

print(cursor.execute(sql))
connection.commit()

sql = '''select * from person'''
cursor.execute(sql)
print(cursor.fetchall())




