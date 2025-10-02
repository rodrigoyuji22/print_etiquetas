from db import run_query_est, run_query_exp, run_query_tra
from label_service import render_labels, render_transport_label
from pathlib import Path

zpl_path1 = Path("templates/expedicao.zpl")
zpl_path2 = Path("templates/estoque.zpl")

def main():
    # df = run_query_exp("63169", "7")
    # z = render_label(df, zpl_path1, "50")
    # print(z)
    df = run_query_tra("NF 73187")
    print(df)
    z = render_transport_label(df)
    print(z)
    

main()