import cx_Oracle
from sklearn.model_selection import cross_val_score

conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()
cursor.execute("select * from emp")

# print(cursor)

# for item in cursor:
#     print(item[1],item[5])

# conn.close()

# 1.emp 테이블에 job을 입력받아 해당 job인 사원을 출력하세요
# 2.사원의 이름의 일부를 입력받아서 검색해서 출력

# for item in cursor:
#     input('[ename]을 입력하세요>>>')
#     print(item)

while True:
    choice = input('''1.job 출력 2.사원 검색>>> ''')
    if choice =='1': 
        conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
        cursor = conn.cursor()
        cursor.execute("select * from emp")
            print('ename','job')
        for item in cursor:
            print(item[1],item[2])
           
    elif choice == '2':
        pass
