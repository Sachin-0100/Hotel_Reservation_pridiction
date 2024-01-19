import streamlit as st
import pandas as pd
import joblib  # For loading the pre-trained model

# Load the pre-trained model
model_path = "model/trained_model.sav"  # Replace with the actual path relative to your script
model1 = joblib.load(model_path)

# Streamlit app
st.title("Booking Status Prediction App")

# Sidebar with user input
st.sidebar.header("User Input Features")

# Collect user inputs for each feature
# For simplicity, assuming all features are numerical and user input is received through sliders
user_inputs = {}
feature_columns = ["no_of_adults", "no_of_children", "no_of_weekend_nights", "no_of_week_nights", 
                   "type_of_meal_plan", "required_car_parking_space", "room_type_reserved", 
                   "lead_time", "arrival_year", "arrival_month", "arrival_date", 
                   "market_segment_type", "repeated_guest", "no_of_previous_cancellations", 
                   "no_of_previous_bookings_not_canceled", "avg_price_per_room", "no_of_special_requests"]

for feature in feature_columns:
    user_inputs[feature] = st.sidebar.slider(f"Select {feature}", float(0), float(100), float(50))

# Make predictions based on user input
user_data = pd.DataFrame([user_inputs])
prediction = model1.pridict(user_data)

# Display prediction
st.subheader("Prediction")
st.write("Predicted Booking Status:", prediction[0])
