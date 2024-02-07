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


def ui():
    st.markdown("<h1 style='background-color:cyan;text-align:center;color:white;'>Real-time currency converter</h1>",
                unsafe_allow_html=True)
    st.markdown("")
    api_data = response_from_api()
    if type(api_data) == dict:
        cols = st.columns(2)
        c1 = cols[0].selectbox("Convert from", api_data.keys())
        c2 = cols[1].selectbox("Convert to", api_data.keys())
        amount = cols[0].number_input("Amount", min_value=1)
        convfactor = api_data[c2] / api_data[c1]
        convertedamount = convfactor * amount
        amount_after_conversion = cols[1].number_input('Converted amount', value=convertedamount)
    else:
        st.error("There is an issue connecting to the API.")


if __name__ == '__main__':
    response_from_api()
    ui()


