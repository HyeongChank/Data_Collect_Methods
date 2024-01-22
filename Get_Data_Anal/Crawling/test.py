from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from datetime import datetime
import time

def operate(keywords):
    for i in range(0, 20):
       
        service = ChromeService()
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("http://www.google.com")

        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(keywords)
        search_box.submit()

        # 기다리면서 검색 결과 페이지 로딩을 기다림
        time.sleep(5)  # 페이지가 완전히 로드될 때까지 대기

        
        print(1)
        
        # 모든 h3 태그를 찾아서 검사
        h3_elements = driver.find_elements(By.TAG_NAME, 'h3')

        for idx, h3_element in enumerate(h3_elements, 1):
            h3_text = h3_element.text

            # "공제회"를 포함하는지 확인
            if "공제회" in h3_text:
                # 해당 웹사이트 클릭
                h3_element.click()

                # 클릭한 웹사이트의 작업 수행 (여기서는 5초 대기 후 브라우저 종료)
                driver.implicitly_wait(5)
                driver.quit()

                print(f"공제회를 포함한 h3 요소를 찾았습니다. ({idx}번째 h3)")

        # 브라우저 종료
        driver.quit()

if __name__ == "__main__":
    keywords = 'lofa'
    operate(keywords)
