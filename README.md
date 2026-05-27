# Retail-Data-Pipeline
End-to-end retail data pipeline: multi-source ingestion, Python cleaning, PostgreSQL &amp; SQL Server storage, Parquet optimization, and Power BI analytics dashboard.
# 🛒 Retail Data Pipeline

An end-to-end retail data engineering project built as part of the **DEPI initiative**. The pipeline extracts data from multiple sources, cleans and transforms it with Python, stores it in SQL Server, and delivers analytics-ready insights via a Power BI dashboard.

---

## 📌 Project Overview

| Layer | Technology |
|-------|-----------|
| Orchestration | Apache Airflow 2.8.1 |
| Containerization | Docker & Docker Compose |
| Data Storage | SQL Server 2022 + PostgreSQL 13 |
| Data Format | CSV → Parquet (optimized) |
| Transformation | Python (pandas, pyarrow) |
| Visualization | Power BI Desktop |

---

## 🏗️ Architecture

```
Kaggle CSVs
(train, features, stores)
        │
        ▼
┌─────────────────┐
│  Apache Airflow  │  ← Orchestrates the pipeline
│  (Docker)        │
└────────┬────────┘
         │
    ┌────┴─────┐
    │          │
    ▼          ▼
SQL Server   Parquet Files
(stores)     (train, features)
    │          │
    └────┬─────┘
         │
         ▼
   Power BI Dashboard
   (Sales Analytics &
    Data Quality)
```

---

## 📂 Project Structure

```
Retail_Data_Pipeline_DEPI/
├── airflow_dags/
│   ├── ingest_stores.py        # Load stores.csv into SQL Server
│   ├── convert_to_parquet.py   # Convert CSVs to Parquet format
│   ├── clean_data.py           # Data cleaning & validation
│   └── pipeline_dag.py         # Airflow DAG definition
├── docker/
│   ├── docker-compose.yml      # Full stack: Airflow + SQL Server + Postgres
│   ├── .env                    # Environment variables (not committed)
│   └── data/
│       └── raw/                # Place Kaggle CSVs here
├── visualization_powerbi/
│   ├── RetailDashboard.pbix    # Power BI dashboard file
│   └── RetailPipeline_Theme.json # Custom Power BI theme
└── README.md
```

---

## 📊 Dataset

**Walmart Store Sales Forecasting** from Kaggle:
- `train.csv` — 421K weekly sales records across 45 stores and 99 departments
- `features.csv` — Store-level features (temperature, fuel price, markdowns, CPI, unemployment)
- `stores.csv` — Store metadata (type A/B/C, size)

> Download from: https://www.kaggle.com/competitions/walmart-recruiting-store-sales-forecasting/data

---

## 🚀 Getting Started

### Prerequisites
- Docker Desktop
- Power BI Desktop
- Git

### 1. Clone the repo
```bash
git clone https://github.com/Dahoomshaheen/Retail_Data_Pipeline_DEPI.git
cd Retail_Data_Pipeline_DEPI
```

### 2. Add Kaggle data
Place `train.csv`, `features.csv`, and `stores.csv` in:
```
docker/data/raw/
```

### 3. Create the .env file
```bash
cd docker
cp .env.example.txt .env
```
Fill in your passwords in the `.env` file.

### 4. Start the pipeline
```bash
docker-compose up -d
```

### 5. Run the ETL scripts
```bash
docker exec -it docker-airflow-scheduler-1 python /opt/airflow/dags/ingest_stores.py
docker exec -it docker-airflow-scheduler-1 python /opt/airflow/dags/convert_to_parquet.py
```

### 6. Open the dashboard
Open `visualization_powerbi/RetailDashboard.pbix` in Power BI Desktop.
Connect to SQL Server at `localhost,1433` with username `sa`.

---

## 📈 Dashboard Highlights

- **$6.74B** total weekly sales across all stores
- **Store Type A** accounts for ~70% of all sales
- **92.5%** of sales occur during non-holiday weeks
- Sales trend visible from 2010 to 2012 across 45 stores
- Per-store breakdown with Type, Size, and total revenue

---

## 🛠️ Pipeline Steps

| Step | Script | Description |
|------|--------|-------------|
| 1 | `ingest_stores.py` | Loads store metadata into SQL Server |
| 2 | `convert_to_parquet.py` | Converts raw CSVs to optimized Parquet (72% size reduction) |
| 3 | `clean_data.py` | Handles nulls, negatives, and schema validation |
| 4 | `build_star_schema.py` | Builds dimensional model in SQL Server |

---

## 👥 Team

Built as part of the **Digital Egypt Pioneers Initiative (DEPI)** — Data Engineering track.

---

## 📄 License

MIT License — free to use and modify.
