from selenium import  webdriver

webdriver = webdriver.Firefox()
webdriver.get("http://192.168.55.41:8081/p2p_management/")

cookie= webdriver.get_cookies()
print(cookie)
webdriver.quit()