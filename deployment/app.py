import streamlit as st
import eda 
import prediction


navigation = st.sidebar.selectbox('Pilihan Halaman : ', ('EDA', 'Predict Plant Nutrition'))


if navigation == 'EDA':
    eda.run()
else:
    prediction.run()
    
