import simplejson as json
from tinydb import TinyDB
from tinydb.storages import MemoryStorage
#파일 DB 생성
db = TinyDB('C:/python_Webcroling/section5/databases/database.db',default_table='users')

#메모리 DB 생성 ->메모리에서 생성해서 휘발하기
# db = TinyDB(storage=MemoryStorage,default_table='users')

#테이블 선택
users = db.table('users')
todos = db.table('todos')

#테이블 데이터 삽입
# users.insert({'name':'kim','email':'test@google.com'})
# todos.insert({'name':'homework','complete':False})

#테이블 데이터 전체 삽입
with open('C:/python_Webcroling/section5/data/users.json','r') as infile:
    r = json.loads(infile.read())
    for u in r:
        users.insert(u)

#테이블 데이터 전체 삽입2
with open('C:/python_Webcroling/section5/data/todos.json','r') as infile:
    r = json.loads(infile.read())
    for t in r:
        todos.insert(t)

# print(users.all())
# print(todos.all())
# print(db.tables())

#전체 데이터 삭제
# users.purge() #db.purge_table('users')
# todos.purge() #db.purge_table('todos')
#
# #전체삭제
# db.purge_tables() #테이블명까지 다 삭제

db.close()
