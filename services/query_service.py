from db import _getConnection
import pandas as pd

def run_query_tra(nf):
    try:
        with open("../queries/transito.sql", "r", encoding="utf-8") as f:
            query = f.read()
        if nf:
            with _getConnection() as conn:
                return pd.read_sql(query, conn, params=[nf])
    except Exception as e:
        print("Erro na consulta")
        raise e  # raise para avisar a API que houve erro na query 


def run_query_est(itemCode):
    try:
        with open("../queries/estoque.sql", "r", encoding="utf-8") as f:
            query= f.read()
        if itemCode:
            with _getConnection() as conn:
                return pd.read_sql(query, conn, params=[itemCode])
    except Exception as e:
        print("Erro na consulta")
        raise e
        

def run_query_exp(pv, itemCode):
    try:
        with open("../queries/expedicao.sql") as f:
            query = f.read()
        if itemCode and pv:
            with _getConnection() as conn:
                return pd.read_sql(query, conn, params=[pv, itemCode])
    except Exception as e:
        print("Erro na consulta")
        raise e    