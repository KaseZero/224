import requests
url = "http://www.bilibili.com"
r=requests.get(url)
print(r.text)
print(r.url)
print(r.status_code)

 