import streamlit as st
import pickle

st.title("Manthar's salary")


with open("model.pkl", 'rb') as file:
    model = pickle.load(file)

user_input =st.number_input("Experience Years",min_value=0.0,max_value=50.0,value=0.0,step=0.1)
if st.button("predict Salary"):
    st.success(model.predict([[user_input]])[0])