import win32print 

def print_tra(zpl):
    hPrinter = win32print.OpenPrinter("ZDesigner ZD230-203dpi ZPL Hugo")
    try:
        jobId = win32print.StartDocPrinter(hPrinter, 1,("Transporte", "", "RAW"))
        win32print.StartPagePrinter(hPrinter)
        win32print.WritePrinter(hPrinter, zpl.encode("utf-8"))
    finally:
        win32print.EndPagePrinter(hPrinter)
        win32print.EndDocPrinter(hPrinter)
        win32print.ClosePrinter(hPrinter)
