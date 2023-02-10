import streamlit as st
import numpy as np
import pandas as pd

st.sidebar.success("Nanti Fitur kita masukan sini")
st.title('Simulation Prediction Wave Energy Potential with Machine Learning')
st.text('LKTC Tanker Goes to Bali\n')

# metric hasil
mtr1, mtr2, mtr3  = st.columns(3)
mtr1.metric("Potensi", "100 MW", "24 MW")
mtr2.metric("Kecepatan Gelombang", "10 mps", "-2 mph")
mtr3.metric("Kecapatan angin", "32 mps", "-9 mph")

# contoh raw data/data set
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! nanti kita cari datasetnya")

if st.checkbox('Contoh dataset'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Testing histogram')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Modelling Mapping %s:00' % hour_to_filter)
st.map(filtered_data)