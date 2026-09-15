from urllib.parse import urlparse

url = "https://docs.python.org/3/library/datetime.html"

result = urlparse(url)

print(result)