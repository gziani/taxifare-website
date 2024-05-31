import streamlit as st
import datetime
import pandas as pd
import numpy as np
import requests

'''
# NY TaxiFare prediction app (in progress)
'''

#st.markdown('''
#Remember that there are several ways to output content into your web page...
#
#Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
#''')
#
#'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride
#
#1. Let's ask for:
#- date and time
#- pickup longitude
#- pickup latitude
#- dropoff longitude
#- dropoff latitude
#- passenger count
#'''

date = st.date_input(
    "Pickup day:",
    datetime.datetime.today())

time = st.time_input(
    "Pickup time:",
    datetime.datetime.today())



map_data = pd.DataFrame([[40.7, -74.0]],
            columns=['lat', 'lon']
        )

st.map(data=map_data, latitude='lat', longitude='lon', color=(0,0,0,1), size=None, zoom=10, use_container_width=True)




#'''
## Once we have these, let's call our API in order to retrieve a prediction
#
#See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...
#
#🤔 How could we call our API ? Off course... The `requests` package 💡
#'''

url = 'https://taxifare.lewagon.ai/predict'


#if url == 'https://taxifare.lewagon.ai/predict':
#    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')



##2. Let's build a dictionary containing the parameters for our API...

inputs = {'pickup_datetime': f"{date} {time}",
        'pickup_longitude': -73.950655,
        'pickup_latitude': 40.783282,
        'dropoff_longitude': -73.984365,
        'dropoff_latitude': 40.769802,
        'passenger_count': 2}

##3. Let's call our API using the `requests` package...

response = requests.get(url, params=inputs)
pred = response.json() #=> {wait: 64}

##4. Let's retrieve the prediction from the **JSON** returned by the API...
pred_display = f"${round(pred['fare'],2)}"

## Finally, we can display the prediction to the user
st.metric("Expected fare", pred_display, "")
