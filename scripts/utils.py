import pandas as pd
import numpy as np

def clean_text_columns(df, columns):
    """Standardize text columns: strip, title case."""
    for col in columns:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.title()
    return df

def convert_numeric(df, columns):
    """Convert numeric columns to float and fill NaN."""
    for col in columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)
    return df

def compute_kpis(df):
    """Add CTR, CPC, Efficiency Index fields."""
    df["CTR"] = np.where(df["Impressions"] > 0, df["Clicks"] / df["Impressions"], 0)
    df["CPC"] = np.where(df["Clicks"] > 0, df["Acquisition_Cost"] / df["Clicks"], 0)
    df["Efficiency_Index"] = np.where(
        df["Acquisition_Cost"] > 0,
        df["ROI"] * df["Conversion_Rate"] / df["Acquisition_Cost"],
        0
    )
    return df

def log(message):
    """Simple console logger."""
    print(f"[INFO] {message}")