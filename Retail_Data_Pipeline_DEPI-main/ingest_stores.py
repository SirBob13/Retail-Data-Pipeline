import pandas as pd
from sqlalchemy import create_engine
import os

def ingest_stores():
    DB_PASSWORD = os.getenv('MSSQL_SA_PASSWORD', 'SuperStrong_SQL_Pass_2026!')
    connection_url = f'mssql+pyodbc://sa:{DB_PASSWORD}@sqlserver:1433/master?driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=yes'

    try:
        engine = create_engine(connection_url)
        file_path = '/opt/airflow/data/raw/stores.csv'
        df = pd.read_csv(file_path)
        print(f'Uploading {len(df)} stores...')
        df.to_sql(name='stores', con=engine, if_exists='replace', index=False)
        print('Upload completed successfully!')
    except Exception as e:
        print(f'Error occurred: {e}')

if __name__ == '__main__':
    ingest_stores()