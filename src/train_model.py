import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
import matplotlib.pyplot as plt

from data_preprocessing import load_and_preprocess


def train_models():

    # Load preprocessed data
    X_train, X_test, y_train, y_test = load_and_preprocess()

    # Random Forest Model
    rf_model = RandomForestClassifier(
        n_estimators=200,
        max_depth=8,
        random_state=42
    )

    rf_model.fit(X_train, y_train)

    rf_preds = rf_model.predict(X_test)

    rf_acc = accuracy_score(y_test, rf_preds)

    print("\nRandom Forest Accuracy:", rf_acc)

    # XGBoost Model
    xgb_model = XGBClassifier(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=5,
        random_state=42,
        use_label_encoder=False,
        eval_metric='logloss'
    )

    xgb_model.fit(X_train, y_train)

    xgb_preds = xgb_model.predict(X_test)

    xgb_acc = accuracy_score(y_test, xgb_preds)

    print("XGBoost Accuracy:", xgb_acc)

    # Select best model
    if xgb_acc > rf_acc:

        best_model = xgb_model
        print("\nBest Model: XGBoost")

    else:

        best_model = rf_model
        print("\nBest Model: Random Forest")

    # Save best model
    joblib.dump(best_model, "models/best_model.pkl")

    # Feature Importance

    if hasattr(best_model, "feature_importances_"):

        importances = best_model.feature_importances_

        feature_names = X_train.columns

        plt.figure(figsize=(10,6))

        plt.barh(feature_names, importances)

        plt.xlabel("Importance Score")

        plt.title("Feature Importance for Loan Prediction")

        plt.show()

        print("\nBest model saved in models/best_model.pkl")


if __name__ == "__main__":
    train_models()