import requests
from bs4 import BeautifulSoup

# 크롤링할 페이지 URL
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"

# requests를 사용하여 페이지 내용 가져오기
response = requests.get(url)
html_content = response.text

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html_content, 'html.parser')

# 기사 제목을 담을 리스트
titles = []

# HTML에서 기사 제목 태그를 찾아 제목 추출
for title in soup.find_all('a', class_='news_tit'):
    titles.append(title.get_text())

# 결과 출력
for i, title in enumerate(titles):
    print(f"{i+1}. {title}")
