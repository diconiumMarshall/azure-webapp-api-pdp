"""
    Dataset
    https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who?resource=download

    Other Datasets
    https://www.kaggle.com/discussions/general/268890

    This connects all modules through FastAPI
    Run with: uvicorn streamlit_app:app --reload
"""

import streamlit as st
import requests


API_URL = "http://fastapi:8000/predict"  # Use 'fastapi' as it's the service name in Docker Compose


def get_rating(review: str) -> int:
    """Calls API which passes the user input to the ML model on the backend."""
    response = requests.post(API_URL, json={"data": review})
    if response.status_code == 200:
        return response.json()["result"]
    else:
        st.error(f"Error: {response.text}")


st.title("Yelp Rating Predictor")

user_input = st.text_area(
    label="Leave a review",
    key='review'
)

# Button to trigger API call
if st.button("Get Prediction"):
    result = get_rating(user_input)
    if result:
        st.success(f"Predicted Rating: {result}")
