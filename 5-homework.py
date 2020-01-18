import simplejson as json
from tinydb import  TinyDB, Query, where

#파일 DB 생성
db = TinyDB('C:/python_Webcroling/section5/databases/homework.db')

#테이블 선택
albums = db.table('albums')
photos = db.table('photos')

#테이블 데이터 전체 삽입
# with open('C:/python_Webcroling/section5/data/albums.json','r') as infile:
#     r = json.loads(infile.read())
#     for u in r:
#         albums.insert(u)
#
# #테이블 데이터 전체 삽입2
# with open('C:/python_Webcroling/section5/data/photos.json','r') as infile:
#     r = json.loads(infile.read())
#     for t in r:
#         photos.insert(t)

Albums = Query()
Photos = Query()

# Users 여러가지 조회 방겁
# print(albums.search(Albums.userId == 7))
# print(len(albums.search(Albums.userId == 10)))

# 연결 관계 출력(조건문)
for album in albums:
    print('[',album['userId'],']')
    for photo in photos:
        if album['id'] == photo['albumId']:
            print(photo['id'])
            print(photo['title'])
