from predict import predict_loan

data = [
    1,  # Gender
    1,  # Married
    0,  # Dependents
    1,  # Education
    0,  # Self employed
    5000,  # Applicant income
    0,  # Coapplicant income
    150,  # Loan amount
    360,  # Loan term
    1,  # Credit history
    1   # Property area
]

decision, risk_level, score = predict_loan(data)

print("Decision:", decision)
print("Risk Level:", risk_level)
print("Risk Score:", score, "%")