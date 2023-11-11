import streamlit as st
import pandas as pd
import joblib
with st.form("my_form"):
   st.write("# CEMENT STRENGTH PREDICTOR")
   st.write("Enter the values:")
   cement = st.number_input("cement")
   Blast = st.number_input("Blast")
   Fly = st.number_input("Fly")
   Water = st.number_input("Water")
   Superplasticizer = st.number_input("Superplasticizer")
   Coarse = st.number_input("coarse")
   Fine = st.number_input("Fine")
   Age = st.number_input("age")
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
      df = pd.DataFrame({"Cement" : [cement],'Blast' : [Blast],'Fly':[Fly],'Water':[Water],'Superplasticizer' :[Superplasticizer],'Coarse':[Coarse],'Fine':[Fine],'Age':[Age]})
    #    st.write("slider", slider_val, "checkbox", checkbox_val)

      scaler = joblib.load('artifacts\model_trainer\scaler')
      scaler.transform(df)
      model = joblib.load('artifacts\model_trainer\model.joblib')
      y_pred = model.predict(df)
      st.write("# CEMENT STRENGTH : ",y_pred)
      st.write("Outside the form")
