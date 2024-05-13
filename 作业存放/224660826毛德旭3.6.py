from selenium import webdriver
from selenium.webdriver.common.by import By
import time

dr = webdriver.Firefox()
dr.get("http://192.168.55.67")
time.sleep(2)


usa=dr.find_element_by_id("zentaoo")
usa.send_keys('zentao')

#定位密码
pas = dr.find_element(By.ID,"passwordA")
#输入
pas.send_keys("")
pas.click()
time.sleep(2)
dr.quit(3)

tel =dr.find_element(By.CLASS_NAME,"telA")
tel.send_keys('')
time.sleep(2)

inp=dr.find_element(By.TAG_NAME,"input")
inp.send_keys('admin')
time.sleep(2)
dr.quit()