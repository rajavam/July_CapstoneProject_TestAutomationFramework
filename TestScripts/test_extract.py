import pandas as pd
import pytest
from sqlalchemy import create_engine
import cx_Oracle
import os

# Create MySQL database connection
mysql_engine = create_engine('mysql+pymysql://root:admin@localhost:3306/enterpriseretaildwh')

oracle_engine = create_engine('oracle+cx_oracle://system:admin@localhost:1521/xe')


def test_sales_data_Extraction():
    # Debugging the file path
    file_path = os.path.abspath("C:/Users/91801/PycharmProjects/Pythonbatch1/July_CapstoneProject_TestAutomationFramework/TestData/sales_data.csv")
    # Load the expected DataFrame from CSV file

    expected_df = pd.read_csv(file_path)
    print("sales data CSV data loaded successfully.")

    # Load the actual data from MySQL
    query = "SELECT * FROM staging_sales"
    actual_df = pd.read_sql(query, mysql_engine)
    assert actual_df.equals(expected_df), f"Data extraction failed."
    print("Data extraction and comparison successful.")

def test_product_data_Extraction():
    # Debugging the file path
    file_path = os.path.abspath("C:/Users/91801/PycharmProjects/Pythonbatch1/July_CapstoneProject_TestAutomationFramework/TestData/product_data.csv")
    # Load the expected DataFrame from CSV file

    expected_df = pd.read_csv(file_path)
    print("Product data CSV data loaded successfully.")

    # Load the actual data from MySQL
    query = "select * from staging_product;"
    actual_df = pd.read_sql(query, mysql_engine)
    assert actual_df.equals(expected_df), f"Data extraction failed."
    print("Data extraction and comparison successful.")

def test_inventory_data_Extraction():
    # Debugging the file path
    file_path = os.path.abspath("C:/Users/91801/PycharmProjects/Pythonbatch1/July_CapstoneProject_TestAutomationFramework/TestData/inventory_data.xml")
    # Load the expected DataFrame from CSV file

    expected_df = pd.read_xml(file_path)
    print("XML data loaded successfully.")

    # Load the actual data from MySQL
    query = "select * from staging_inventory;"
    actual_df = pd.read_sql(query, mysql_engine)
    assert actual_df.equals(expected_df), f"Data extraction failed."
    print("Data extraction and comparison successful.")

def test_supplier_data_Extraction():
    # Debugging the file path
    file_path = os.path.abspath("C:/Users/91801/PycharmProjects/Pythonbatch1/July_CapstoneProject_TestAutomationFramework/TestData/supplier_data.json")
    # Load the expected DataFrame from CSV file

    expected_df = pd.read_json(file_path)
    print("JSON data loaded successfully.")

    # Load the actual data from MySQL
    query = "select * from staging_supplier;"
    actual_df = pd.read_sql(query, mysql_engine)
    assert actual_df.equals(expected_df), f"Data extraction failed."
    print("Data extraction and comparison successful.")