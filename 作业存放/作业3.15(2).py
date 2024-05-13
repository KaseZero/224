from selenium import webdriver
import time

from selenium.webdriver.common.by import By
dr=webdriver.Firefox()
url="http://localhost:8080/p2p_management/"
dr.get(url)
dr.find_element(By.NAME,'username')
dr.find_element(By.NAME,'password')
dr.find_element(By.XPATH,".//*[@id='login']/div[4]/input").click()
time.sleep(2)

dr.find_element(By.XPATH,"html/body/div[2]/div[2]/div[6]/div/div/div[1]/div[2]/div[1]/div").click()
dr.find_element(By.XPATH,".//*[@id='proNum']").send_keys("2224")
dr.find_element(By.XPATH,".//*[@id='proName']").send_keys("1111")
dr.find_element(By.XPATH,".//*[@id='proLimit']").send_keys("2222")
dr.find_element(By.XPATH,".//*[@id='annualized']").send_keys("3333")
dr.find_element(By.ID,'saveBtn').click()
time.sleep(2)
dr.quit()
