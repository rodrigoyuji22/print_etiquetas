from db import *
from services.label_service import *
from pathlib import Path
from services.print_service import print_tra

zpl_path1 = Path("templates/expedicao.zpl")
zpl_path2 = Path("templates/estoque.zpl")

load_dotenv()
printerTransporte, printerExpedicao, printerGalpao2 = os.getenv("PRINTER_TRA"), os.getenv("PRINTER_EXPEDICAO"), os.getenv("PRINTER_GALPAO2")


def main():
    # df = run_query_exp("63169", "7")
    # z = render_label(df, zpl_path1, "50")
    # print(z)
    df = run_query_tra("NF 73187")
    print(df)
    zpl = render_transport_label(df)
    print_tra(zpl, printerTransporte)
    
    
main()