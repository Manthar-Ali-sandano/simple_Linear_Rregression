import streamlit as st
import pickle
import os

st.title("Salary Predictor")

# Function to resolve the model path
def get_model_path():
    # Check if running on Streamlit Cloud
    if "STREAMLIT_CLOUD" in os.environ:
        # Path for Streamlit Cloud
        return "01-salary-predictor/model.pkl"
    else:
        # Path for local environment
        return os.path.join(os.path.dirname(__file__), "model.pkl")


with open(get_model_path(), 'rb') as file:
    model = pickle.load(file)

user_input =st.number_input("Experience Years",min_value=0.0,max_value=50.0,value=0.0,step=0.1)
st.success(model.predict([[user_input]]))