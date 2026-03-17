import joblib
import numpy as np

model = joblib.load("models/best_model.pkl")

def predict_loan(data):

    data = np.array(data).reshape(1, -1)

    prob = model.predict_proba(data)[0][1]
    risk_score = round(prob * 100, 2)

    if prob >= 0.7:
        return "Loan Approved", "Low Risk ✅", risk_score
    elif prob >= 0.4:
        return "Review Needed", "Medium Risk ⚠️", risk_score
    else:
        return "Loan Rejected", "High Risk ❌", risk_score