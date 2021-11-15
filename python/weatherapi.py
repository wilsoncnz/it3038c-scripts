import requests
import json

print('Please enter your zip code: ')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s&appid=006c67779e426d7f767583d4fb6600db' % zip)
data = r.json()

print("The weather in %s is %s" % (zip, data['weather'][0]['description']))