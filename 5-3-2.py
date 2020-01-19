import sqlite3
import simplejson as json
import datetime

#DB 생성
# for mac
# conn = sqlite3.connect('C:/python/webcrolling/section5/-webcrolling_section5/databases/sqlite1.db')
#for desktop
conn = sqlite3.connect('C:/python_Webcroling/section5/databases/sqlite1.db') #isolation_level=None : Auto Commit

#커서 바인딩
c = conn.cursor()

#데이터 조회
c.execute("SELECT * FROM users")

#1개 로우 선택
# print(c.fetchone())

#지정 로우 선택
# print(c.fetchmany(size=4))

#전체 로우 선택
# print(c.fetchall())

#순회1
# rows = c.fetchall()
# for row in rows:
#     print('usage1 > ',row)

#순회2
# for row in c.fetchall():
#     print('usage2 > ',row)

#순회3
# for row in c.execute("SELECT * FROM users"):
#     print('usage3 > ',row)

#조건 조회 1
param1 = (1,)
c.execute("SELECT * FROM users WHERE id=?",param1)
print(c.fetchall())

#조건 조회 2
param2 = 1
c.execute("SELECT * FROM users WHERE id='%s'" % param2) # %s,%d,%f,%d 와는 다른 개념
print(c.fetchall())

#조건 조회 3
c.execute("SELECT * FROM users WHERE id=:id",{"id":1})
print(c.fetchall())

#조건 조회 4
param4 = (1,4)
c.execute("SELECT * FROM users WHERE id IN(?,?)",param4)
print(c.fetchall())

#조건 조회 5
c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2",{"id1":1,'id2':4})
print(c.fetchall())

#dump
with conn:
    #Dump 출력
    with open('C:/python_Webcroling/section5/data/test.dump','w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print("Dump Write Complete!")
