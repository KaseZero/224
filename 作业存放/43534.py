import requests
url = "http://127.0.0.1:8000/api/student/dashboard/index"
cookies = {"JSESSIONID":"OUc_QwCmssTZkX93CV8ckEQZAYS_vvcHFop5h1Q"}
res = requests.post(url=url, cookies=cookies)
print(res.txt)