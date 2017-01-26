import requests
import json
import time
import grequests

startTime = time.time()

BASE_JSON = 'https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/index.json'

BASE_URL = 'https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/'

FILE = '/current/index.json'

aws_json = requests.get(url=BASE_JSON).json()

prices = aws_json['offers']
services = []
services_urls = []
services_json = []

for price in prices:
    services.append(price)

for service in services:
    services_urls.append(BASE_URL + service + FILE)

rs = (grequests.get(u) for u in services_urls)

responses = grequests.map(rs)

for r in responses:
    services_json.append(r.json())

with open('services.json', mode='w', encoding='utf-8') as out:
    json.dump(services_json, out, indent=2, sort_keys=True)

print('The script took {0} second!'.format(time.time() - startTime))
