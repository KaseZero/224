from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

dr =webdriver.Firefox()
dr.get('file:///C:/Users/Administrator/Desktop/abc.html')

user = webdriver(dr,5).until(EC.presence_of_element_located(By.ID,"userA"))

dr.quit()