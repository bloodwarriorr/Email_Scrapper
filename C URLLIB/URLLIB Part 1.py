import urllib
import urllib.request
import urllib.parse

#Source: https://www.geeksforgeeks.org/python-urllib-module/

#0
print (dir(urllib))

#1
x = urllib.request.urlopen('https://google.com')
print (x)
print(x.read())

#2
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()



#3 - URL Error
try:
    #3a
    x = urllib.request.urlopen('https://www.googleeee.com')
    #3b
    #x = urllib.request.urlopen('https://www.google.com / search?q = test')
    print(x.read())

# Catching the exception generated
except Exception as e:
    print("This is the shgia:", str(e))


