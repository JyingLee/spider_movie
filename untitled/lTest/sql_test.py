import mysql.connector

conn = mysql.connector.connect(user='root', password='', database='python_test')
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) PRIMARY  KEY ,name1 VARCHAR(20))')
cursor.execute('insert into user(id,name1) VALUES (%s,%s)', ['1', 'jying'])
print(cursor.rowcount)
conn.commit()
cursor.close()
