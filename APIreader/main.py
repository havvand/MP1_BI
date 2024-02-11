import pprint

import API_reader as API
import pandas as pd
import requests
import numpy as np

url = "https://api.statbank.dk/v1/data"

# This is to get an overview of the codes used only in the ERHV1 table.
# For other tables the codes will be different.
erhv1_codes = pd.read_csv("data/ERHV1.csv", sep=';')

meta_data = requests.get("https://api.statbank.dk/v1/tableinfo/erhv1").json()
print(type(meta_data))
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(meta_data)

# CSV GET request
"""
parameters = [
    "/ERHV1",
    "/CSV?",
    "BRANCHE07=",
    "011100",
    "&TAL=",
    "ANSATTE"
]

df_csv = pd.read_csv(API.get_request(url, parameters), sep=';')
print("TYPE: ", type(df_csv))
print(df_csv)

# JSON POST request

variables = [
             {"code": "BRANCHE07", "values": ["620100", "620200", "602000"]},
             {"code": "tid", "values": ["2020", "2021", "2022"]},
             {"code": "TAL", "values": ["ARBSTED","ANSATTE"]}
            ]

data = API.JSON_POST_request(url, "ERHV1", "CSV", variables)

print(type(data))

df = pd.read_csv(data, sep=';')
print(df)
"""
