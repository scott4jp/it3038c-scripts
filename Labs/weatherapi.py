import json
import requests 

print('Pease enter you zip code: ')
zip = input()


r = requests.get('https://api.openweathermap.org/data/2.5/weather?zip=%s&appid=2549a390643decdeee07d6d1b98e14bf' % zip)

data = r.json

print(data['weather'][0]['description'])