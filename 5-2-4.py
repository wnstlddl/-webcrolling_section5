import simplejson as json
from tinydb import TinyDB, Query, where

db = TinyDB('C:/python_Webcroling/section5/databases/database1.db')

# db.insert({'name':'kim','email':'test@google.com'}) #json(dict) {}
# db.insert_multiple([{'name':'lee','email':'test2@google.com'},{'name':'park','email':'test3@google.com'}]) #jsonArray(dict) [{},{},{}]

SQL =Query()

el = db.get(SQL.name=='kim')

print(el)
print(el.doc_id)

#데이터 수정
db.update({'email':'tesdf@daum.net'},doc_ids=[1])

#데이터 수정 및 수정
db.upsert({'email':'tesdf@naver','login':True},SQL.name=='park')

#데이터 삭제
# db.remove(doc_ids=[1,3])
# db.remove(SQL.name=='park')

#전체조회
print(db.all())
