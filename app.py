

import streamlit as st
import pandas as pd
import numpy as np
import joblib 

st.title("Credit Card Fraud Detection App")

model = joblib.load("https://github.com/mrsaurabhtanwer/Credit-Card-Fraud-Detection-System/blob/main/fraud_model.pkl")
scaler = joblib.load("https://github.com/mrsaurabhtanwer/Credit-Card-Fraud-Detection-System/blob/main/fraud_scaler.pkl")

amount = st.number_input("Transaction Amount", min_value=0.0)
old_balance = st.number_input("Old Balance", min_value=0.0)
new_balance = st.number_input("New Balance", min_value=0.0)
transaction_type = st.selectbox("Transaction Type", options=["Debit", "Credit"])
type_val = 0 if transaction_type == "Debit" else 1

input_data = pd.DataFrame([[amount, old_balance, new_balance, type_val]],
                           columns=['amount', 'old_balance', 'new_balance', 'transaction_type'])
input_scaled = scaler.transform(input_data)

if st.button("Predict Fraud"):
     prediction = model.predict(input_scaled)[0]
     st.write("🟢 Legitimate Transaction" if prediction == 0 else "🔴 Fraudulent Transaction")

