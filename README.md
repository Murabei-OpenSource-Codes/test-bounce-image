# test-bounce-image
Dummy image that returns request data with headers and other
request information. It can be used to check service mesh redirection
to correct micro-services.



# Usage
It is possible to deploy image using docker compose.
```
version: '3'
services:
  #################
  # Load Balancer #
  bounce-request:
    image: docker.io/andrebaceti/bounce-request-test-image:0.0
    ports:
      - "8080:5000"
```

## Examples of call return:

### Get request:
```
In [8]: requests.get("http://localhost:8080").json()
Out[8]:
{'headers': {'Accept': '*/*',
  'Accept-Encoding': 'gzip, deflate',
  'Connection': 'keep-alive',
  'Host': 'localhost:8080',
  'User-Agent': 'python-requests/2.31.0'},
 'host': 'localhost:8080',
 'method': 'GET',
 'path': '',
 'request_data': None,
 'url': 'http://localhost:8080/'}
```

### POST request:
```
In [9]: requests.post("http://localhost:8080", json={"teste": 1}).json()
Out[9]:
{'headers': {'Accept': '*/*',
  'Accept-Encoding': 'gzip, deflate',
  'Connection': 'keep-alive',
  'Content-Length': '12',
  'Content-Type': 'application/json',
  'Host': 'localhost:8080',
  'User-Agent': 'python-requests/2.31.0'},
 'host': 'localhost:8080',
 'method': 'POST',
 'path': '',
 'request_data': {'teste': 1},
 'url': 'http://localhost:8080/'}
```
