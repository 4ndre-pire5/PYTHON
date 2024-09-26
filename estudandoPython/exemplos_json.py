import json
import urllib.request

# obj = json.loads('{"gold": 1271, "silver": 1284, "platinum": 1270}')
# print(obj['gold'])

# url = "https://api.gdax.com/products/BTC-EUR/ticker"
# data = urllib.request.urlopen(url).read().decode()

# obj = json.loads(data)

# print('$' + obj['price'])
# print('$' + obj['volume'])

with open('teste.json', 'r') as myfile:
    data = myfile.read()

obj = json.loads(data)

print("usd: " + str(obj['usd']))
print("eur: " + str(obj['eur']))
print("gbp: " + str(obj['gbp']))

