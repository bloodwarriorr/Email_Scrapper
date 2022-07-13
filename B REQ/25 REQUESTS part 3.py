import requests


response = requests.get('https://api.github.com')

#1
print("\n-----\nByte-string")
print(response.content)

#2
print("\n-----\nText")
print(response.text)

#3
#print("\n-----\nutf-8")
#response.encoding = 'utf-8'

#4
print("\n-----\njson")
print(response.json())
