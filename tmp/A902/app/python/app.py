import requests

headers = {'Content-type': 'application/json; charset=utf-8','Accept':'application/json'}

url = 'http://test.andes-hub.com:8080/admin/admin/login'

r = requests.post(url, data='{"password":"123","accountName":"wuyao"}', headers=headers)
print(r.text)


