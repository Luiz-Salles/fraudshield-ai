import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="FraudShield AI",
    layout="wide"
)

st.title("FraudShield AI")

st.subheader(
    "Sistema Inteligente de Detecção de Fraudes Financeiras"
)

df = pd.read_csv(
    "data/resultado.csv"
)

suspeitas = df[
    df["anomalia"] == -1
]

col1, col2, col3 = st.columns(3)

col1.metric(
    "Transações",
    len(df)
)

col2.metric(
    "Fraudes Detectadas",
    len(suspeitas)
)

col3.metric(
    "Taxa",
    f"{(len(suspeitas)/len(df))*100:.2f}%"
)

st.divider()

st.subheader(
    "Transações Suspeitas"
)

st.dataframe(
    suspeitas
)

st.divider()

st.subheader(
    "Top 10 maiores transações suspeitas"
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