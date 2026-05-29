# Insurance Risk Analytics

## Project Overview

This project focuses on insurance risk analytics and predictive modeling for risk-based pricing. The objective is to analyze insurance policy and claims data, validate business hypotheses, and build machine learning models that support dynamic premium pricing decisions.

The project is divided into four major tasks:

1. Exploratory Data Analysis (EDA)
2. Data Version Control (DVC)
3. A/B Hypothesis Testing
4. Statistical Modeling & Risk-Based Pricing

---

# Project Structure

```text
insurance-risk-analytics/
├── .github/
│   └── workflows/
│       └── ci.yml
├── data/
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_hypothesis_testing.ipynb
│   └── 03_modeling.ipynb
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── eda_utils.py
│   ├── hypothesis_tests.py
│   └── modeling.py
├── reports/
│   └── final_report.md
├── tests/
├── .dvc/
├── .gitignore
├── dvc.yaml
├── requirements.txt
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/hawaebrahimhamid-png/insurance-risk-analytics.git
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Task 1: Exploratory Data Analysis (EDA)

## Objective

Understand the insurance dataset through statistical summaries and visual analysis.

## Activities

* Data summarization
* Missing value analysis
* Univariate analysis
* Bivariate analysis
* Geographic trend analysis
* Outlier detection
* Loss ratio analysis
* Temporal trend analysis

## Key Insights

* TotalClaims contains significant outliers
* Some provinces show higher loss ratios
* Vehicle type influences claim severity
* Premium and claims have weak positive correlation

## Deliverables

* `01_eda.ipynb`
* Reusable utility functions in `src/eda_utils.py`
* Insight-driven visualizations

---

# Task 2: Data Version Control (DVC)

## Objective

Create a reproducible data pipeline using DVC.

## Activities

* Initialized DVC
* Added local DVC remote storage
* Tracked datasets using DVC
* Versioned raw and cleaned datasets

## DVC Commands

```bash
dvc init
dvc add data/insurance_data.csv
dvc push
```

## Deliverables

* DVC-tracked datasets
* `.dvc` files committed to Git
* Reproducible data pipeline

---

# Task 3: A/B Hypothesis Testing

## Objective

Validate statistical hypotheses related to insurance risk drivers.

## Hypotheses Tested

* Risk differences across provinces
* Risk differences across zip codes
* Margin differences across zip codes
* Risk differences between genders

## Statistical Tests Used

* Chi-Square Test
* Independent T-Test

## Results

* Some provinces showed statistically significant risk differences
* Margin differences were observed across selected zip codes
* Gender-based risk differences were minimal

## Deliverables

* `02_hypothesis_testing.ipynb`
* `src/hypothesis_tests.py`
* Results summary table
* Business recommendations

---

# Task 4: Statistical Modeling & Risk-Based Pricing

## Objective

Build predictive models for claim severity and premium optimization.

## Data Preparation

* Missing value handling
* Feature engineering
* Categorical encoding
* Train-test splitting

## Models Implemented

### Regression Models

* Linear Regression
* Random Forest Regressor
* XGBoost Regressor

### Classification Model

* Random Forest Classifier

## Evaluation Metrics

### Regression

* RMSE
* R² Score

### Classification

* Accuracy
* Precision
* Recall
* F1 Score

## Premium Optimization Formula

```text
Premium =
(P(claim) × Predicted Severity)
+ Expense Loading
+ Profit Margin
```

## Feature Importance

SHAP analysis was used to identify the most influential features affecting claim severity and premium prediction.

## Key Findings

* Higher premiums are associated with higher predicted claims
* Vehicle age impacts claim severity
* Province and vehicle type strongly influence insurance risk

## Deliverables

* `03_modeling.ipynb`
* `src/modeling.py`
* SHAP visualizations
* Model comparison table

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost
* SHAP
* DVC
* Git & GitHub

---

# Reproducing the Project

## Pull DVC Data

```bash
dvc pull
```

## Run Notebooks

Open Jupyter Notebook:

```bash
jupyter notebook
```

---

# Author

Hawa Ebrahim Hamid

---

# License

This project is for educational purposes.
