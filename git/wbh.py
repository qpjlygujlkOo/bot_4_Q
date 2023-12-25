import requests

url = "https://smee.io/QhKDYlxvf38pJJ9/"

r = requests.post(url)
print(r.content)