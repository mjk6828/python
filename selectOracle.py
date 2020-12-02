import cx_Oracle

conn = cx_Oracle.connect("scott", "scott", "localhost:1521/orcl.93.91.74") #오라클 연결
cursor = conn.cursor() #커서 생성
sql = "select * from orauser"
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    for i in row:
        print(i, end=' ')
    print('')
conn.close()