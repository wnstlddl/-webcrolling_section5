import simplejson as json
from tinydb import TinyDB, Query

db = TinyDB('C:/python_Webcroling/section5/databases/database.db',default_table='users')

#메모리 DB 생성 ->메모리에서 생성해서 휘발하기
# db = TinyDB(storage=MemoryStorage,default_table='users')

#테이블 선택
users = db.table('users')
todos = db.table('todos')

#user tabls 출력
# for item in users:
#     print(item['username'],' : ',item['phone'])
#
# #todo tabls 출력
# for item in todos:
#     print(item['title'],' : ',item['completed'])

#연결 관계 출력(조건문)
# for item in users:
#     print('[',item['username'],']')
#     for todo in todos:
#         if item['id'] == todo['userId']:
#             print(todo['title'])

#쿼리 객체 사용 조회
Users = Query()
Todos = Query()

#Row 수정
users.update({'username':'kim'},Users.id==3)

user_3 = users.search(Users.id ==3) # >,<,>=,<=
print(user_3)

#Row 삭제
users.remove(Users.id==3)
print(users.search(Users.id ==3))
