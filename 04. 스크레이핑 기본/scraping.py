#%%
## Requests 모듈 사용 방법
# 
# 네이버 실시간 검색어 순위 웹 API
import requests
r = requests.get("http://rank.search.naver.com/rank.js")
print(r.status_code)  # 응답 상태 코드 확인(현재 서비스 종료)
print(r.text)  # 응답 내용 출력

# %%
## HTML 소스 분석하기

# 도서 제목 추출하기

# CSS selector: #content > div:nth-child(1) > div.col-md-9 > h1
# XPath: //*[@id="content"]/div[1]/div[2]/h1

# lxml로 스크레이핑하기
import requests
import lxml.html

r = requests.get("https://wikibook.co.kr/python-for-web-scraping/")
html = r.text # HTML 소스코드 추출
root = lxml.html.fromstring(html)  # HTML 파싱
titleElement = root.xpath('//*[@id="content"]/div[1]/div[2]/h1')

print("도서 제목: ", titleElement[0].text)
print("태그: ", titleElement[0].tag)
print("속성: ", titleElement[0].attrib)

# %%
# 인터넷 서점 링크 추출
import requests
import lxml.html

r = requests.get("https://wikibook.co.kr/python-for-web-scraping/")
html = r.text # HTML 소스코드 추출
root = lxml.html.fromstring(html)  # HTML 파싱

linkAs = root.cssselect("#book-stores > li > a")
for linkA in linkAs:
    print(linkA.attrib['href'])
# %%
