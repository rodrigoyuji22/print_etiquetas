def render_labels(df, path, qtd = 0, peso = 0):
    with open(path, "r", encoding="utf-8") as f:
        zpl = f.read()
    row = df.iloc[0]

    for i in df.columns: # for in in df.columns itera o nome das columns
        placeholder = "{{"+i+"}}" # criar a string q vai representar o nome do placeholder/coluna
        if row[i] != None:
            valor = str(row[i])
        else:
            valor = ""
        zpl = zpl.replace(placeholder, valor)

        if qtd != 0:
            zpl = zpl.replace("{{qtd}}", qtd)
        if peso != 0:
            zpl = zpl.replace("{{peso}}", peso)
    return zpl

def render_transport_label(df, vol = 0):
    with open("templates/transito.zpl") as f:
        zpl = f.read()
    row = df.iloc[0]
    for i in df.columns:
        placeholder = "{{" + i + "}}"
        if row[i] != None:
            zpl = zpl.replace(placeholder, str(row[i]))
    return zpl





