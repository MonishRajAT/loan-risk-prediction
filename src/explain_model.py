import shap
import joblib
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

model = joblib.load("models/best_model.pkl")

def explain_prediction(data):

    feature_names = [
        "Gender","Married","Dependents","Education",
        "Self_Employed","ApplicantIncome","CoapplicantIncome",
        "LoanAmount","Loan_Amount_Term",
        "Credit_History","Property_Area"
    ]

    df = pd.DataFrame([data], columns=feature_names)

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(df)

    # ✅ HANDLE ALL CASES SAFELY
    if isinstance(shap_values, list):
        shap_val = shap_values[1][0]
    else:
        shap_val = shap_values[0]
        if len(shap_val.shape) == 2:
            shap_val = shap_val[:, 1]

    # ✅ BAR CHART (CLEAN UI)
    st.subheader("📊 Feature Impact")

    fig, ax = plt.subplots()

    ax.barh(feature_names, shap_val)
    ax.set_xlabel("Impact on Prediction")
    ax.set_title("Feature Contribution")

    st.pyplot(fig)

    # ✅ TEXT EXPLANATION (VERY IMPORTANT)
    st.subheader("🧠 Key Factors")

    # Get top 3 important features
    indices = np.argsort(np.abs(shap_val))[::-1][:3]

    for i in indices:
        impact = "increased" if shap_val[i] > 0 else "decreased"
        st.write(f"• {feature_names[i]} → {impact} approval probability")