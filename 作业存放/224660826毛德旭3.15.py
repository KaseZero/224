import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
dr=webdriver.Firefox()
url="http://192.168.55.62"
dr.get(url)
time.sleep(2)
zto=dr.find_element(By.ID,"zentao")
zto.click()
time.sleep(2)
acc=dr.find_element(By.ID,"account")
acc.send_keys("admin")
time.sleep(1)
pas=dr.find_element(By.NAME,"password")
pas.send_keys("Abc123456")
time.sleep(2)
sub=dr.find_element(By.ID,"submit")
sub.click()
time.sleep(1)
dr.find_element(By.XPATH,".//*[@id='navbar']/ul/li[4]/a").click()
time.sleep(1)
dr.find_element(By.XPATH,".//*[@id='subNavbar']/ul/li[1]/a").click()
time.sleep(1)
dr.find_element(By.XPATH,".//*[@id='mainMenu']/div[3]/a[3]/i").click()
time.sleep(1)
dr.maximize_window()
dr.find_element(By.XPATH,".//*[@id='openedBuild_chosen']/ul").click()
time.sleep(1)
dr.find_element(By.XPATH,".//*[@id='openedBuild_chosen']/div/ul/li[1]").click()
time.sleep(1)
dr.find_element(By.ID,"title").send_keys("admin")
time.sleep(1)
dr.find_element(By.ID,"submit").click()
time.sleep(5)
dr.find_element(By.XPATH,".//*[@id='userNav']/li/a/span[1]").click()
time.sleep(2)
dr.find_element(By.XPATH,".//*[@id='userNav']/li/ul/li[13]/a").click()
time.sleep(2)
dr.quit()

