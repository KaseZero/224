import requests
url = "http://baidu.com/get"
res = requests.get(url)
print(res.text)

#存储图片
url='https://static.oschina.net/uploads/cooperation/index_channel_list_ad_between_gitee_jRqtJ.jpg'
r = requests.get(url)
content =r.content
with open('1.jpg','wb') as f:
    f.write(content)
print('图片下载成功！')

#异常处理
from requests.exceptions import Timeout
try:
    response = requests.get('https://www.testwo.com', timeout=0.1)
    print(response.status_code)
except Timeout:
    print("请求超时,请重试。")