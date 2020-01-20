import pymysql

#MtSQL Connection
conn =pymysql.connect(host='localhost',user='python2',password='1111!',
                      db='python_app1',charset='utf8')

try:
    with conn.cursor() as c: #conn.cursor(pymysql.cursor.DictCursor)
        c.execute("SELECT * FROM users")
        #1개 로우
        # print(c.fetchone())
        #선택 지정
        # print(c.fetchmany(3))
        #전체 로우
        # print(c.fetchall())

        #순회1
        rows = c.fetchall()
        c.execute("SELECT * FROM users ORDER BY id ASC")
        for row in rows:
            print("usage1 >",row)

        #순회2
        c.execute("SELECT * FROM users ORDER BY id DESC")
        for row in c.fetchall():
            print("usage2 >",row)

        #조건 조회1
        param1 = (1,)
        c.execute("SELECT * FROM users WHERE id=%s",param1)
        print('param1',c.fetchall())

        #조건 조회2
        param2 = 1
        c.execute("SELECT * FROM users WHERE id='%d'" %param2)
        print('param2',c.fetchall())

        #조건 조회3
        param3 = (4,5)
        c.execute("SELECT * FROM users WHERE id IN(%s, %s)",param3)
        print('param3',c.fetchall())

        #조건 조회4
        c.execute("SELECT * FROM users WHERE id IN('%d',%d)" % (4,5))
        print('param3',c.fetchall())

finally:
    conn.close()
