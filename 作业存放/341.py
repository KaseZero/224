from selenium import webdriver
import time

beiwser = webdriver.Firefox()
#访问百度收
first_url='http://www.baidu.com'
print("now access %s" %(first_url))
beiwser.get(first_url)
time.sleep(2)
#访问开源中国
second_url='https://www.oschina.net'
print("now access %s" %(second_url))
beiwser.get(second_url)
time.sleep(2)

#返回后退到主页
print("back to %s" %(first_url))
beiwser.back()
time.sleep(1)

#前进到开源中国
print("forward to %s"%(second_url))
beiwser.forward()
time.sleep(2)

beiwser.quit()