from selenium import webdriver
import time
#創建瀏覽器對綫
driver =webdriver.Firefox()
#dr.get
driver.get("http://192.168.55.67")
#获取页面尺寸
size = driver.get_window_size()
print(size)
#设置窗口i页面大小
driver.set_window_size(800, 900)
#关闭浏览器窗口
#driver.close()
#关闭所有浏览器窗口
#driver.quit()

#获取浏览器位置
position = driver.get_window_position()
print(position)
#设置浏览器位置
driver.set_window_position(100, 100)