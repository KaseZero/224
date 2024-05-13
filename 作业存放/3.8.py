from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.action_chains import ActionChains

dr = webdriver.Firefox()
dr.get("file:///C:/Users/Administrator/Desktop/abc.html")
time.sleep(2)

ac=ActionChains(dr)
user = dr.find_element(By.ID,"userA")

ac.context_click(user).perform()
time.sleep(2)
user.send_keys("admin")
time.sleep(1)
a= dr.find_element(By.XPATH,".//*[@id='zc]/filedset/buttom")

ac.move_to_element(a).perform()
time.sleep(2)

ac.move_by_offset(100,300).perform()
time.sleep(2)
dr.quit()

