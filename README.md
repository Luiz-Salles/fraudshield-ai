# FraudShield AI – Financial Fraud Detection & Risk Analytics

An intelligent fraud detection and risk analytics platform powered by Machine Learning, designed to identify suspicious financial transactions and support fraud monitoring processes in financial institutions.

---

## Overview

FraudShield AI is a machine learning-based solution that detects potentially fraudulent financial transactions through anomaly detection techniques.

The system combines transaction profiling, risk scoring, behavioral analysis, and interactive dashboards to support fraud monitoring and risk assessment activities commonly found in banking and financial environments.

Using the Isolation Forest algorithm, the platform automatically identifies unusual transaction patterns and assigns risk scores to assist decision-making and investigation workflows.

---

## Dashboard Preview

### Executive Dashboard

<img width="1810" height="876" alt="image" src="https://github.com/user-attachments/assets/bbc0a674-ca03-4e16-b96b-3c11f555db83" />

### Fraud Detection Map

<img width="1455" height="692" alt="image" src="https://github.com/user-attachments/assets/4cd8450b-43d5-4e47-b120-6ed433e3c7a6" />

### Highest Risk Transactions

<img width="1472" height="531" alt="image" src="https://github.com/user-attachments/assets/923cb2fd-71df-4d60-ad05-306b7830e9cb" />

---

## Key Features

* Machine Learning-based fraud detection
* Anomaly detection using Isolation Forest
* Transaction risk scoring engine
* Interactive risk analytics dashboard
* Fraud monitoring and investigation support
* Dynamic filtering by city, transaction type and channel
* Real-time dashboard interactions through Streamlit
* Data visualization using Plotly

---

## Technologies

* Python
* Pandas
* NumPy
* Scikit-Learn
* Isolation Forest
* Streamlit
* Plotly
* Git
* GitHub

---

## Machine Learning Model

Algorithm:
Isolation Forest

Features Used:
- Transaction Amount
- Transaction Hour
- Transaction City
- Transaction Channel
- Account Age

Output:
- Anomaly Classification
- Risk Score

---

## How It Works

### 1. Synthetic Transaction Generation

The system generates realistic transaction records containing:

* Transaction amount
* Transaction hour
* City
* Transaction type
* Transaction channel
* Account age

Normal and suspicious transaction patterns are simulated to create a realistic fraud detection environment.

### 2. Data Processing

Categorical features are encoded and prepared for machine learning analysis.

### 3. Fraud Detection Model

An Isolation Forest model is trained to identify anomalous transactions based on behavioral patterns.

### 4. Risk Scoring

Each transaction receives a risk score ranging from 0 to 100, allowing prioritization of suspicious activities.

### 5. Interactive Analytics Dashboard

Users can explore:

* Fraud distribution by channel
* Fraud concentration by city
* Fraud detection maps
* Risk score distributions
* High-risk transaction rankings

---

## Dashboard Components

### Executive KPIs

* Total Transactions
* Frauds Detected
* Detected Risk Rate
* Highest Suspicious Amount
* Highest Risk Score

### Visual Analytics

* Donut Chart: Fraud Distribution by Channel
* Treemap: Fraud Concentration by City
* Scatter Plot: Fraud Detection Map
* Heatmap: Fraud Activity Analysis
* Histogram: Risk Score Distribution

### Investigation Table

* Top 20 Highest Risk Transactions

---

## Project Structure

```text
fraudshield-ai/

├── assets/
│   ├── dashboard-overview.png
│   ├── fraud-map.png
│   └── risk-distribution.png
│
├── data/
│   ├── transactions.csv
│   └── resultado.csv
│
├── models/
│   └── fraud_model.pkl
│
├── generate_data.py
├── detector.py
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Luiz-Salles/fraudshield-ai.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Generate the dataset:

```bash
python generate_data.py
```

Train the model:

```bash
python detector.py
```

Launch the dashboard:

```bash
streamlit run app.py
```

---

## Example Use Cases

* Banking fraud monitoring
* Financial risk assessment
* Transaction anomaly detection
* Fraud investigation support
* Risk analytics dashboards
* Financial behavior monitoring

---

## Future Improvements

* Real-time transaction ingestion
* REST API integration
* User authentication and authorization
* Explainable AI (XAI) module
* Advanced fraud scoring models
* Database integration
* Cloud deployment
* Automated alerting system

---

## Skills Demonstrated

This project demonstrates practical experience with:

* Machine Learning
* Data Analysis
* Fraud Detection
* Risk Analytics
* Data Visualization
* Python Development
* Dashboard Development
* Feature Engineering
* Git Version Control
* Software Project Structure

---

## Author

**Luiz Felipe Salles Alves**

GitHub:
https://github.com/Luiz-Salles
