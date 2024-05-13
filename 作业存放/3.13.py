from selenium import webdriver
import time
from selenium.webdriver.common.by import By
dr=webdriver.Firefox()
dr.implicitly_wait(2)

but1=dr.find_element(By.XPATH,'html/body/input[1]')
but2=dr.find_element(By.XPATH,'html/body/input[2]')
but3=dr.find_element(By.XPATH,'html/body/input[2]')

but1.click()
al = dr.switch_to.alert
print(al.text)
time.sleep(1)
al.accept()

but2.click()
time.sleep(1)
al2= dr.switch_to.alert
print(al2.text)
al2.dismiss()

but3.click()
time.sleep(1)
alt3=dr.switch_to.alert
print(alt3.text)
al3.accept()

