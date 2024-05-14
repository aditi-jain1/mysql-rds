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

# Create a Table
sql = '''use users'''
cursor.execute(sql)

sql = '''select * from person'''
cursor.execute(sql)
print(cursor.fetchall())




