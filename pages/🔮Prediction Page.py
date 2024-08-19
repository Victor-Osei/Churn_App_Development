import streamlit as st
import numpy as np
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import sklearn 
import lightgbm as lgb 
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Predictive Analytics Dashboard",
    page_icon="🔮",
    layout="wide",
)

# Custom header with a subheader
page_title = "🔮 Predictive Analytics Dashboard"
st.title(page_title)
st.subheader("Empowering your decisions with data-driven insights")

# Loading the model and preprocessing tools
components = joblib.load('models/churn_model_components.pkl')

# Extract the preprocessor and models
preprocessor = components['preprocessing']['preprocessor']
models = components['tuned_models']

# Define the expected columns and their default values
expected_columns = {
    'Gender': 'Male', 'Senior_Citizen': 'No', 'Partner': 'No', 'Dependents': 'No', 
    'tenure': 0, 'Phone_Service': 'No', 'Multiple_Lines': 'No phone service', 
    'Internet_Service': 'DSL', 'Online_Security': 'No internet service', 
    'Online_Backup': 'No internet service', 'Device_Protection': 'No internet service', 
    'Tech_Support': 'No internet service', 'Streaming_TV': 'No internet service', 
    'Streaming_Movies': 'No internet service', 'Contract': 'Month-to-month', 
    'Paperless_Billing': 'No', 'Payment_Method': 'Electronic check', 
    'Monthly_Charges': 0.0, 'Total_Charges': 0.0
}

# Function to make predictions
def predict(attributes, model_name='random_forest'):
    # Combine user attributes with the default values
    user_data = {**expected_columns, **attributes}
    df = pd.DataFrame([user_data], columns=expected_columns.keys())
    processed_df = preprocessor.transform(df)
    pred = models[model_name].predict(processed_df)
    prob = models[model_name].predict_proba(processed_df)
    return pred[0], np.max(prob)

# Initialize session state to store history if it doesn't exist
if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=['Date', 'Time', 'Prediction', 'Probability'])

# Check if the page is for predictions
st.markdown("### Enter Customer Details to Predict Churn")
with st.form(key='user_input_form'):
    gender = st.selectbox('Gender', ['Male', 'Female'])
    senior_citizen = st.selectbox('Senior Citizen', ['Yes', 'No'])
    partner = st.selectbox('Partner', ['Yes', 'No'])
    dependents = st.selectbox('Dependents', ['Yes', 'No'])
    tenure = st.slider('Tenure (in months)', 0, 100, 1)
    phone_service = st.selectbox('Phone Service', ['Yes', 'No'])
    multiple_lines = st.selectbox('Multiple Lines', ['Yes', 'No', 'No phone service'])
    internet_service = st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'])
    online_security = st.selectbox('Online Security', ['Yes', 'No', 'No internet service'])
    online_backup = st.selectbox('Online Backup', ['Yes', 'No', 'No internet service'])
    device_protection = st.selectbox('Device Protection', ['Yes', 'No', 'No internet service'])
    tech_support = st.selectbox('Tech Support', ['Yes', 'No', 'No internet service'])
    streaming_tv = st.selectbox('Streaming TV', ['Yes', 'No', 'No internet service'])
    streaming_movies = st.selectbox('Streaming Movies', ['Yes', 'No', 'No internet service'])
    contract = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
    paperless_billing = st.selectbox('Paperless Billing', ['Yes', 'No'])
    payment_method = st.selectbox('Payment Method', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
    monthly_charges = st.number_input('Monthly Charges', 0.0, 200.0, 70.0)
    total_charges = st.number_input('Total Charges', 0.0, 10000.0, 150.0)

    # Model selection
    model_choice = st.selectbox('Choose Model', list(models.keys()))

    # Submit button
    submit_button = st.form_submit_button(label='Predict Churn')

# Prediction and output
if submit_button:
    user_input = {
        'Gender': gender, 'Senior_Citizen': 'Yes' if senior_citizen == 'Yes' else 'No', 'Partner': partner, 
        'Dependents': dependents, 'tenure': tenure, 'Phone_Service': phone_service, 
        'Multiple_Lines': multiple_lines, 'Internet_Service': internet_service, 
        'Online_Security': online_security, 'Online_Backup': online_backup, 
        'Device_Protection': device_protection, 'Tech_Support': tech_support, 
        'Streaming_TV': streaming_tv, 'Streaming_Movies': streaming_movies, 
        'Contract': contract, 'Paperless_Billing': paperless_billing, 
        'Payment_Method': payment_method, 'Monthly_Charges': monthly_charges, 
        'Total_Charges': total_charges
    }

    prediction, probability = predict(user_input, model_choice)
    prediction_text = 'Churn' if prediction == 1 else 'No Churn'
    
    st.markdown(f"### Prediction: {'Churn' if prediction == 1 else 'No Churn'}")
    st.markdown(f"**Probability:** {probability:.2f}")

    # Display a probability bar chart
    fig, ax = plt.subplots()
    ax.barh(['No Churn', 'Churn'], [1 - probability, probability], color=['green', 'red'])
    ax.set_xlim(0, 1)
    st.pyplot(fig)

    # Explanation or interpretation section
    interpretation = f"The model predicts that the customer is {'likely' if prediction == 1 else 'not likely'} to churn with a confidence level of {probability:.2%}."
    st.markdown("#### Interpretation")
    st.write(interpretation)

    # Store the predicted data in history with date and time
    current_time = datetime.now()
    new_record = pd.DataFrame({
        'Date': [current_time.strftime('%Y-%m-%d')],
        'Time': [current_time.strftime('%H:%M:%S')],
        'Prediction': [prediction_text],
        'Model': [model_choice],
        'Probability': [probability],
        'Interpretation': [interpretation],
    })
    st.session_state.history = pd.concat([st.session_state.history, new_record], ignore_index=True)