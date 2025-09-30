# 로그 출력 라이브러리로 로그 관리하기

# 서드파티 로그 출력 전용 라이브러리
# Eilot 설치
# pip install eliot

import json
import sys

from eliot import Message, start_action, to_file, write_traceback
import requests

# 로그 출력을 위해 표준 출력으로 설정(터미널에 출력)
to_file(sys.stdout)

# 크롤링 대상 URL 리스트
PAGE_URL_LIST = [
    "https://eliot.readthedocs.io/en/1.0.0/",
    "https://eliot.readthedocs.io/en/1.0.0/generating/index.html",
    "https://example.com/notfound.html"
]

def fetch_pages():
    """페이지 내용 추출"""
    with start_action(action_type="fetch_pages"):  # 어떤 처리의 로그인지는 action_type으로 지정
        page_contents = {}
        for page_url in PAGE_URL_LIST:
            with start_action(action_type="download", url = page_url):
                try:
                    r = requests.get(page_url, timeout=30)
                    r.raise_for_status()
                except requests.exceptions.RequestException as e:
                    write_traceback()  # 예외 발생 시 traceback 출력
                    continue
                page_contents[page_url] = r.text
    return page_contents

if __name__ == "__main__":
    page_contents = fetch_pages()
    with open("page_contents.json", "w") as f_page_contents:
        json.dump(page_contents, f_page_contents, ensure_ascii=False)
    
    # 단순하게 로그 메시지만 출력할 수도 있음
    Message.log(message_type = "info", msg = "데이터 저장 완료.")