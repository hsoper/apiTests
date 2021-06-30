import requests
import json
from pycoingecko import CoinGeckoAPI
import pandas as pd
from sqlalchemy import create_engine
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()['bpi']['USD']['rate']
h = CoinGeckoAPI()
data = h.get_price(ids='dogecoin', vs_currencies='usd')['dogecoin']['usd']
coins = h.get_price(ids='ethereum,monero,tether', vs_currencies='usd')
print(coins)
coin = []
priceUSD = []
for key, usd in coins.items():
    coin.append(key)
    for k, i in usd.items():
        priceUSD.append(float(i))
user = input("What cryptocurrency's price do you want to know?\n")
user = user.lower()
coins = h.get_price(ids=user, vs_currencies='usd')
for key, item in coins.items():
    if key == user:
        coin.append(key)
        priceUSD.append(float(item['usd']))
print(coin, f"\n{priceUSD}")
dcoins = {"Coin":coin, "PriceUSD":priceUSD}
dcoins = pd.DataFrame.from_dict(dcoins)
print(dcoins)
engine = create_engine('mysql://root:codio@localhost/Crypto')
dcoins.to_sql('CoinPrices', con=engine, if_exists='replace', index=False)
