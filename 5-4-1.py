import pymysql
import simplejson as json
import datetime

#MtSQL Connection
conn =pymysql.connect(host='localhost',user='python2',password='1111!',
                      db='python_app1',charset='utf8')

#pyMysql 버전 확인
# print('pymysql.version',pymysql.__version__)

#데이터베이스선탁
# conn.select_db('python_app1')

#cursor 연결
c = conn.cursor()
# print(type(c))

#데이터 베이스 생성
# c.execute('create database python_app2') #DML, DDL, DCL 사용가능

# #커서반환
# c.close()

# #접속 해제
# conn.close()
# #트렌젝션 시작 선언
# conn.begin()
# #커밋
# conn.commit()
# #롤백
# conn.rollback()

#날짜생성
now = datetime.datetime.now()
nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDateTime',nowDateTime)

c.execute("CREATE TABLE IF NOT EXISTS users(id bigint(20) NOT NULL, \
            username varchar(20), \
            email varchar(30), \
            phone varchar(30), \
            website varchar(30), \
            regdate varchar(20) NOT NULL, PRIMARY KEY(id))")

try:
    with conn.cursor() as c:
        #JSON to pyMysql
        with open('C:/python_Webcroling/section5/data/users.json','r') as infile:
            r = json.load(infile)
            userData =[]
            for user in r:
                t = (user['id'],user['username'],user['email'],user['phone'],user['website'],nowDateTime)
                userData.append(t)
            c.executemany("INSERT INTO users(id, username, email, phone, website,regdate) VALUES (%s, %s, %s, %s, %s, %s)",userData)
        conn.commit()
finally:
    conn.close()
