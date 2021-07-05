import pandas as pd
import numpy as np
import pickle
import streamlit as st
st.write("""
# forest fire prediction app
This app predicts the *proba of having a forest fire today * !
""")

st.sidebar.header('User Input Features')



# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
bill_length_mm = st.sidebar.slider('Temperature', -40,60,28)
bill_depth_mm = st.sidebar.slider('RH', 0,200,20)
flipper_length_mm = st.sidebar.slider('	Ws', 0,200,17)
body_mass_g = st.sidebar.slider('Rain', 0,2000,0)
data = {
        'temperature': bill_length_mm,
        'RH': bill_depth_mm,
        'WS': flipper_length_mm,
        'rain': body_mass_g}
df = pd.DataFrame(data, index=[0])
        
# Displays the user input features
st.subheader('User Input features')

st.write(df)

# Reads in saved classification model
load_clf = pickle.load(open('penguins_clf1.pkl', 'rb'))

# Apply model to make predictions
prediction = load_clf.predict(df)
if prediction:
    prediction = "we think that there will be a fire today"
else:
    prediction = "we think that there wont be a fire today"

st.subheader('Prediction')
st.write(prediction)

