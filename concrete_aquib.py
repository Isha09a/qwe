
import streamlit as st
import pandas as pd
import pickle

# Load the pickled model
with open('lrt.pkl', 'rb') as file:
    model = pickle.load(file)

st.write("""
# Simple linear regression Prediction App

This app predicts the 'y'
""")

st.sidebar.header('User Input Parameters')

X_test = st.sidebar.slider("Select X to get yhat",0,10,5)

st.write("X test is :", X_test)


st.subheader('User Input parameters')
st.write(df)
y_hat_test = model.predict(df)

st.write("b0 is", round(model.intercept_, 3))
st.write("b1 is", round(model.coef_[0], 3))
st.write("yhat test is", y_hat_test)

