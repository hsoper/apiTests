import requests
import json
import pandas as pd
from sqlalchemy import create_engine


# Test when if the input is a supported crypto in the correct format
# Check for null inputs
def get_coingecko_json(coin):
    baseURL = ('https://api.coingecko.com/'
               + 'api/v3/simple/price?ids=')
    response = requests.get(baseURL + str(coin) + '&vs_currencies=usd')
    if response.json() == requests.get(baseURL+'w'+'&vs_currencies=usd').json():
        print("That is not a valid crypto name. Heres the value of bitcoin")
        return requests.get(baseURL + "bitcoin" + '&vs_currencies=usd').json()
    return response.json()


# check if the function returns a 2d array and not a none object
def get_names_and_usd(json):
    temp = [[], []]
    for key, usd in json.items():
        temp[0].append(key)
        for k, i in usd.items():
            temp[1].append(float(i))
    return temp


# deleted get_get_users_coinusd() since its
# function is similar to get_coingecko_json()
# check when the input is a null for the list
# check when the json file is empty
def append_json_values(lis, json):
    temp = get_names_and_usd(json)
    if type(lis) is not list:
        return temp
    for i in range(0, len(temp)):
        for x in temp[i]:
            lis[i].append(x)
    return lis


# check when the input is an empty list/invalid
# check when when the list contains the wrong types. (not a string or float)
def make_dataframe(coin_usd):
    if type(coin_usd) is not list:
        print("Sorry that is not a valid input. Your input will be returned.")
        return coin_usd;
    if (len(coin_usd) != 2 or type(coin_usd[1]) is not list
        or type(coin_usd[0]) is not list):
        print("Sorry that is not a valid input. Your input will be returned.")
        return coin_usd;
    dcoins = {"Coin": coin_usd[0], "PriceUSD": coin_usd[1]}
    dcoins = pd.DataFrame.from_dict(dcoins)
    return dcoins


# no return value
# Possibly check the inputs of the method
def sendto_database(datafr, database, table):
    engine = create_engine('mysql://root:codio@localhost/' + database)
    datafr.to_sql(table, con=engine, if_exists='replace', index=False)


# coins = get_coingecko_json('ethereum,monero,tether')
# coin_usd = get_names_and_usd(coins)
# coin_usd = append_json_values(coin_usd, get_users_coinusd())
# dcoins = make_dataframe(coin_usd)
# print(dcoins)
# sendto_database(dcoins, "crypto", 'CoinPrices')
