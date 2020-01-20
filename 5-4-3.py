import pymysql

#MtSQL Connection
conn =pymysql.connect(host='localhost',user='python2',password='1111!',
                      db='python_app1',charset='utf8')

try:
    with conn.cursor() as c:
        #데이터 수정1
        c.execute("UPDATE users SET username = %s WHERE id = %s",('niceman',1))
        #데이터 수정1
        c.execute("UPDATE users SET username = '%s' WHERE id = '%d'" % ('goodboy',2))



        #데이터 삭제1
        c.execute("DELETE FROM users WHERE id = %s",(1,))

        #데이터 삭제2
        c.execute("DELETE FROM users WHERE id = '%s'" % (2,))

        #중간 데이터 확인
        # c.execute("SELECT * FROM users")

        c.execute("SELECT * FROM users ORDER BY id ASC")
        for row in c.fetchall():
            print("usage1 >",row)

        # conn.commit()

finally:
    conn.close()
