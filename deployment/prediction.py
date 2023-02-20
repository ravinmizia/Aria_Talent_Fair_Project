import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json
import sklearn
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression,LinearRegression
from sklearn.ensemble import RandomForestClassifier
from PIL import Image



# Load the Files
with open('model.pkl', 'rb') as file_1:
  model = pickle.load(file_1)

with open('model_scaler.pkl', 'rb') as file_2:
  model_scaler = pickle.load(file_2)

with open('list_num_cols.txt', 'r') as file_4:
  list_num_cols = json.load(file_4)

with open('list_cat_cols.txt', 'r') as file_5:
  list_cat_cols = json.load(file_5)




def run():
       
  image = Image.open('ariaicon.png')
   
  col1, col2, col3 = st.columns(3)

  with col1:
        st.write(' ')
  with col2:
        st.image(image) 
  with col3:
        st.write(' ')


  st.write("## Insert variable's value ")

  st.markdown('***')

    # Membuat Form
  with st.form(key='form_parameters'):
        v3 = st.number_input(' V3', min_value=100, max_value=1000, value=300)
        v6 = st.number_input(' V6', min_value=100, max_value=1000, value=300)
        v7 = st.number_input(' V7', min_value=100, max_value=1000, value=300)
        v8 = st.number_input(' V8', min_value=2000, max_value=7500, value=2000)

        st.markdown('***')
      
        submitted = st.form_submit_button('Predict')
          

  data_inf = {
    'v3':v3,
    'v6':v6,
    'v7':v7,
    'v8':v8
    }


  data_inf = pd.DataFrame([data_inf])


  if submitted:
        
      data_inf_num = data_inf[list_num_cols]

      # Feature Scaling 
      data_inf_num_scaled = model_scaler.transform(data_inf_num)
          
      predicted_value=[]
      
      # Predict 
      y_pred_inf = model.predict(data_inf_num_scaled)

      predicted_value.append(y_pred_inf[0][0])

      data_inf['predicted_value'] = predicted_value

      st.dataframe(data_inf)

      print('Predicted Value :' , predicted_value)
