import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression

st.write("""
# Advertising Project App
""")

st.sidebar.header('Advertising method')     

def user_input_features():
    TV = st.sidebar.slider('TV', 1.0, 300.0, 150.0)
    Radio = st.sidebar.slider('Radio', 1.0, 50.0, 25.0)
    Newspaper = st.sidebar.slider('Newspaper', 1.0, 70.0, 35.0)
    data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('Advertising Input parameters')
st.write(df)

dfdata = pd.read_csv("Advertising.csv")
dftdata = dfdata.drop(['Unnamed:0'], axis=1)
X = dfdata.drop(['Sales'],axis=1)
Y = dfdata.Sales

clf = LinearRegression()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(advertisingproject.target_names)

st.subheader('Prediction')
st.write(advertisingproject.target_names[prediction])
#st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
