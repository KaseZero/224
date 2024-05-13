import requests
import  json

url = "http://nttpbin.org/post"
data = {
    "name" : "VAn",
    "age": "114514"
}
herders = {"Content-Type":"application/json"}
res = requests.post(url=url, data=json.dumps(data), headers=herders)
print(res.txt)
