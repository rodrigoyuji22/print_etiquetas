import pyodbc
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