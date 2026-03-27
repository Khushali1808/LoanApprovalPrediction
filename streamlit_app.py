import streamlit as st
import requests

st.title("🏦 Loan Approval Predictor")

income = st.slider("Monthly Income ($)", 1000, 10000, 4000)
credit_score = st.slider("Credit Score (0-100)", 0, 100, 60)
loan_amount = st.slider("Loan Amount ($)", 1000, 50000, 15000)
loan_term = st.slider("Loan Term (months)", 6, 60, 24)

if st.button("Predict"):
    url = "http://127.0.0.1:5000/predict"  # use your deployed URL if hosted
    
    data = {
        "income": income,
        "credit_score": credit_score,
        "loan_amount": loan_amount,
        "loan_term": loan_term
    }
    
    response = requests.post(url, json=data)
    result = response.json()
    
    if result['prediction'] == 1:
        st.success("✅ Loan is likely to be approved!")
    else:
        st.error("❌ Loan is likely to be rejected.")