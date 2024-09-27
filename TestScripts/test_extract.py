import pandas as pd
import pytest
from sqlalchemy import create_engine,text
import cx_Oracle
# Create MySQL database connection
mysql_engine = create_engine('mysql+pymysql://root:Admin%40143@localhost:3308/enterpriseretaildwh')

oracle_engine = create_engine('oracle+cx_oracle://system:admin@localhost:1521/xe')

def test_sales_data_Extraction():
    expected_df = pd.read_csv("TestData/sales_data.csv")
    query = "select * from staging_sales"
    actual_df = pd.read_sql(query, mysql_engine)
    assert actual_df.equals(expected_df), f"Data extraction failed."
    print("Sales data extarcted and laoded to staging successfuly")
