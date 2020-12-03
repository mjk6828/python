import cx_Oracle
class connection:
    conn = cx_Oracle.connect("scott", "scott", "localhost:1521/orcl.93.91.74") #오라클 연결
    cur = conn.cursor()
    sql = "select * from orauser"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()
