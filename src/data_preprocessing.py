import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess():

    # Load the dataset
    df = pd.read_csv("data/train.csv")
    print("Original dataset shape: ", df.shape)

    # Drop Loan_ID
    df = df.drop(columns=["Loan_ID"])

    # Fill missing categorical values with mode
    df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
    df['Married'].fillna(df['Married'].mode()[0], inplace=True)
    df['Dependents'].fillna(df['Dependents'].mode()[0], inplace=True)
    df['Self_Employed'].fillna(df['Self_Employed'].mode()[0], inplace=True)

    # Fill missing numerical values with median
    df['LoanAmount'].fillna(df['LoanAmount'].median(), inplace=True)
    df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].median(), inplace=True)
    df['Credit_History'].fillna(df['Credit_History'].median(), inplace=True)

    # Enocde categorical columns
    label_cols = [
        'Gender',
        'Married',
        'Dependents',
        'Education',
        'Self_Employed',
        'Property_Area',
        'Loan_Status'
    ]
    le = LabelEncoder()
    for col in label_cols:
        df[col] = le.fit_transform(df[col])

    # Split the features and target variable
    X = df.drop("Loan_Status", axis=1)
    y = df["Loan_Status"]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    
    print("Training data shape: ", X_train.shape)
    print("Testing data shape: ", X_test.shape)

    return X_train, X_test, y_train, y_test