import cx_Oracle

#모든 레코드 삽입
conn = cx_Oracle.connect("scott", "scott", "localhost:1521/orcl.93.91.74") #오라클 연결
cur = conn.cursor() #커서 생성

items = [
    (1,'승연2','12345','한승연2','mjk6829@gmail.com',75456683),
    (2, '승연3','12345','한승연3','mjk6829@gmail.com',75456683),
    (3,'승연4','12345','한승연4','mjk6829@gmail.com',75456683),
    (4, '승연5','12345','한승연5','mjk6829@gmail.com',75456683)
]
sql = "INSERT INTO orauser VALUES(:1, :2, :3, :4, :5, :6)"
cur.bindarraysize = len(items)
cur.executemany(sql, items)
conn.commit()

sql2 = "select count(*) from orauser"

cur.execute(sql2)
count = cur.fetchone()
print("유저수:", count[0])