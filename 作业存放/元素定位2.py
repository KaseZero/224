from selenium import webdriver
from selenium.webdriver.common.by import By
import time

dr = webdriver.Firefox()
dr.maximize_window()
dr.get('http://192.168.55.67/')
t_l=['admin','123456','12134134234']
inp= dr.find_element(By.XPATH,".//*[@id='zc']/foe;dest/p/input")
for i in inp:
    print(i.get_attribute('id'))
time.sleep(3)
dr.quit()