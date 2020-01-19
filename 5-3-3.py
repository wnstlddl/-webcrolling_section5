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

#데이터 수정1
c.execute("UPDATE users SET username = ? WHERE id=?",('niceman',1))

#데이터 수정2
c.execute("UPDATE users SET username =:name WHERE id=:id",{'name':'goodboy','id': 2})

#데이터 수정3
param1 = ('sexyboy',3)
c.execute("UPDATE users SET username ='%s' WHERE id='%s'" % param1)

#데이터 삭제
c.execute("DELETE FROM users WHERE id=?",(4,))

#데이터 삭제2
c.execute("DELETE FROM users WHERE id=:id",{'id': 5})

#데이터 삭제3
param1 = (3,)
c.execute("DELETE FROM users WHERE id='%s'" % param1)

#중간 데이터 확인
for user in c.execute("SELECT * FROM users"):
    print(user)

conn.commit()
conn.close()
