import os
import sqlite3
import pandas as pd

from utils import clean_text_columns, convert_numeric, compute_kpis, log
from config import (
    RAW_DATA_PATH, PROCESSED_DATA_PATH, DB_PATH, REPORTS_DIR, TABLE_NAME
)

# Ensure required folders exist
os.makedirs("../data/processed", exist_ok=True)
os.makedirs("../reports", exist_ok=True)

def load_raw_data():
    if not os.path.exists(RAW_DATA_PATH):
        raise FileNotFoundError(
            f"Raw dataset not found at {RAW_DATA_PATH}. Upload marketing_campaign_dataset.csv."
        )
    log("Loading raw dataset...")
    return pd.read_csv(RAW_DATA_PATH)

def clean_data(df):
    log("Cleaning dataset...")

    text_columns = [
        "Company", "Campaign_Type", "Target_Audience", "Channels_Used",
        "Location", "Language", "Customer_Segment"
    ]
    numeric_columns = [
        "Duration", "Conversion_Rate", "Acquisition_Cost", "ROI",
        "Clicks", "Impressions", "Engagement_Score"
    ]

    df.drop_duplicates(inplace=True)
    df.fillna(0, inplace=True)

    df = clean_text_columns(df, text_columns)
    df = convert_numeric(df, numeric_columns)

    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    df = compute_kpis(df)
    return df

def save_cleaned_data(df):
    df.to_csv(PROCESSED_DATA_PATH, index=False)
    log(f"Cleaned data saved to {PROCESSED_DATA_PATH}")

def load_to_sql(df):
    log("Loading cleaned data into SQLite database...")
    conn = sqlite3.connect(DB_PATH)
    df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)
    conn.close()
    log(f"Data loaded into table '{TABLE_NAME}' in {DB_PATH}")

def run_queries():
    log("Running analytical queries...")

    queries = {
        "top_campaign_types_by_roi": f"""
            SELECT Campaign_Type, ROUND(AVG(ROI), 2) AS Avg_ROI
            FROM {TABLE_NAME}
            GROUP BY Campaign_Type
            ORDER BY Avg_ROI DESC
            LIMIT 5;
        """,
        "top_campaigns_by_conversion_rate": f"""
            SELECT Company, Campaign_Type, ROUND(AVG(Conversion_Rate)*100, 2) AS Avg_Conversion_Rate
            FROM {TABLE_NAME}
            GROUP BY Company, Campaign_Type
            ORDER BY Avg_Conversion_Rate DESC
            LIMIT 5;
        """,
        "overall_channel_performance": f"""
            SELECT Channel_Used, 
                   ROUND(AVG(CTR)*100, 2) AS Avg_CTR, 
                   ROUND(AVG(CPC), 2) AS Avg_CPC,
                   ROUND(AVG(ROI), 2) AS Avg_ROI
            FROM {TABLE_NAME}
            GROUP BY Channel_Used
            ORDER BY Avg_ROI DESC;
        """
    }

    conn = sqlite3.connect(DB_PATH)

    for name, query in queries.items():
        df = pd.read_sql_query(query, conn)
        output_path = os.path.join(REPORTS_DIR, f"{name}.csv")
        df.to_csv(output_path, index=False)
        log(f"Exported {name}.csv")

    conn.close()

def run_etl_pipeline():
    log("=== Starting ETL Pipeline ===")

    df_raw = load_raw_data()
    df_clean = clean_data(df_raw)
    save_cleaned_data(df_clean)
    load_to_sql(df_clean)
    run_queries()

    log("=== ETL Pipeline Complete ===")

if __name__ == "__main__":
    run_etl_pipeline()