import json
import requests
import streamlit as st


def response_from_api():
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    if response.status_code == 200:
        response_in_json = response.json()
        rates_dict = response_in_json['rates']
    else:
        return response.status_code
    return rates_dict





