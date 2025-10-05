import win32print 
from dotenv import load_dotenv
import os


def print_tra(zpl, printer):
    hPrinter = win32print.OpenPrinter(printer)
    try:
        jobId = win32print.StartDocPrinter(hPrinter, 1,("etiqueta", "", "RAW"))
        win32print.StartPagePrinter(hPrinter)
        win32print.WritePrinter(hPrinter, zpl.encode("utf-8"))
    finally:
        win32print.EndPagePrinter(hPrinter)
        win32print.EndDocPrinter(hPrinter)
        win32print.ClosePrinter(hPrinter)
