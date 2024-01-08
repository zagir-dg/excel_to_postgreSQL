import pandas as pd
from sqlalchemy import create_engine

# Replace the values of the variables below with your own data
excel_file_path = r"C:\Users\employees.xlsx"
database_connection = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': '123456',
    'host': 'localhost',
    'port': '5432'
}
table_name = 'excel_to_postgres_table'

# Database scheme
schema_name = 'scheme example'
# Read data from the Excel file
df = pd.read_excel(excel_file_path)

# Create a connection to the PostgreSQL database
engine = create_engine(f'postgresql+psycopg2://{database_connection["user"]}' + 
                       f':{database_connection["password"]}@{database_connection["host"]}' + 
                       f':{database_connection["port"]}/{database_connection["dbname"]}')

# Write data to PostgreSQL
df.to_sql(table_name, engine, schema=schema_name, if_exists='replace', index=False)

print(f"Data successfully transferred to the table {table_name} in the {database_connection['dbname']} database")
