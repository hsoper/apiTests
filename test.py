import requests
import json
from pycoingecko import CoinGeckoAPI
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()['bpi']['USD']['rate']
print('This is the current bitcoin price according to coindesk :', data)
h = CoinGeckoAPI()
data = h.get_price(ids='dogecoin', vs_currencies='usd')['dogecoin']['usd']
print("This is the current dogecoin price according to CoinGecko : ",data)
print('These are the current ethereum' +
      'monero, and tether prices according to CoinGecko')
coins = h.get_price(ids='ethereum,monero,tether', vs_currencies='usd')
monero = coins['monero']['usd']
ethereum = coins['ethereum']['usd']
tether = coins['tether']['usd']
print("Ethereum price: ", ethereum)
print("Monero price: ", monero)
print("Tether price: ", tether)
user = input("What cryptocurrency's price do you want to know?\n")
user = user.lower()
coins = h.get_price(ids=user, vs_currencies='usd')
coin = "No cryptocurrency entered."
for key,item in coins.items():
    if key == user:
        coin = f"{user.upper()[0:1]+user[1:]} price : {coins[user]['usd']}"
print(coin)
