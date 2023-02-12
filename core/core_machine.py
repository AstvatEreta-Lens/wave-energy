import streamlit as st
import numpy as np
import pandas as pd

# Title
st.title('Counting App Ocean Wave Power')
st.text('By Student of Pertamina University\n')

# Sidebar
with st.sidebar:
    side_title = st.success("Input the Parameters")
    v_arus_laut = st.number_input("Kecepatan Arus laut (m/s)")
    # gaya hidrodinamik
    kerapatan_massa = st.slider("Kerapatan Massa Ai (kg/m^3)", 1000, 1100 )
    A_luas_penampang = st.number_input("Luas Penampang(m^2)")
    Efisiensi_turbin = st.slider("Efisiensi(%)", 0.0, 100.0)
 
# Operation
daya_listrik_arus = 0.5*kerapatan_massa*A_luas_penampang*abs(v_arus_laut**3)*(Efisiensi_turbin/100)

# metric hasil
mtr1, mtr2, mtr3  = st.columns(3)
mtr1.metric("Daya", daya_listrik_arus)
mtr2.metric("Efisiensi", Efisiensi_turbin )
mtr3.metric("Kecapatan Arus", v_arus_laut )

# Save data
save_value = st.button("save")

#chart






