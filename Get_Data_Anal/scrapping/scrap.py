import requests
from bs4 import BeautifulSoup

def get_search_results(query):
    # Google 검색 결과 페이지에 접근
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url)
    print('yes')
    # 응답이 성공인지 확인
    if response.status_code == 200:
        print('yesyes')
        # BeautifulSoup을 사용하여 HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')

        # 검색 결과에서 원하는 정보 추출
        results = soup.find_all('div', class_='tF2Cxc')  # 예제에서는 검색 결과의 일부를 나타내는 클래스를 사용
        return results
    else:
        print(f"Error: {response.status_code}")
        return None

def extract_text_from_results(results):
    # 검색 결과에서 텍스트 추출
    texts = [result.get_text() for result in results]
    return texts

if __name__ == "__main__":
    # 검색어 입력
    search_query = input("검색어를 입력하세요: ")

    # 검색 결과 가져오기
    search_results = get_search_results(search_query)

    if search_results:
        # 검색 결과에서 텍스트 추출
        extracted_texts = extract_text_from_results(search_results)

        # 추출된 텍스트 출력
        for i, text in enumerate(extracted_texts, 1):
            print(f"{i}. {text}")
    else:
        print("검색 결과를 가져오는 데 문제가 있습니다.")
