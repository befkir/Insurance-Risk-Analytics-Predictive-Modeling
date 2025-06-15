# 🚗 Insurance Risk Analysis - EDA & Data Version Control

This repository contains the exploratory data analysis (EDA), project planning, and data versioning setup for an insurance portfolio analysis project. The main objective is to uncover risk and profitability patterns in the insurance dataset and ensure full reproducibility of results using Git, GitHub, and DVC.

## 📌 Project Objectives

- Analyze risk patterns in insurance claims and premiums.
- Identify trends by geography, vehicle type, and customer attributes.
- Establish a reproducible and auditable workflow for data and model tracking.

## 🧠 Tasks Breakdown

### 🔹 Task 1: Git, GitHub & Exploratory Data Analysis (EDA)

- Created a GitHub repository with proper branching (`task-1`) and version control.
- Performed EDA to analyze:
  - **Loss Ratio** trends across Province, Gender, and Vehicle Type.
  - **Distribution** of financial variables (TotalClaims, TotalPremium, CustomValueEstimate).
  - **Outliers**, **temporal trends**, and **geographic impact**.
- Shared key insights using descriptive statistics and advanced visualizations.
- Setup basic **CI/CD** with GitHub Actions (optional).

### 🔹 Task 2: Data Version Control with DVC

- Installed and initialized DVC in the project directory.
- Configured local remote storage for data reproducibility.
- Tracked datasets with `.dvc` files and pushed to local storage.
- Ensured all changes are committed to Git for traceability.

## 📁 Project Structure

```
insurance-risk-eda/
├── data/                        # Raw data (tracked via DVC)
│   └── insurance_data.csv
├── notebooks/
│   └── eda_insurance.ipynb      # Jupyter notebook with EDA
├── .github/                # GitHub workflows and CI
│   └── workflows/
├── .vscode/                # Editor settings
├── scripts/
├── src/
├── tests/                  # Unit tests
├── output/                 # plot will be saved here
├── .dvc/                        # DVC internal config
├── .gitignore
├── README.md
└── requirements.txt
```
