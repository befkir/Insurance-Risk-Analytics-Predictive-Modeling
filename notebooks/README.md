## 📂 `notebooks/` Folder

This directory contains Jupyter notebooks that document the exploratory data analysis (EDA)

### Suggested README Content for `notebooks/`

# 📂 Notebooks

This folder contains Jupyter notebooks for exploring and analyzing Insurance data of the insurance risk and profitability project..

## 🧪 Main Notebook

### `eda_insurance.ipynb`

This notebook includes:

- Data loading and preprocessing using functions from `src/preprocessing.py`
- Handling of missing values and data cleaning
- Exploratory Data Analysis (EDA) including:
  - Descriptive statistics
  - Loss ratio computation
  - Univariate, bivariate, and temporal trend analysis
- Creative and insightful visualizations using reusable utilities from `utils/visualization.py`
- All plots are saved to the `/output` directory and also displayed inline (if run in Jupyter)

## Usage

1.  Install dependencies using:

```
pip install -r requirements.txt
```

2. Run the script:

```
cd Scripts
python3 preprocessing.py
```
