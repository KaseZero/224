import requests,json
url = 'http://192.168.55.2:8000/api/user/login'
data={"userName":"student","passward":"123456","remember":False}
r =requests.post(url,jason=data)
c =r.cookies

url = 'http://192.168.55.2:8000/api/student/dashboard/index'
r1 =requests.post(url,cookies=c)
print(r1.txt)