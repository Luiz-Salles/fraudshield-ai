import pandas as pd
import random

cidades_normais = [
    "Campinas",
    "Valinhos",
    "Vinhedo",
    "Jundiai",
    "São Paulo"
]

dados = []

# transações normais
for _ in range(2000):

    dados.append({
        "valor": random.randint(10, 2500),
        "hora": random.randint(6, 23),
        "cidade": random.choice(cidades_normais)
    })

# fraudes simuladas
for _ in range(50):

    dados.append({
        "valor": random.randint(10000, 50000),
        "hora": random.randint(0, 4),
        "cidade": random.choice([
            "Moscou",
            "Pequim",
            "Teerã"
        ])
    })

df = pd.DataFrame(dados)

df.to_csv(
    "data/transactions.csv",
    index=False
)

print("Base criada com sucesso.")