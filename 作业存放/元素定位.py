from selenium import webdriver
from selenium.webdriver.common.by import By
import time
dr =webdriver.Firefox()
dr.maximize_window()
dr.get("file:///C:/Users/Administrator/Desktop/abc.html")

dr.find_element(By.ID,"userA").send_keys('admin')
dr.find_element(By.ID,'passwordA').send_keys('123456')
t = dr.find_element(By.ID,'emailA')
t.send_keys('1231312314')
dr.find_element(By.ID,'emailA').send_keys("31234@156.com")

time.sleep(3)

t.clear()
t.send_keys('55562254')

time.sleep(3)
dr.find_element(By.TAG_NAME,'buttpm').click()
time.sleep(1)

time.sleep(3)
dr.quit()