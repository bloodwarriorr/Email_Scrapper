import urllib.request
import urllib.parse as urlparse
import re

url = 'https://www.example.com/?q=abc&p=123'
params = urlparse.parse_qs(urlparse.urlparse(url).query)

print (params['q'][0])
print (params['p'][0])

