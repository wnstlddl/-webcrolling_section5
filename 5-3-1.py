import sqlite3
import simplejson as json
import datetime

#DB 생성
conn = sqlite3.connect('C:/python/webcrolling/section5/-webcrolling_section5/databases/sqlite1.db')
#날짜 생성
now = datetime.datetime.now()
print('now :',now)
nowDatetime = now.strftime("%Y-%m-%d %H:%M:%S")
print('nowDatetime :',nowDatetime)

#sqlite3 버전 확인
print('sqlite3.version',sqlite3.version)
print('sqlite3.sqlite_version',sqlite3.sqlite_version)
