import requests
import streamlit as st


API_URL = "http://localhost:8000/predict"


st.set_page_config(
    page_title="House Price Predictor",
    layout="centered"
)


st.title("House Price Predictor")
st.write("Enter house details and get a predicted price.")


area = st.number_input("Area", min_value=0.0, value=7420.0)
bedrooms = st.number_input("Bedrooms", min_value=0, value=4)
bathrooms = st.number_input("Bathrooms", min_value=0, value=2)
stories = st.number_input("Stories", min_value=0, value=3)
parking = st.number_input("Parking spaces", min_value=0, value=2)


payload = {
    "area": area,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "stories": stories,
    "parking": parking,
}


if st.button("Predict"):
    try:
        response = requests.post(API_URL, json=payload, timeout=10)

        if response.status_code == 200:
            result = response.json()
            st.success(
                f"Predicted house price: ${result['predicted_house_price']:,.2f}"
            )
        else:
            st.error("API returned an error.")
            st.write(response.text)

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to API. Make sure FastAPI is running.")

    except requests.exceptions.Timeout:
        st.error("API request timed out.")