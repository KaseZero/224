import requests

url = "http://127.0.0.1:8000/api/user/login"
data = {"userName": "student","passward": "123456"}
s = requests.session()
s.port(url=url, json=data)
res = s.port("http://127.0.0.1:8000/api/student/dashboard/index")
print(res.text)