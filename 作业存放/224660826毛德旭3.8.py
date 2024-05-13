from selenium import webdriver
import time
from selenium.webdriver.common.by import By
dr=webdriver.Firefox()
url="http://192.168.55.62"
dr.get(url)
time.sleep(2)
dr.find_element(By.ID,"zentao").click()
time.sleep(2)
dr.find_element(By.ID,"account").send_keys("admin")
dr.find_element(By.NAME,"password").send_keys("Abc123456")
time.sleep(2)
dr.find_element(By.ID,"submit").click()
time.sleep(3)
dr.find_element(By.XPATH,".//*[@id='navbar']/ul/li[4]/a").click()
time.sleep(2)
dr.find_element(By.XPATH,".//*[@id='subNavbar']/ul/li[1]/a").click()
time.sleep(3)
jk=dr.find_elements(By.XPATH,".//*[@id='bugList']/tbody/tr/td[5]")
for i in jk:
    print(i)
dr.find_element(By.CLASS_NAME,"user-name").click()
time.sleep(3)
jo = dr.find_element_by_xpath(".//*[@id='userNav']/li/ul/li[13]/a")
jo.click()
dr.quit()
