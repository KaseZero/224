from selenium import webdriver
from selenium.webdriver.common.by import By
import time

dr = webdriver.Firefox()
dr.get("")
dr.implicitly_wait(3)
dr.find_element(By.ID,'userA').send_keys('admin')
dr.find_element(By.ID,"passwordA").send_keys("123456")
dr.find_element(By.ID,"telA").send_keys("12133131")
dr.find_element(By.ID,"emailA").send_keys("123@qq.com")
imghdr = time.strftime("%y%m%d_%H%m%S")

dr.get_screenshot_as_file("img.jpg")
dr.quit()