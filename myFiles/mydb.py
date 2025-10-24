import mysql.connector

db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Telekinesis1'
)  
print('Done')
cursor=db.cursor()
print('Done')
'''cursor=database.cursor()
cursor.execute('CREATE DATABASE employee')
cursor.close()'''
print('Done')