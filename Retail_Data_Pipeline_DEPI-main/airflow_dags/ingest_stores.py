import pandas as pd
import pymssql
import os

def ingest_stores():
    DB_PASSWORD = os.getenv('MSSQL_SA_PASSWORD', 'SuperStrong_SQL_Pass_2026!')
    try:
        conn = pymssql.connect(server='sqlserver', user='sa', password=DB_PASSWORD, database='master')
        file_path = '/opt/airflow/data/raw/stores.csv'
        df = pd.read_csv(file_path)
        print(f'Uploading {len(df)} stores...')
        cursor = conn.cursor()
        cursor.execute("IF OBJECT_ID('stores', 'U') IS NOT NULL DROP TABLE stores")
        cursor.execute('CREATE TABLE stores (Store INT, Type NVARCHAR(5), Size INT)')
        for _, row in df.iterrows():
            cursor.execute('INSERT INTO stores VALUES (%d, %s, %d)', (int(row['Store']), str(row['Type']), int(row['Size'])))
        conn.commit()
        conn.close()
        print('Upload completed successfully!')
    except Exception as e:
        print(f'Error occurred: {e}')

if __name__ == '__main__':
    ingest_stores()
