from cgi import print_exception
import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()

# cursor.execute("drop table fruit_store")
cursor.execute("create table fruit_store(fruit_name varchar2(20),price number(7),count number(5))")
sql = "insert into fruit_store values (:1,:2,:3)"

fruit_name = input('과일명 >>>')
price = input('가격 >>>')
count = input('수량 >>>')
data = (fruit_name, int(price), int(count))

# cursor.execute("update table fruit_store(fruit_name varchar2(20),price number(7),count number(5))")
# sql = "insert into fruit_store values (:1,:2,:3)"

# fruit_name = input('과일명 >>>')
# price = input('가격 >>>')
# count = input('수량 >>>')
# data = (fruit_name, int(price), int(count))

cursor.execute(sql,data)
cursor.close()
conn.commit()
conn.close()