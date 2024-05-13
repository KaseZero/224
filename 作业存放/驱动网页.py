from selenium import webdriver
from selenium.webdriver.common.by import By
import time

dr = webdriver.Firefox()
dr.get("file:///C:/Users/Administrator/Desktop/abc.html")
time.sleep(2)

#usa=dr.find_element_by_id("userA")
#dr.find_element(By.ID)
#dr.quit()
tel =dr.find_element(By.CLASS_NAME,"telA")
tel.send_keys('12312312312312312')
time.sleep(2)

inp=dr.find_element(By.TAG_NAME,"input")
inp.send_keys('admin')
time.sleep(2)
dr.quit()