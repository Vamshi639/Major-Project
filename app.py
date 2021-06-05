import streamlit as st
import joblib
model = joblib.load('Sentiment_Analyzer')
st.title('Sentiment Analyzer')
input = st.text_input('Enter your review:')
output = model.predict([input])
ans = output[0]
if st.button('Predict'):
  st.title(output[0]) 
