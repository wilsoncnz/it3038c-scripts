import requests
import json


r = requests.get('http://localhost:3000')
data = r.json()

for x in range(len(data)):
    print(data[x]['name'].capitalize() + ' is ' +data[x]['color'] + ".")


