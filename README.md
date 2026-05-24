Insurance Risk Analytics & Predictive Modeling
1. Project Overview

This project performs end-to-end insurance risk analytics to understand customer behavior, claim patterns, and profitability drivers. The goal is to support data-driven decision-making for risk-based pricing and marketing optimization.

2. Business Objective

The main objective is to help insurance providers:

Identify low-risk and high-risk customer segments
Understand factors influencing insurance claims
Improve premium pricing strategies
Support data-driven marketing and underwriting decisions
3. Dataset Description

The dataset contains historical insurance policy and claims data including:

Customer demographics
Vehicle information
Policy details
Geographic location
Premium and claims data
Key Metrics:
TotalPremium → Total amount paid by customer
TotalClaims → Total claim amount
Loss Ratio = TotalClaims / TotalPremium
Margin = TotalPremium − TotalClaims
4. Project Structure
insurance-risk-analytics/
│
├── data/                     # Dataset (tracked using DVC)
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── cleaning.ipynb
│
├── src/
│   ├── eda_utils.py
│   ├── __init__.py
│
├── tests/
├── .dvc/
├── .github/workflows/
├── requirements.txt
└── README.md
5. Installation

Clone the repository:

git clone https://github.com/hawaebrahimhamid-png/insurance-risk-analytics.git
cd insurance-risk-analytics

Create virtual environment:

python -m venv venv
venv\Scripts\activate   # Windows

Install dependencies:

pip install -r requirements.txt
6. How to Run

Run Jupyter Notebook:

jupyter notebook

Then open:

notebooks/01_eda.ipynb
7. DVC Usage

This project uses DVC for data version control.

Initialize DVC:
dvc init
Pull data:
dvc pull
Track data:
dvc add data/insurance_data.csv
Push data to remote storage:
dvc push
8. CI Pipeline

GitHub Actions is used for Continuous Integration.

It automatically:

Installs dependencies
Runs pytest tests
Ensures code quality on every push

Workflow file:

.github/workflows/ci.yml
9. EDA Summary

Key insights from exploratory data analysis:

Claims vary significantly across provinces
Vehicle type and age strongly influence claim amounts
Data shows strong skewness in TotalClaims distribution
Clear seasonal trends observed in claims over time
Outliers exist in high-value claims
Business Insights:
High-risk regions require adjusted premium strategies
Vehicle characteristics should be included in pricing models
Seasonal patterns can support dynamic pricing strategies
10. Future Work
Build predictive models for claim severity
Implement classification model for claim probability
Improve feature engineering for better risk prediction
Add SHAP explainability for model interpretation
Expand DVC versioning for raw and processed datasets
🚀 Summary

This project demonstrates a full data science pipeline including:

Data ingestion
Exploratory data analysis
Data version control (DVC)
CI/CD pipeline setup
Business-driven insights