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


def run_query_exp(pv, itemCode):
    with open("queries/expedicao.sql", "r") as f:
        expedicao_template = f.read()

    if itemCode and len(str(itemCode)) >= 15:
        filtro_item = f"AND T1.ItemCode = '{itemCode}'"
    elif itemCode:
        filtro_item = f"AND T1.ItemCode LIKE '{itemCode}%'"
    else:
        filtro_item = ""

    query = expedicao_template.format(pv_=pv, filtro_item_=filtro_item)

    with _getConnection() as conn:
        return pd.read_sql(query, conn)
    
def run_query_est(itemCode, lote):
    with open("queries/estoque.sql", "r") as f:
        estoque_template = f.read()
    if itemCode and len(itemCode) >= 15:
        filtro_item2= f"AND T1.ItemCode = '{itemCode}'"
    elif itemCode:
        filtro_item2= f"AND T1.ItemCode LIKE '{itemCode}%'"
    else:
        filtro_item2 = ""

    if lote:
        filtro_lote = f"AND T1.BatchNum LIKE '{lote}%'"
    else:
        filtro_lote = ""

    query = estoque_template.format(filtro_item2_ = filtro_item2, filtro_lote_ = filtro_lote)
    with _getConnection() as conn:
        return pd.read_sql(query, conn)

def run_query_tra(nf):
    with open("queries/transito.sql", "r") as f:
        template_transport = f.read()
    nf_s = f"'{nf}'"
    query = template_transport.format(nf_ = nf_s)
    with _getConnection() as conn:
        return pd.read_sql(query, conn)