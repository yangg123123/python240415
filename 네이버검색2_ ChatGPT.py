import requests
from bs4 import BeautifulSoup

def crawl_naver_blog(search_keyword, start_page=1, end_page=100):
    # 결과를 담을 리스트 초기화
    results = []
    
    # 시작 페이지부터 끝 페이지까지 반복
    for page in range(start_page, end_page + 1):
        # 검색어를 이용하여 블로그 검색 결과 페이지 URL 생성
        base_url = "https://search.naver.com/search.naver"
        params = {"where": "post", "sm": "tab_jum", "query": search_keyword, "start": (page - 1) * 10 + 1}
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            # HTML을 파싱하여 BeautifulSoup 객체 생성
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 블로그 검색 결과 항목들을 찾아서 처리
            blog_items = soup.find_all('li', class_='sh_blog_top')
            
            for item in blog_items:
                # 블로그 정보 추출
                blog_title = item.find('a', class_='sh_blog_title').text
                blog_link = item.find('a', class_='sh_blog_title')['href']
                
                # 포스트 정보 추출
                post_title = item.find('a', class_='sh_blog_title')['title']
                post_date = item.find('span', class_='date').text
                
                # 결과를 딕셔너리로 저장
                result = {
                    'blog_title': blog_title,
                    'blog_link': blog_link,
                    'post_title': post_title,
                    'post_date': post_date
                }
                
                # 결과 리스트에 추가
                results.append(result)
        else:
            print(f"Failed to retrieve search results for page {page}.")
    
    return results

# 검색어 입력 받기
search_keyword = input("검색어를 입력하세요: ")

# 크롤링 실행 (1페이지부터 100페이지까지)
search_results = crawl_naver_blog(search_keyword, start_page=1, end_page=100)

# 결과 출력
if search_results:
    print("검색 결과:")
    for idx, result in enumerate(search_results, start=1):
        print(f"\n#{idx}")
        print("블로그명:", result['blog_title'])
        print("블로그주소:", result['blog_link'])
        print("제목:", result['post_title'])
        print("포스팅날짜:", result['post_date'])
else:
    print("검색 결과가 없습니다.")
