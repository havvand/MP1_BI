import requests
import pandas as pd
import io


# ----------------- For a GET request, the data is a list of query parameters -----------------
""" This method is for a GET request. The variable parameters contains the query parameters. 
    The function get_request takes the url and adds the parameters to the url.
    The response is then returned and the csv data is decoded and returned as a string."""

def get_request(url, params):
    for i in range(len(params)):
        url += params[i]

    print(url, "TESTING URL")
    response = requests.get(url)
    csv_data = response.content.decode("utf-8")
    return io.StringIO(csv_data)


# ------------------- For a POST request-----------------
""" This method is for a POST request. The variable parameters contains an array with the query parameters, 
    which are used in the JSON_POST_request function.
    The function JSON_POST_request takes the url, table, format and variables as arguments."""


def JSON_POST_request(url, table, format, variables):
    request_json = {
        "table": table,
        "format": format,
        "variables": variables
    }

    response = requests.post(url, json=request_json)
    csv_data = response.content.decode("utf-8")
    return io.StringIO(csv_data)