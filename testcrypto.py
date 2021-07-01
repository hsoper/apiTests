import unittest
import requests
import pandas as pd
from crypto import get_coingecko_json, get_names_and_usd
from crypto import make_dataframe, append_json_values

class TestFileName(unittest.TestCase):
    # The function should not return an empty string. 
    # Might add some default crypto the users as 
    # input if the user inputs an invalid 
    def test_get_coingecko_json(self):
        baseURL = 'https://api.coingecko.com/api/v3/simple/price?ids='
        response = requests.get(baseURL+"coin" + '&vs_currencies=usd')
        self.assertNotEqual(get_coingecko_json("invalid"), response.json() )
        self.assertNotEqual(get_coingecko_json(2424), response.json() )
        self.assertNotEqual(get_coingecko_json(None), None )


    # The function should not return an empty list.
    def test_get_names_and_usd(self):
        baseURL = 'https://api.coingecko.com/api/v3/simple/price?ids='
        response = requests.get(baseURL+"coin"+'&vs_currencies=usd')
        self.assertNotEqual(len(get_names_and_usd(response.json())[0]), 0)
        self.assertNotEqual(len(get_names_and_usd(response.json())[1]), 0)


    #method should always return whatever the json file is going to append
    #even if the user doesn't input a correct list format
    def test_append_json_values(self):
        baseURL = 'https://api.coingecko.com/api/v3/simple/price?ids='
        response = requests.get(baseURL + "bitcoin" + '&vs_currencies=usd')
        temp = get_names_and_usd(response.json())
        self.assertEqual(append_json_values([[],[]], response.json()), temp)
        self.assertEqual(append_json_values("list", response.json()), temp)
        self.assertEqual(append_json_values(242, response.json()), temp)


    #Should return an empty dataframe if invalid inputs
    #tells the user
    def test_make_data_frame(self):
        l = [[]]
        self.assertEqual(make_dataframe(l), pd.DataFrame.from_dict({}))
        self.assertEqual(make_dataframe(1), pd.DataFrame.from_dict({}))
        self.assertEqual(make_dataframe("hello"), pd.DataFrame.from_dict({}))


if __name__ == '__main__':
    unittest.main()
