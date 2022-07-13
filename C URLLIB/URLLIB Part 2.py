#from urllib.parse import urlparse
import urllib.parse


#3
url = 'https://finviz.com/screener.ashx?v=111&f=idx_sp500'
parsed = urllib.parse.urlparse(url)
print("#3 - This is the parsed url:", parsed)


#4
print("\n#4")
#url = 'http://user:pwd@NetLoc:80/path;param?query=arg#frag'
url = 'https://finviz.com/screener.ashx?v=111&f=idx_sp500'
parsed = urllib.parse.urlparse(url)
print('scheme  :', parsed.scheme)
print('netloc  :', parsed.netloc)
print('path    :', parsed.path)
print('params  :', parsed.params)
print('query   :', parsed.query)
print('fragment:', parsed.fragment)
print('username:', parsed.username)
print('password:', parsed.password)
print('hostname:', parsed.hostname)
print('port    :', parsed.port)


#5

import urllib.parse
parsed = urllib.parse.urlsplit('http://user:pass@NetLoc:80/path;parameters/path2;parameters2?query=argument#fragment')
print("The whole thing gives:\n")
print ("\n#5", parsed)
print("------")
print( 'scheme  :', parsed.scheme)
print( 'netloc  :', parsed.netloc)
print( 'path    :', parsed.path)
print( 'query   :', parsed.query)
print( 'fragment:', parsed.fragment)
print( 'username:', parsed.username)
print( 'password:', parsed.password)
print( 'hostname:', parsed.hostname, '(netloc in lower case)')
print( 'port    :', parsed.port)

