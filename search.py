from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager




o = Options()
o.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=o)


class SeleniumParser():
    def find_in_google(request):
            time.sleep(3)
            driver.get("https://www.google.co.uz/")

            find_info = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
            find_info.clear()
            find_info.send_keys(request + Keys.ENTER)


            list_of_all_links = []
            all_links = driver.find_elements(By.CLASS_NAME, "MjjYud")
            for i in all_links:
                a =  i.find_element(By.TAG_NAME, "a")
                list_of_all_links.append(a.get_attribute('href'))
            
            
            
            print(list_of_all_links)



SeleniumParser.find_in_google(input())


