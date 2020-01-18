import simplejson as json
from tinydb import TinyDB, Query, where

db = TinyDB('C:/python_Webcroling/section5/databases/database.db',default_table='users')

#메모리 DB 생성 ->메모리에서 생성해서 휘발하기
# db = TinyDB(storage=MemoryStorage,default_table='users')

#테이블 선택
users = db.table('users')
todos = db.table('todos')

Users = Query()
Todos = Query()

# Users 여러가지 조회 방겁
# print(users.search(Users.id == 7))
# print(users.search(Users['id'] == 7))
# print(users.search(where('id') == 7))
# print(users.search(Query()['id'] == 7))
# print(users.search(where('address')['zipcode'] == "90566-7771"))
# print(users.search(where('address').zipcode == "90566-7771"))

#고급 쿼리
# print(users.search(Users.email.exists()))
# print(users.search(Users['email'].exists()))

#Not
print('not', users.search(~(Users.username == 'Bret')))

#Or
print('or', users.search((Users.username == 'Bret') |(Users.username == 'Antonette')  ))

#And
print('and', users.search((Users.username == 'Bret') & (Users.id == 1)  ))

#기타함수
print('len',len(users))
print('len',len(todos))
print('contains',users.contains(Users.username=='Kamren'))
print('count',users.count(Users.username=='Kamren'))
