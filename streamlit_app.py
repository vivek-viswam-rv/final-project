import streamlit as st
import requests

# Set up the Streamlit interface
st.title("Wine Classification Model")
st.write("Enter the feature values of a wine sample to get its class prediction.")

# Input fields for the features
Alcohol = st.number_input("Alcohol", value=13.0)
MalicAcid = st.number_input("Malic Acid", value=1.5)
Ash = st.number_input("Ash", value=2.0)
AlcalinityOfAsh = st.number_input("Alcalinity of Ash", value=15.0)
Magnesium = st.number_input("Magnesium", value=100.0)
TotalPhenols = st.number_input("Total Phenols", value=2.5)
Flavanoids = st.number_input("Flavanoids", value=2.0)
NonflavanoidPhenols = st.number_input("Nonflavanoid Phenols", value=0.3)
Proanthocyanins = st.number_input("Proanthocyanins", value=1.0)
ColorIntensity = st.number_input("Color Intensity", value=5.0)
Hue = st.number_input("Hue", value=1.0)
OD280_OD315 = st.number_input("OD280/OD315 of Diluted Wines", value=3.0)
Proline = st.number_input("Proline", value=1000.0)

# Button to make a prediction
if st.button("Predict"):
    # Prepare the input data as a dictionary
    input_data = {
        "Alcohol": Alcohol,
        "MalicAcid": MalicAcid,
        "Ash": Ash,
        "AlcalinityOfAsh": AlcalinityOfAsh,
        "Magnesium": Magnesium,
        "TotalPhenols": TotalPhenols,
        "Flavanoids": Flavanoids,
        "NonflavanoidPhenols": NonflavanoidPhenols,
        "Proanthocyanins": Proanthocyanins,
        "ColorIntensity": ColorIntensity,
        "Hue": Hue,
        "OD280_OD315": OD280_OD315,
        "Proline": Proline
    }

    # Send the input data to the FastAPI endpoint
    api_url = "https://vivek-viswam-final-project-36b367658b24.herokuapp.com/predict"
    try:
        response = requests.post(api_url, json=input_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Class: {result['prediction']}")
        else:
            st.error(f"Error: {response.status_code}, {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
