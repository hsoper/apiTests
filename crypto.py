import requests
import json
import pandas as pd
from sqlalchemy import create_engine

baseURL = 'https://api.coingecko.com/api/v3/simple/price?ids='

def get_coingecko_json(coin):
  response = requests.get(baseURL+coin+'&vs_currencies=usd')
  print(response.status_code)
  return response.json()


def get_names_and_usd(json):
    temp = [[],[]]
    for key, usd in json.items():
        temp[0].append(key)
        for k, i in usd.items():
            temp[1].append(float(i))
    return temp

  
def get_users_coinusd():
    user = input("What cryptocurrency's price do you want to know?\n")
    user.lower()
    x=0
    js = get_coingecko_json(user)
    return js

  
def append_json_values(lis,json):
    temp = get_names_and_usd(json)
    for i in range(0,len(temp)):
        for x in temp[i]:
            lis[i].append(x)
    return lis

  
def make_dataframe(lis):
    dcoins = {"Coin": coin_usd[0], "PriceUSD": coin_usd[1]}
    dcoins = pd.DataFrame.from_dict(dcoins)
    return dcoins

def sendto_database(datafr,database,table):
    engine = create_engine('mysql://root:codio@localhost/'+database)
    datafr.to_sql(table, con=engine, if_exists='replace', index=False)
    
    
coins = get_coingecko_json('ethereum,monero,tether')
coin_usd = get_names_and_usd(coins)
coin_usd = append_json_values(coin_usd,get_users_coinusd())
dcoins = make_dataframe(coin_usd)
print(dcoins)
sendto_database(dcoins,engine,'CoinPrices')