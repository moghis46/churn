import streamlit as st
import pickle
import numpy as np

model  = pickle.load(open('churn_model.pkl', 'rb'))
scaler = pickle.load(open('churn_scaler.pkl', 'rb'))

st.title('📊 Customer Churn Prediction')

senior_citizen  = st.selectbox('Senior Citizen', [0, 1])
tenure          = st.number_input('Tenure (months)', min_value=0, max_value=72, value=12)
monthly_charges = st.number_input('Monthly Charges', min_value=0.0, max_value=150.0, value=65.0)
total_charges   = st.number_input('Total Charges', min_value=0.0, max_value=10000.0, value=780.0)
gender          = st.selectbox('Gender', ['Male', 'Female'])
partner         = st.selectbox('Partner', ['Yes', 'No'])
dependents      = st.selectbox('Dependents', ['Yes', 'No'])
phone_service   = st.selectbox('Phone Service', ['Yes', 'No'])
multiple_lines  = st.selectbox('Multiple Lines', ['Yes', 'No', 'No phone service'])
internet        = st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'])
online_security = st.selectbox('Online Security', ['Yes', 'No', 'No internet service'])
online_backup   = st.selectbox('Online Backup', ['Yes', 'No', 'No internet service'])
device_protection = st.selectbox('Device Protection', ['Yes', 'No', 'No internet service'])
tech_support    = st.selectbox('Tech Support', ['Yes', 'No', 'No internet service'])
streaming_tv    = st.selectbox('Streaming TV', ['Yes', 'No', 'No internet service'])
streaming_movies = st.selectbox('Streaming Movies', ['Yes', 'No', 'No internet service'])
contract        = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
paperless       = st.selectbox('Paperless Billing', ['Yes', 'No'])
payment         = st.selectbox('Payment Method', ['Bank transfer (automatic)', 'Credit card (automatic)', 'Electronic check', 'Mailed check'])

features = np.array([[
    senior_citizen,
    tenure,
    monthly_charges,
    total_charges,
    1 if gender == 'Male' else 0,
    1 if partner == 'Yes' else 0,
    1 if dependents == 'Yes' else 0,
    1 if phone_service == 'Yes' else 0,
    1 if multiple_lines == 'No phone service' else 0,
    1 if multiple_lines == 'Yes' else 0,
    1 if internet == 'Fiber optic' else 0,
    1 if internet == 'No' else 0,
    1 if online_security == 'No internet service' else 0,
    1 if online_security == 'Yes' else 0,
    1 if online_backup == 'No internet service' else 0,
    1 if online_backup == 'Yes' else 0,
    1 if device_protection == 'No internet service' else 0,
    1 if device_protection == 'Yes' else 0,
    1 if tech_support == 'No internet service' else 0,
    1 if tech_support == 'Yes' else 0,
    1 if streaming_tv == 'No internet service' else 0,
    1 if streaming_tv == 'Yes' else 0,
    1 if streaming_movies == 'No internet service' else 0,
    1 if streaming_movies == 'Yes' else 0,
    1 if contract == 'One year' else 0,
    1 if contract == 'Two year' else 0,
    1 if paperless == 'Yes' else 0,
    1 if payment == 'Credit card (automatic)' else 0,
    1 if payment == 'Electronic check' else 0,
    1 if payment == 'Mailed check' else 0,
]])

if st.button('Predict Churn'):
    scaled = scaler.transform(features)
    pred   = model.predict(scaled)
    if pred[0] == 1:
        st.error('❌ Customer Churn Karega!')
    else:
        st.success('✅ Customer Nahi Jayega!')