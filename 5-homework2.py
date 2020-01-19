import sqlite3
import simplejson as json
import datetime

#DB 생성
#for desktop
conn = sqlite3.connect('C:/python_Webcroling/section5/databases/sqlite_homework.db') #isolation_level=None : Auto Commit
#날짜 생성
now = datetime.datetime.now()
nowDatetime = now.strftime("%Y-%m-%d %H:%M:%S")

c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS photos(albumId INTEGER, id text, title text, url text, thumbnailUrl text, regdate text)')

with open('C:/python_Webcroling/section5/data/photos.json', 'r') as infile:
    r = json.load(infile)
    photoDate = []
    for photo in r:
        t =(photo['albumId'],photo['id'],photo['title'],photo['url'],photo['thumbnailUrl'],nowDatetime)
        print(t)
        photoDate.append(t)
    c.executemany("INSERT INTO photos(albumId, id, title, url, thumbnailUrl, regdate) VALUES (?,?,?,?,?,?)", tuple(photoDate))

conn.commit()
