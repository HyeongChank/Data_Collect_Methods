from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from datetime import datetime


def operate(keywords):

    for i in range(30):
        service = ChromeService()
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("http://www.google.com")
        search_box = driver.find_element(By.NAME, "q")

        search_box.send_keys(keywords)
        search_box.submit()
    
        movescroll = driver.find_element(By.CSS_SELECTOR, 'body')
        movescroll.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        movescroll.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        movescroll.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        xpath = '//*[@id="arc-srp_110"]/div/div[3]/div/div/div[1]/div/div/span/a'
        # xpath = '//*[@id="rso"]/div[2]/div[4]/div/div/div/div[1]/div/div/span'

        driver.find_element(by=By.XPATH, value=xpath).click()
        time.sleep(5)
        driver.quit()
        c_time = datetime.now()
        y_time = c_time.year; m_time = c_time.month; d_time = c_time.day ; h_time = c_time.hour ; m_time = c_time.minute
        t = str(y_time) + '.' + str(c_time.month) + '.' + str(d_time) + '.' + str(h_time) + '.' + str(m_time)
        print(str(i+1) + '회')
        time.sleep(3)

if __name__=="__main__":
    keyword1 = 'lofa'
    # keyword2 = '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/span/a'
    # keywords = {'lofa':keyword1, 'lofa':keyword1}
    operate(keyword1)