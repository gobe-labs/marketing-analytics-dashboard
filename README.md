# marketing-analytics-dashboard
This project demonstrates the full lifecycle of a marketing analytics workflow — from raw data ingestion and cleaning to SQL-based analytics and interactive visualization in Tableau.
It simulates the work of a Data Analyst, showcasing my skills in:
- Data cleaning & transformation
- KPI engineering
-SQL analytics
- Dashboard design & storytelling
- GitHub documentation
- Reproducible pipeline design

# Project File Structure
```bash
marketing-analytics-dashboard/
│
├── .vscode/
│   └── settings.json
│
├── dashboard/
│   ├── marketing_dashboard.twbx
│   └── screenshots/
│       ├── cleaned_data_preview.jpeg
│       ├── dashboard_preview.jpeg
│       └── sql_results.png
│
├── data/
│   ├── processed/
│   │   └── cleaned_marketing_data.csv
│   └── raw/
│       ├── marketing_campaign_dataset.csv
│       └── marketing_dashboard.db
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   └── 02_etl_to_sql.ipynb
│
├── reports/
│   ├── overall_channel_performance.csv
│   ├── top_campaign_types_by_roi.csv
│   └── top_campaigns_by_conversion_rate.csv
│
├── scripts/
│   ├── config.py
│   ├── etl_pipeline.py
│   ├── run_all.py
│   ├── utils.py
│   └── __pycache__/
│       ├── config.cpython-312.pyc
│       ├── etl_pipeline.cpython-312.pyc
│       └── utils.cpython-312.pyc
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```
# Overview

Modern marketing teams rely heavily on performance analytics to guide spending decisions.
This project builds an end-to-end solution to analyze marketing effectiveness across channels, campaigns, and companies.

# Tech Stack
## Languages
- Python (Pandas, NumPy)
- SQL (SQLite)

## Tools
- Tableau (Dashboard & Visualization)
- Jupyter Notebook
- Git & GitHub
- SQLAlchemy (optional)

## Concepts

- ETL Pipeline Design
- Data Cleaning & Feature Engineering
- KPI Development
- SQL Aggregation & Ranking
- Business Intelligence Dashboarding

# ETL Pipeline Flow

## Raw Data → Cleaned Dataset (Python)

### Notebook 01_data_cleaning.ipynb performs:

- Column normalization
- Missing value handling
- Type conversions
- Normalizing categorical fields
- Numeric normalization

 **KPI calculations:**

| KPI              | Formula                   | Result                  |
| ---------------- | ------------------------- | ------------------------ |
| CTR              | Clicks / Impressions      | Engagement               |
| CPC              | Acquisition Cost / Clicks | Cost efficiency          |
| Conversion Rate  | Conversions / Clicks      | Lead efficiency          |
| ROI              | Revenue / Cost            | Financial performance    |
| Efficiency Index | ROI * CR / Cost           | Overall campaign quality |


## Cleaned Dataset → SQL Database (SQLite)

Notebook `02_etl_to_sql.ipynb` loads the cleaned data into `marketing_dashboard.db`.

Analytical SQL queries calculate:

- Average ROI per campaign type

- Highest conversion rates across companies

- CTR, CPC, ROI per marketing channel

All SQL outputs export into `/reports/` as CSVs for Tableau.

## Dashboard Creation (Tableau)

The Tableau dashboard visualizes marketing performance using:

- KPI Summary Bar (CTR, CPC, Conversion Rate, ROI)
- Channel Performance Analysis
- Campaign Type ROI Ranking
- Top Campaigns by Conversion Rate
- Interactive filters: Campaign Type, Channels, Date

Dashboard includes:

- Performance indicators
- Channel efficiency insights
- Lead generation strength
- Spend efficiency at a glance

## Key Insights (Example)

- Email campaigns produced the highest ROI with low CPC.
- Product Launch campaigns delivered superior conversion rates.
- Social Media drove high impressions but below-average CTR.
- Direct marketing showed strong ROI consistency across segments.


# How to Run the Project
### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/marketing-analytics-dashboard.git
cd marketing-analytics-dashboard
```
### 2. Add raw dataset

Place your `marketing_campaign.csv` into:
```
data/raw/
```
### 3. Run Data Cleaning Notebook

Open:
```
notebooks/01_data_cleaning.ipynb
```

This outputs:
```
data/processed/cleaned_marketing_data.csv
```
### 4. Run SQL ETL Notebook

Open:
```
notebooks/02_etl_to_sql.ipynb
```

This outputs reports into:
```
/reports/
```
### 5. Open Tableau Dashboard

Load:
```
dashboard/marketing_dashboard.twbx
```
Or connect directly to the CSVs in /reports/.
***

### Possible Future Enhancements

- Automate ETL with a single Python script

- Add logistic regression to predict high-ROI campaigns

- Integrate Google Ads / Meta Ads API for real-time data

- Add a Streamlit web app version of the dashboard

- Publish analysis insights to Medium / LinkedIn




***
Pull requests are welcome :). Feel free to open issues for feature requests or bugs.