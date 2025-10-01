from db import run_query
from label_service import render_label
from pathlib import Path

query_path = Path("queries/label.sql")
zpl_path = Path("templates/label.zpl")
def main():
    df = run_query(63169, "79813513PA200000")
    z = render_label(df, zpl_path)
    print(z)


main()