import os
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure output folder exists
os.makedirs("../output/", exist_ok=True)

def save_plot(fig, filename,show=False):
    """Save matplotlib figure to the output directory."""
    path = os.path.join("../output/", filename)
    fig.savefig(path, bbox_inches='tight')
    print(f"📸 Plot saved to: {path}")
    if show:
        plt.show()
    plt.close(fig)

def plot_histogram(series, title, filename, show=False):
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(series, bins=50, kde=True, ax=ax)
    ax.set_title(title)
    save_plot(fig, filename, show)

def plot_boxplot(data, x, y, title, filename, rotate=False, show=False):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(x=x, y=y, data=data, ax=ax)
    ax.set_title(title)
    if rotate:
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    save_plot(fig, filename, show)

def plot_bar(series, title, ylabel, filename, show=False):
    fig, ax = plt.subplots(figsize=(10, 5))
    series.plot(kind='bar', ax=ax)
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    save_plot(fig, filename, show)

def plot_time_series(df, title, filename, show=False):
    fig, ax = plt.subplots(figsize=(12, 5))
    df.plot(ax=ax)
    ax.set_title(title)
    ax.set_ylabel("Amount")
    save_plot(fig, filename, show)

def plot_heatmap(corr, title, filename, show=False):
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title(title)
    save_plot(fig, filename, show)

def plot_outlier_boxplots(df, columns, filename_prefix="outlier_", show=False):
    """
    Create and save boxplots for a list of numerical columns to detect outliers.

    Parameters:
        df (DataFrame): Data source
        columns (List[str]): Numerical columns to check
        filename_prefix (str): Prefix for output filenames
        show (bool): Whether to display the plot inline (for Jupyter)
    """
    for col in columns:
        fig, ax = plt.subplots(figsize=(10, 4))
        sns.boxplot(x=df[col], ax=ax)
        ax.set_title(f'Outlier Detection - {col}')
        filename = f"{filename_prefix}{col.lower()}.png"
        save_plot(fig, filename, show)

def count_outliers(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return ((series < lower) | (series > upper)).sum()