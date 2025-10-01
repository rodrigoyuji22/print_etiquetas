import pyodbc
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
serverName, dataBase, uid, pwd = os.getenv("DB_SERVER_NAME"), os.getenv("DB_SERVER_BASE"), os.getenv("DB_UID"), os.getenv("DB_PWD")

def _getConnection() -> pyodbc.Connection:
    connectionString = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={serverName};"
        f"DATABASE={dataBase};"
        f"UID={uid};"
        f"PWD={pwd};"
        "Encrypt=no;"
        "TrustServerCertificate=yes;"
    )
    return pyodbc.connect(connectionString)


def run_query(pv, itemCode):
    with open("queries/label.sql", "r") as f:
        query_template = f.read()

    # monta o filtro dinamicamente (igual VBA)
    if itemCode and len(str(itemCode)) >= 15:
        filtro_item = f"AND T1.ItemCode = '{itemCode}'"
    elif itemCode:
        filtro_item = f"AND T1.ItemCode LIKE '{itemCode}%'"
    else:
        filtro_item = ""

    # substitui os placeholders no SQL
    query = query_template.format(pv=pv, filtro_item=filtro_item)

    with _getConnection() as conn:
        return pd.read_sql(query, conn)


