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
    hitung = st.button('Hitung')
 
# Operation
daya_listrik_arus = 0.5*kerapatan_massa*A_luas_penampang*abs(v_arus_laut**3)*(Efisiensi_turbin/100)
if hitung :
    mtr1, mtr2, mtr3  = st.columns(3)
    mtr1.metric("Daya (watt)", daya_listrik_arus)   
    mtr2.metric("Efisiensi(%)", Efisiensi_turbin )
    mtr3.metric("Kecapatan Arus(m/s)", v_arus_laut )
    if daya_listrik_arus <= 1000:
        st.error("Daya listrik yang dihasilkan kurang dari standar dari sebuah pembangkit listrik.")
        st.text(""" Berikut beberapa saran:
         1. Optimalkan konfigurasi turbin: Desain dan konfigurasi yang tepat dapat 
            membantu meningkatkan efisiensi turbin dan meningkatkan daya listrik yang dihasilkan.
         2. Pemeliharaan rutin: Memastikan bahwa semua bagian turbin berfungsi dengan 
            baik dan bebas dari kerusakan dapat membantu meningkatkan daya listrik yang dihasilkan.
         3. Penggunaan material berkualitas tinggi: Menggunakan material berkualitas tinggi untuk
             membuat bagian-bagian turbin dapat membantu memastikan bahwa turbin berfungsi dengan 
             baik selama jangka waktu yang lama dan menghasilkan daya listrik yang optimal.
         4. Monitoring kondisi lingkungan: Memantau kondisi lingkungan seperti arus air, 
            gelombang, dan kondisi cuaca dapat membantu menentukan waktu yang tepat untuk 
            mengoperasikan turbin dan memaksimalkan daya listrik yang dihasilkan.
         5. Penggunaan teknologi baru: Penggunaan teknologi terbaru seperti teknologi
            optimasi turbin arus laut dapat membantu meningkatkan daya listrik yang dihasilkan
            dan memastikan bahwa turbin berfungsi dengan baik selama jangka waktu yang lama""") 
    elif daya_listrik_arus > 1000 and daya_listrik_arus < 10000:
        st.warning(""" Daya listrik yang dihasilkan cukup dari standar, berikut beberapa saran """)
    elif daya_listrik_arus >= 10000:
        st.success(""" Daya listrik yang dihasilkan melebihi standar, pertahankan segala aspek dan lakukanlah perawatan berkala terhadap segala perangkat """)

