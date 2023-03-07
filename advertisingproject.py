import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Advertising Project App

This app predicts the **Advertisement** type!
""")

st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
show = st.checkbox('I agree the terms and conditions')
if show:
    st.write(pd.DataFrame({
    'Intplan': ['yes', 'yes', 'yes', 'no'],
    'Churn Status': [0, 0, 0, 1]

st.sidebar.header('Advertising method')     
    option = st.sidebar.selectbox(
    'Select a mini project',
    ['TV','Radio','Newspaper','Sales'])

def user_input_features():
    TV = st.sidebar.slider('TV', 1.0, 300.0, 150.0)
    Radio = st.sidebar.slider('Radio', 1.0, 50.0, 25.0)
    Newspaper = st.sidebar.slider('Newspaper', 1.0, 70.0, 35.0)
    Sales = st.sidebar.slider('Sales', 1.0, 30.0, 15.0)
    data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper,
            'Sales': Sales}
    features = pd.DataFrame(data, index=[0])
    return features

df = pd.read_csv('Advertising.csv')

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
