#pip install requests
import requests
# source: https://www.youtube.com/watch?v=a6fIbtFB46g


#1
res =requests.get('https://api.github.com')
print(res)
print (res.status_code)
print (res.ok)

#2
#res =requests.get('https://stamapi.github.com')
#print(res)
#print (res.status_code)

#3

if res:                 # could mean: 200, 204, 304 etc
    print("Success")
else:
    print("Ba'aya")

if res.status_code == 200:
    print('Success!')
elif res.status_code == 404:
    print('Not Found.')

