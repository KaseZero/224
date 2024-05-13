from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.firefox()
url = 'file:///C:/Users/Administrator/Desktop/abc.html'
driver.get(url)

size=driver.find_element(By.ID,"userA").size
print('size:',size)

text=driver.find_element(By.ID,"fwA").text
print('a标签text:',text)

title=driver.title
print('title:',title)

url=driver.current_url
print('url:',url)

href=driver.find_element(By.ID,"")