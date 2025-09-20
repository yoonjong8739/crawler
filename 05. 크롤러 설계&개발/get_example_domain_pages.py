# 크롤러 개발 시 직면하는 여러 문제
# 1. 대량의 페이지를 크롤링하면 시간이 오래 걸림
# 2. 동작하고 있는 것처럼 보였던 크롤러가 사실은 버그 때문에 멈춰있을 수 있음

#%%
## print 함수로 로그 출력하기
# 요청에 걸린 시간 출력하기

import time
import requests

PAGE_URL_LIST = [
    "http://example.com/1.page",
    "http://example.com/2.page",
    "http://example.com/3.page",
]

for page_url in PAGE_URL_LIST:
    res = requests.get(page_url, timeout = 30)
    print(
        "페이지 URL: {}, HTTP 상태: {}, 처리 사간(초): {}".format(
            page_url, 
            res.status_code, 
            res.elapsed.total_seconds())
    )
    time.sleep(1)  # 1초 대기

#%%
# 디버그 전용 로그와 오류 전용 로그를 다른 파일에 출력하면서 터미널의 표준 출력에도 로그 출력
import json
import time
import requests

PAGE_URL_LIST = [
    "http://example.com/1.page",
    "http://example.com/2.page",
    "http://example.com/3.page",
]

def fetch_pages():
    """페이지의 내용을 추출하기"""
    # 처리 기록 전용 로그 파일을 append 모드로 열기
    f_info_log = open("crawler_info.log", "a", encoding="utf-8")
    
    # 오류 기록 전용 로그 파일을 append 모드로 열기
    f_error_log = open("crawler_error.log", "a")
    
    # 추출 내용을 저장할 딕셔너리
    page_contents = {}
    
    # 터미널에 처리 시작을 출력하고, 로그 파일에도 메시지를 출력
    msg = "크롤링을 시작합니다\n"
    print(msg)
    f_info_log.write(msg)
    
    for page_url in PAGE_URL_LIST:
        r = requests.get(page_url, timeout = 30)  # try 구문에 포함되지 않아 예외처리하지 못함.
        try:
            r.raise_for_status()  # 응답에 문제가 있으면 예외를 발생
        except requests.exceptions.RequestException as e:
            # requests와 관련된 예외가 발생하면 터미널과 오류 로그에 오류를 출력
            msg = "[ERROR] {}\n".format(e)
            print(msg)
            f_error_log.write(msg)
            continue  # 예외가 발생하면 중지하지 않고 다음 페이지로 진행
    
        # 정상적으로 내용을 추출했다면 딕셔너리에 내용을 저장
        page_contents[page_url] = r.text  # (key)url: (value)html 내용
        time.sleep(1)  # 1초 대기

    f_info_log.close()  # 처리 기록 전용 로그 파일 닫기
    f_error_log.close()  # 오류 기록 전용 로그 파일 닫기
    
    return page_contents

if __name__ == "__main__":
    page_contents = fetch_pages()
    f_page_contents = open("page_contents.json", "w")
    json.dump(page_contents, f_page_contents, ensure_ascii=False)
    f_page_contents.close()

# %%
# with 구문으로 close 메서드 누수 막기
import json
import time
import requests

PAGE_URL_LIST = [
    "http://example.com/1.page",
    "http://example.com/2.page",
    "http://example.com/3.page",
]

def fetch_pages2():
    """페이지의 내용을 추출하기"""
    # 처리 기록 전용 로그 파일을 append 모드로 열기
    with open("crawler_info.log", "a", encoding="utf-8") as f_info_log, \
        open("crawler_error.log", "a") as f_error_log:  # 오류 기록 전용 로그 파일을 append 모드로 열기
        
        # 추출 내용을 저장할 딕셔너리
        page_contents = {}
        
        # 터미널에 처리 시작을 출력하고, 로그 파일에도 메시지를 출력
        msg = "[INFO]크롤링을 시작합니다\n"
        print(msg)
        f_info_log.write(msg)
        
        for page_url in PAGE_URL_LIST:
            try:
                r = requests.get(page_url, timeout = 30)
                r.raise_for_status()  # 응답에 문제가 있으면 예외를 발생
            except requests.exceptions.RequestException as e:
                # requests와 관련된 예외가 발생하면 터미널과 오류 로그에 오류를 출력
                msg = "[ERROR] {}\n".format(e)
                print(msg)
                f_error_log.write(msg)
                continue  # 예외가 발생하면 중지하지 않고 다음 페이지로 진행
        
            # 정상적으로 내용을 추출했다면 딕셔너리에 내용을 저장
            page_contents[page_url] = r.text  # (key)url: (value)html 내용
            time.sleep(1)  # 1초 대기
    
    return page_contents

if __name__ == "__main__":
    page_contents = fetch_pages2()
    with open("page_contents.json", "w", encoding="utf-8") as f_page_contents:
        json.dump(page_contents, f_page_contents, ensure_ascii=False)