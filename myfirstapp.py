import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Simple Iris Flower Prediction App

This app predicts the **Iris flower** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    TV = st.sidebar.slider('TV', 1.0, 150.0, 300.0)
    Radio = st.sidebar.slider('Radio', 1.0, 25.0, 50.0)
    Newspaper = st.sidebar.slider('Newspaper', 1.0, 35.0, 70.0)
    Sales = st.sidebar.slider('Sales', 1.0, 15.0, 30.0)
    data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper,
            'Sales': Sales}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('Advertising Input parameters')
st.write(df)

advertising = datasets.load_iris()
X = advertising.data
Y = advertising.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])
#st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
