def render_labels(df, path, qtd = "", peso = "", lote =""):
    with open(path, "r", encoding="utf-8") as f:
        zpl = f.read()
    row = df.iloc[0]

    for i in df.columns:  # for in in df.columns itera o nome das columns
        placeholder = "{{"+i+"}}"
        if row[i]:
            valor = str(row[i])
        else:
            valor = ""
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