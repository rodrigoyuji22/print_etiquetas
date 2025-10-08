from collections.abc import Mapping
from typing import Any

import pandas as pd


def _normalize_row(data: Any) -> Mapping[str, Any]:
    if isinstance(data, pd.DataFrame):
        if data.empty:
            raise ValueError("DataFrame vazio recebido para impressão")
        return data.iloc[0].to_dict()
    if isinstance(data, pd.Series):
        return data.to_dict()
    if isinstance(data, Mapping):
        return dict(data)
    raise TypeError("Formato de dados não suportado para renderização da etiqueta")


def render_labels(data, path, qtd="", peso="", lote=""):
    with open(path, "r", encoding="utf-8") as f:
        zpl = f.read()

    row = _normalize_row(data)

    for column, value in row.items():  # percorre as colunas da linha selecionada
        placeholder = "{{" + str(column) + "}}"
        valor = "" if value in (None, "None") else str(value)
        zpl = zpl.replace(placeholder, valor)

    if qtd:
        zpl = zpl.replace("{{qtd}}", str(qtd))
    if peso:
        zpl = zpl.replace("{{peso}}", str(peso))
    if lote:
        zpl = zpl.replace("{{lote}}", str(lote))
    return zpl

def render_transport_label(df, vol = "1"):
    with open("zpl/transito.zpl") as f:
        zpl = f.read()
    row = df.iloc[0]
    for i in df.columns:
        placeholder = "{{" + i + "}}"
        if row[i] != None:
            zpl = zpl.replace(placeholder, str(row[i]))
    zpl = zpl.replace("{{vol}}", str(vol))
    return zpl
