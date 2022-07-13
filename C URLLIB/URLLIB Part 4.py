

import urllib.request
import urllib.parse
import re

#Source: https://www.geeksforgeeks.org/python-parse-a-website-with-regex-and-urllib/?ref=rp


url = 'https://www.geeksforgeeks.org/'
#a
values = {'s':'python programming',
          'submit':'search'}

#b
data = urllib.parse.urlencode(values)
print (data)
#c
data = data.encode('utf-8')
print (data)
#d
req = urllib.request.Request(url, data)
#e
resp = urllib.request.urlopen(req)

respData = resp.read()
#2
#print (respData)		#gives messy printing

#3
paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

for eachP in paragraphs:
    print(eachP)
