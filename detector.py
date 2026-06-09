import pandas as pd

from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder

import joblib

df = pd.read_csv("data/transactions.csv")

encoder = LabelEncoder()

df["cidade"] = encoder.fit_transform(df["cidade"])

X = df[["valor", "hora", "cidade"]]

modelo = IsolationForest(
    contamination=0.025,
    random_state=42
)

modelo.fit(X)

df["anomalia"] = modelo.predict(X)

df["score"] = modelo.decision_function(X)

joblib.dump(
    modelo,
    "models/fraud_model.pkl"
)

df["risk_score"] = (
    (1 - (
        (df["score"] - df["score"].min())
        /
        (df["score"].max() - df["score"].min())
    )) * 100
).round(2)

df.to_csv(
    "data/resultado.csv",
    index=False
)

print("Successfully Trained Model.")