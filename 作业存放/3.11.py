#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/3/11 17:01
# Author    : smart
# @File     : 33.py
# @Software : PyCharm

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
dr = webdriver.Firefox()
dr.get("http://192.168.55.1/zentao/my/")

time.sleep(2)
user2 = dr.find_element(By.ID,"account")
user2.send_keys("admin")
time.sleep(2)

pwd = dr.find_element(By.NAME,"password")
pwd.send_keys("Abc123")


login = dr.find_element(By.ID,"submit")
login.click()
time.sleep(2)

ac = ActionChains(dr)

a = dr.find_element(By.XPATH,".//*[@id='navbar']/ul/li[1]/a/span")
ac.move_to_element(a).perform()
time.sleep(2)

b = dr.find_element(By.XPATH,".//*[@id='navbar']/ul/li[2]/a")
ac.move_to_element(b).perform()
time.sleep(2)

c = dr.find_element(By.XPATH,".//*[@id='navbar']/ul/li[3]/a")
ac.move_to_element(c).perform()
time.sleep(2)

d = dr.find_element(By.XPATH,".//*[@id='navbar']/ul/li[4]/a")
ac.move_to_element(d).perform()
time.sleep(2)

e = dr.find_element(By.XPATH,".//*[@id='navbar']/ul/li[6]/a")
ac.move_to_element(e).perform()
time.sleep(2)

f = dr.find_element(By.XPATH,".//*[@id='navbar']/ul/li[7]/a")
ac.move_to_element(f).perform()
time.sleep(2)

g = dr.find_element(By.XPATH,".//*[@id='navbar']/ul/li[8]/a")
ac.move_to_element(g).perform()
time.sleep(2)

h = dr.find_element(By.XPATH,".//*[@id='navbar']/ul/li[10]/a")
ac.move_to_element(h).perform()
time.sleep(2)

i = dr.find_element(By.XPATH,".//*[@id='navbar']/ul/li[11]/a")
ac.move_to_element(i).perform()
time.sleep(2)

aa = dr.find_element(By.XPATH,".//*[@id='subNavbar']/ul/li[1]/a")
ac.move_to_element(aa).perform()
time.sleep(2)

bb = dr.find_element(By.XPATH,".//*[@id='subNavbar']/ul/li[2]/a")
ac.move_to_element(bb).perform()
time.sleep(2)

cc = dr.find_element(By.XPATH,".//*[@id='subNavbar']/ul/li[4]/a")
ac.move_to_element(cc).perform()
time.sleep(2)

dd = dr.find_element(By.XPATH,".//*[@id='subNavbar']/ul/li[5]/a")
ac.move_to_element(dd).perform()
time.sleep(2)

ee = dr.find_element(By.XPATH,".//*[@id='subNavbar']/ul/li[6]/a")
ac.move_to_element(ee).perform()
time.sleep(2)

ff = dr.find_element(By.XPATH,".//*[@id='subNavbar']/ul/li[7]/a")
ac.move_to_element(ff).perform()
time.sleep(2)

gg = dr.find_element(By.XPATH,".//*[@id='subNavbar']/ul/li[9]/a")
ac.move_to_element(gg).perform()
time.sleep(2)

hh = dr.find_element(By.XPATH,".//*[@id='subNavbar']/ul/li[10]/a")
ac.move_to_element(hh).perform()
time.sleep(2)

ii = dr.find_element(By.XPATH,".//*[@id='subNavbar']/ul/li[12]/a")
ac.move_to_element(ii).perform()
time.sleep(2)

jj = dr.find_element(By.XPATH,".//*[@id='subNavbar']/ul/li[13]/a")
ac.move_to_element(jj).perform()
time.sleep(2)

kk = dr.find_element(By.XPATH,".//*[@id='subNavbar']/ul/li[14]/a")
ac.move_to_element(kk).perform()
time.sleep(2)

d=dr.find_element(By.CLASS_NAME,"user-name")
d.click()
time.sleep(2)

c=dr.find_element(By.PARTIAL_LINK_TEXT,"退出")
time.sleep(2)
c.click()
time.sleep(2)
dr.quit()