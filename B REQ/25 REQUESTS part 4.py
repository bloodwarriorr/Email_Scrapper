import requests

#1
r = requests.get('https://xkcd.com/353/')
#print(r)
#a
#print (dir(r))
#b
#print (help(r))
#c
#print (r.text)


#grab image 
r = requests.get('https://imgs.xkcd.com/comics/salary_negotiation.png')
#print (r.content)
#a
with open ('comic.png', 'wb') as f:
    f.write(r.content)              #saves img as file
#b
print (r.headers)



#3
#site httpbin.org
# running: https://httpbin.org/get?page=2&count=25

#a
payload = {'page':2, 'count':25}
#b
r = requests.get('https://httpbin.org/get', params=payload)
print (r.text)
#c
print(r.url)


#4
#a
payload = {'username':'cohen', 'password':'qwerty132'}
r = requests.post('https://httpbin.org/post', data=payload)
print (r.text)
#b
print (r.url)
#c
print (r.json())
#d
r_dict = r.json()
print(r_dict['form'])


#5
#basic authentication
#a
# get in the page: https://httpbin.org/basic-auth/cohen/qwerty123

#b
r = requests.get('https://httpbin.org/basic-auth/cohen/qwerty123',auth=('cohen','qwerty123'))
print(r.text)
#c
r = requests.get('https://httpbin.org/basic-auth/cohen/qwerty123',auth=('stam','qwerty123'))
print (r.text)
#d
print (r)


#6
r = requests.get('https://httpbin.org/delay/1', timeout=3)
print(r)
r = requests.get('https://httpbin.org/delay/10', timeout=3)
print(r)

