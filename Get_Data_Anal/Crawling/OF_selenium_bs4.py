from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def operate(keywords):
    service = ChromeService()
    options = webdriver.ChromeOptions()
    
    for i in range(0,20):
        c_time = datetime.now()
        y_time = c_time.year; m_time = c_time.month; d_time = c_time.day ; h_time = c_time.hour ; m_time = c_time.minute
        t = str(y_time) + '.' + str(c_time.month) + '.' + str(d_time) + '.' + str(h_time) + '.' + str(m_time)
        try:
        # for key in keywords:
            
            driver = webdriver.Chrome(service=service, options=options)
            driver.get("http://www.google.com")
            search_box = driver.find_element(By.NAME, "q")
            search_box.send_keys(keywords)
            search_box.submit()
            
            time.sleep(3)
            # 모든 h3 태그를 찾아서 검사
            h3_elements = driver.find_elements(By.TAG_NAME, 'h3')
            time.sleep(3)
            for idx, h3_element in enumerate(h3_elements, 1):
                h3_text = h3_element.text

                # "공제회"를 포함하는지 확인
                if "공제회" in h3_text:
                    # 해당 웹사이트 클릭
                    h3_element.click()

                    # 클릭한 웹사이트의 작업 수행 (여기서는 5초 대기 후 브라우저 종료)
                    #driver.implicitly_wait(5)
                    time.sleep(3)

                    print(f"공제회를 포함한 h3 요소를 찾았습니다. ({idx}번째 h3)")
                else:
                    pass
            
        except Exception as e:
            print("error ", e)

            pass
        finally:
            print(t + " " + str(i+1) + "회 " + keywords)
            driver.quit()

        


if __name__=="__main__":
    keywords = 'lofa'
    operate(keywords)