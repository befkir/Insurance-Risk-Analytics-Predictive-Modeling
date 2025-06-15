import pandas as pd

def load_data(filepath):
    """Load dataset from a CSV file."""
    return pd.read_csv(filepath)

def summarize_missing_values(df, threshold=0.5):
    """
    Summarizes missing values and optionally removes columns with too many missing values.
    
    Parameters:
        df (DataFrame): Input dataframe.
        threshold (float): If a column has more than this fraction of missing values, it will be dropped.
    
    Returns:
        df_cleaned (DataFrame): Cleaned dataframe
        dropped_columns (List): List of dropped column names
    """
    missing_summary = df.isnull().sum()
    print("📊 Missing Value Summary:")
    print(missing_summary[missing_summary > 0])

    # Drop columns with too many missing values
    dropped_columns = missing_summary[missing_summary > threshold * len(df)].index.tolist()
    df_cleaned = df.drop(columns=dropped_columns)

    print(f"\n🧹 Dropped {len(dropped_columns)} columns with > {threshold*100:.0f}% missing values:")
    print(dropped_columns)

    return df_cleaned, dropped_columns

def fill_missing_values(df):
    """
    Fills missing values with reasonable defaults or strategies.
    
    - Categorical: Fill with "Unknown"
    - Numeric: Fill with median
    """
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col].fillna("Unknown", inplace=True)
        else:
            df[col].fillna(df[col].median(), inplace=True)
    return df
