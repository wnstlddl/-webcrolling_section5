import sqlite3
import simplejson as json
import datetime

#DB 생성
# for mac
# conn = sqlite3.connect('C:/python/webcrolling/section5/-webcrolling_section5/databases/sqlite1.db')
#for desktop
conn = sqlite3.connect('C:/python_Webcroling/section5/databases/sqlite1.db') #isolation_level=None : Auto Commit

#DB 생성(메모리)
# conn = sqlite3.connect(':memory:')
#날짜 생성
now = datetime.datetime.now()
print('now :',now)
nowDatetime = now.strftime("%Y-%m-%d %H:%M:%S")
print('nowDatetime :',nowDatetime)

#sqlite3 버전 확인
print('sqlite3.version',sqlite3.version)
print('sqlite3.sqlite_version',sqlite3.sqlite_version)

#Cursor 연결
c = conn.cursor()
print(type(c))

#테이블 생상(SQLite3 Datatype : TEXT,NUMERIC, INTEGER, REAL, BLOB)
c.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)')#AUTOINCREMENT

# 데이터 삽입
# c.execute("INSERT INTO users VALUES(1, 'kim', 'kim@naver.com', '010-0000-0000', 'kim.co.kr', ?)",(nowDatetime,))

userList = (
    (2, 'kim', 'kim@naver.com', '010-0000-0000', 'kim.co.kr',nowDatetime),
    (3, 'kim', 'kim@naver.com', '010-0000-0000', 'kim.co.kr',nowDatetime),
    (4, 'kim', 'kim@naver.com', '010-0000-0000', 'kim.co.kr',nowDatetime),
)

# c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", userList)

with open('C:/python_Webcroling/section5/data/users.json', 'r') as infile:
    r = json.load(infile)
    userDate = []
    for user in r:
        t =(user['id'],user['username'],user['email'],user['phone'],user['website'],nowDatetime)
        # print('t',t)
        userDate.append(t)
    # c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", userDate)
    c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", tuple(userDate))

# print('user db delete', conn.execute("delete from users").rowcount,'rows')
conn.commit()
