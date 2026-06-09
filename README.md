# FraudShield AI

An Intelligent Financial Fraud Detection System powered by Machine Learning.

## Overview

FraudShield AI is a fraud detection solution designed to identify suspicious financial transactions through anomaly detection techniques.

The system analyzes transaction patterns and automatically flags potentially fraudulent activities, helping financial institutions improve risk monitoring and fraud prevention processes.

## Features

* Detection of anomalous financial transactions
* Machine Learning-based risk analysis
* Interactive dashboard built with Streamlit
* Transaction monitoring and visualization
* Risk scoring system
* Reproducible environment using Python

## Technologies

* Python
* Pandas
* NumPy
* Scikit-Learn
* Isolation Forest
* Streamlit
* Plotly

## Project Structure

```text
fraudshield-ai/

├── data/
├── models/
├── generate_data.py
├── detector.py
├── app.py
├── requirements.txt
└── README.md
```

## How It Works

1. Generate transaction data.
2. Preprocess transaction features.
3. Train an Isolation Forest model.
4. Detect anomalous transactions.
5. Calculate risk scores.
6. Display results in an interactive dashboard.

## Installation

```bash
pip install -r requirements.txt
```

## Run

Generate dataset:

```bash
python generate_data.py
```

Train model:

```bash
python detector.py
```

Start dashboard:

```bash
streamlit run app.py
```

## Example Use Cases

* Banking fraud monitoring
* Financial transaction analysis
* Risk assessment
* Fraud investigation support

## Future Improvements

* Real-time transaction monitoring
* API integration
* User authentication
* Explainable AI module
* Advanced fraud scoring

## Author

Luiz Felipe Salles Alves

GitHub:
https://github.com/Luiz-Salles