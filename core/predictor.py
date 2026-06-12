import joblib
import pandas as pd

class FraudPredictor:

    def __init__(self):
        self.model = joblib.load("model/fraud_model.pkl")

    def predict(self, data):

        predictions = self.model.predict(data)

        probabilities = self.model.predict_proba(data)[:, 1]

        return predictions, probabilities