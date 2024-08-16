import streamlit as st
import numpy as np
import datetime
import requests
import pandas as pd
'''
# TaxiFareModel front
'''

date = st.date_input("Date pickup")

time = st.time_input("Time pickup")

pickup_longitude = st.number_input('Insert your pickup longitude')

pickup_latitude = st.number_input('Insert your pickup latitude')

dropoff_longitude = st.number_input('Insert your dropoff longitude')

dropoff_latitude = st.number_input('Insert your dropoff latitude')

def passenger():
    passenger = np.arange(1, 5)
    return passenger
count = passenger()

passenger_count = st.selectbox("Select passenger count", count)

url = 'https://taxifare.lewagon.ai/predict'


dict_params = {"pickup_datetime": str(date) + " " + str(time),
               "pickup_longitude": pickup_longitude,
               "pickup_latitude": pickup_latitude,
               "dropoff_longitude": dropoff_longitude,
               "dropoff_latitude": dropoff_latitude,
               "passenger_count": passenger_count
               }

def map_data():
    return pd.DataFrame({"lon": [pickup_longitude, dropoff_longitude],
                         "lat": [pickup_latitude, dropoff_latitude]})

map = map_data()

'''
## Your travel
'''

st.map(map)

'''
## Your fare is
'''

result_api = requests.get(url, params=dict_params).json()

st.json(result_api)
