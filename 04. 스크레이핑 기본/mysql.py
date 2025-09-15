# %%
# 데이터베이스에 접속해서 SQL 실행하기
import MySQLdb
connection = MySQLdb.connect(
    user = "scrapingman",
    passwd = "myPassword-1",
    host = "localhost",
    db = "scrapingdata",
    charset = "utf8"
)

# connect 함수의 반환값 확인
print(type(connection))

# cursor 생성하기
cursor = connection.cursor()
print(type(cursor))

# 테이블 만들기
cursor.execute(
    "CREATE TABLE books (title text, url text)"
)
connection.commit() # SQL 실행

# %%
import MySQLdb
connection = MySQLdb.connect(
    user = "scrapingman",
    passwd = "myPassword-1",
    host = "localhost",
    db = "scrapingdata",
    charset = "utf8"
)

# cursor 생성하기
cursor = connection.cursor()
cursor.execute(
    "INSERT INTO books VALUES(%s, %s)", ("처음 시작하는 파이썬 프로그래밍", "https://example.com")
)
connection.commit() # SQL 실행

# %%
import MySQLdb
connection = MySQLdb.connect(
    user = "scrapingman",
    passwd = "myPassword-1",
    host = "localhost",
    db = "scrapingdata",
    charset = "utf8"
)
# cursor 생성하기
cursor = connection.cursor()

# 실행할 때마다 다른 결과가 나오지 않게 테이블 제거해두기
cursor.execute("DROP TABLE IF EXISTS books")

# 테이블 만들기
cursor.execute("CREATE TABLE books (title text, url text)")

# 데이터 삽입하기
cursor.execute(
    "INSERT INTO books VALUES(%s, %s)", ("처음 시작하는 파이썬 프로그래밍", "https://example.com")
)

# SQL 실행
connection.commit()

# 연결 종료하기
connection.close()

#%%
# 분석 결과 저장하기
import feedparser
import MySQLdb

# MySQL 접속
connection = MySQLdb.connect(
    user = "scrapingman",
    passwd = "myPassword-1",
    host = "localhost",
    db = "scrapingdata",
    charset = "utf8"
)

# cursor 생성하기
cursor = connection.cursor()

# 실행할 때마다 다른 결과가 나오지 않게 테이블 제거해두기
cursor.execute("DROP TABLE IF EXISTS books")

# 테이블 만들기
cursor.execute("CREATE TABLE books (title text, url text)")

# URL을 지정해서 FeedParserDict 객체 생성하기
rss = feedparser.parse("http://www.aladin.co.kr/rss/special_new/351")
print(rss.version)  # RSS 버전
print(rss['feed']) # 피드 정보
#print(rss['feed']['title'])  # 피드 제목

for content in rss['entries']:
    # 데이터 저장
    cursor.execute(
        "INSERT INTO books VALUES(%s, %s)", (content['title'], content['link']) 
    )

# SQL 실행
connection.commit()

# 연결 종료하기
connection.close()
# %%
