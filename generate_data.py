import pandas as pd
import random

cidades = [
    "Campinas",
    "Valinhos",
    "Vinhedo",
    "São Paulo",
    "Jundiaí"
]

tipos = [
    "PIX",
    "TED",
    "BOLETO",
    "CARTAO"
]

dados = []

for _ in range(3000):

    dados.append({
        "valor": random.randint(10, 3000),
        "hora": random.randint(6, 23),
        "cidade": random.choice(cidades),
        "tipo_transacao": random.choice(tipos),
        "idade_conta": random.randint(180, 5000)
    })

for _ in range(80):

    dados.append({
        "valor": random.randint(15000, 80000),
        "hora": random.randint(0, 4),
        "cidade": random.choice([
            "Moscou",
            "Pequim",
            "Teerã"
        ]),
        "tipo_transacao": random.choice([
            "PIX",
            "TED"
        ]),
        "idade_conta": random.randint(1, 30)
    })

df = pd.DataFrame(dados)

df.to_csv(
    "data/transactions.csv",
    index=False
)

print("Dataset generated successfully.")