import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="FraudShield AI",
    layout="wide"
)

st.title("FraudShield AI")

st.subheader(
    "Intelligent Financial Fraud Detection System"
)

df = pd.read_csv(
    "data/resultado.csv"
)

suspeitas = df[
    df["anomalia"] == -1
]

col1, col2, col3 = st.columns(3)

col1.metric(
    "Transactions",
    len(df)
)

col2.metric(
    "Fraud Detected",
    len(suspeitas)
)

col3.metric(
    "Rate",
    f"{(len(suspeitas)/len(df))*100:.2f}%"
)

st.divider()

st.subheader(
    "Suspicious Transactions"
)

st.dataframe(
    suspeitas
)

st.divider()

st.subheader(
    "Top 10 Highest-Value Suspicious Transactions"
)

st.bar_chart(
    suspeitas
    .sort_values(
        by="valor",
        ascending=False
    )
    .head(10)
    .set_index(
        suspeitas
        .sort_values(
            by="valor",
            ascending=False
        )
        .head(10)
        .index
    )["valor"]
)

st.subheader(
    "Highest Risk Transactions"
)

top_risk = (
    suspeitas
    .sort_values(
        by="risk_score",
        ascending=False
    )
    .head(20)
)

st.dataframe(
    top_risk[
        [
            "valor",
            "cidade",
            "risk_score"
        ]
    ]
)