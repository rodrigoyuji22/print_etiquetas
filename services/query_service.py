from db import _getConnection
from queries import *
import pandas as pd

def run_query_tra(nf):
    try:
        with open("../queries/transito.sql", "r") as f:
            query = f.read()
        with _getConnection() as conn:
            return pd.read_sql(query, conn, params=[nf])
    except Exception as e:
        print("Erro na consulta")
        raise e  # raise para avisar a API que houve erro na query 

def run_query_est(itemCode):
        with open("../queries/estoque.sql") as f:
            query_template = f.read()

        condicoes = []
        params_arr = []

        if itemCode:
            itemCodeStr = str(itemCode)
            if len(itemCodeStr) >= 15:
                condicoes.append(f"AND T0.ItemCode = ?")
                params_arr.append(itemCodeStr)
            else:
                condicoes.append(f"AND T0.ItemCode LIKE ?")
                params_arr.append(f"{itemCodeStr}%")
        
        

                 