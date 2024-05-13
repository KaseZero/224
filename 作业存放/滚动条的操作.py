import time
from selenium import  webdriver

webdriver = webdriver.firefox()
webdriver.set_window_size(500,600)

url =
webdriver.get(url)
time.sleep(1)

script = ""
webdriver.execute_script(script)
time.sleep(2)

script = ""
webdriver.execute_script(script)

time(2)
webdriver.quit()