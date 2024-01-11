import requests

requests.get("http://localhost:8080").json()
requests.post("http://localhost:8080", json={"teste": 1}).json()
