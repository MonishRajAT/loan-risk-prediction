import streamlit as st
from src.predict import predict_loan
from src.explain_model import explain_prediction

st.title("📊 Loan Risk Prediction")

st.markdown("Fill applicant details below")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male","Female"])
    married = st.selectbox("Marital Status", ["No","Yes"])
    dependents = st.selectbox("Dependents", ["0","1","2","3+"])
    education = st.selectbox("Education", ["Graduate","Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["No","Yes"])

with col2:
    income = st.number_input("Income", min_value=0)
    co_income = st.number_input("Co Income", min_value=0)
    loan_amount = st.number_input("Loan Amount", min_value=0)
    loan_term = st.number_input("Loan Term", min_value=0)
    credit_history = st.selectbox("Credit History", ["Bad","Good"])
    property_area = st.selectbox("Property Area", ["Rural","Semiurban","Urban"])

# Encoding
gender = 1 if gender=="Male" else 0
married = 1 if married=="Yes" else 0
dependents = 3 if dependents=="3+" else int(dependents)
education = 1 if education=="Graduate" else 0
self_employed = 1 if self_employed=="Yes" else 0
credit_history = 1 if credit_history=="Good" else 0
property_area = {"Rural":0,"Semiurban":1,"Urban":2}[property_area]

if st.button("🚀 Predict"):

    if income <= 0 or loan_amount <= 0:
        st.error("Enter valid values")
    else:
        data = [
            gender, married, dependents, education,
            self_employed, income, co_income,
            loan_amount, loan_term, credit_history, property_area
        ]

        decision, risk_level, score = predict_loan(data)

        st.subheader("📊 Result")

        col1, col2, col3 = st.columns(3)

        col1.metric("Risk Score", f"{score}%")
        col2.success(decision)
        col3.warning(risk_level)

        st.divider()

        st.subheader("🔍 AI Explanation")

        explain_prediction(data)