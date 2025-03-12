import time
from asyncio import sleep
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException

service = Service("C:\\Users\\damnb\\OneDrive\\Masaüstü\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://www.elitedivingcentre.com.tr")
driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(2)
element = driver.find_element(By.XPATH, "(//a[@itemprop='url'])[4]")
element.click()
driver.execute_script("window.scrollBy(0, 1200);")
time.sleep(5)
# date = driver.find_element(By.XPATH,"(//button[@class='wte-fsd__button'])[0]")
# date.click()
time.sleep(5)
book_now = driver.find_element(By.XPATH,"(//div[@class='wte-fsd__availability-cta-wrap'])[8]")
book_now.click()
time.sleep(3)
# devam_butonu = driver.find_element(By.XPATH,"(//button[@class='wte-process-btn-next'])")
# devam_butonu.click()
input()
# time.sleep(5)