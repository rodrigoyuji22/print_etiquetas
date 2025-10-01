def render_label(df, path):
    with open(path, "r", encoding="utf-8") as f:
        zpl = f.read()
    row = df.iloc[0]

    for i in df.columns:
        placeholder = "{{"+i+"}}" # criar a string q vai representar o nome do placeholder
        if row[i] != None:
            valor = str(row[i])
        else:
            valor = ""
        zpl = zpl.replace(placeholder, valor)
    return zpl

