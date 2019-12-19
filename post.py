import requests

url = 'http://localhost:5000/api'

r = requests.posts(url,json={'exp':75,})
print(r.json())
