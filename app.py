from flask import Flask, request, jsonify
from dotenv import load_dotenv
from pathlib import Path
import os

from services.query_service import *
from services.print_service import print_
from services.label_service import *

load_dotenv()
app = Flask(__name__)

printerTransporte, printerExpedicao, printerEstoque = os.getenv("PRINTER_TRA"), os.getenv("PRINTER_EXPEDICAO"), os.getenv("PRINTER_GALPAO2")
template_transporte, template_expedicao, template_estoque = Path("templates/transito.zpl"), Path("templates/expedicao.zpl"), Path("templates/estoque.zpl")
host, port = os.getenv("HOST_API"), int(os.getenv("PORT_API", 1234))




@app.route('/')
def home():
    return {'status': 'ok', 'message': 'API teste1'}

@app.route('/print/transporte', methods=['POST'])
def print_transporte():
    try:
        data = request.get_json()
        nf = data.get('nf')
        vol = int(data.get('vol',1))

        if not nf:
            return jsonify({'error': 'Campo NF obrigatório'}), 400

        df = run_query_tra(nf)
        if df.empty: # type: ignore
            return jsonify({'error': 'NF não encontrada'}), 404
    
        for i in range(1, vol+1):
            vol_str = f"{i:02d}/{vol}"
            zpl = render_transport_label(df, vol=vol_str)
            print_(zpl, printerTransporte)
        
        return jsonify({
            'status': 'success',
            'message': 'Etiquetas inseridas na fila de impressão'
        }), 201
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/print/estoque', methods=['POST'])
def print_estoque():
    try:
        data = request.get_json()
        itemCode = data.get('itemCode')
        lote = data.get('lote')
        qtd = data.get('qtd')
        peso = data.get('peso')

        if not itemCode:
            return jsonify({'error': 'Campo Código do item obrigatório'}), 400
        df = run_query_est(itemCode)
        zpl = render_labels(df, template_estoque, qtd, peso)
        print_(zpl, printerExpedicao)
        return jsonify({
            'status': 'success', 
            'message': 'Etiqueta inserida na fila de impressao'
        }), 201

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500
    
@app.route('/print/expedicao', methods=('POST')) # type: ignore
def print_expedicao():
    try:
        data = request.get_json()
        pv = data.get('pv')
        itemCode = data.get('itemCode')
        qtd = data.get('qtd')
        peso = data.get('peso')
        lote = data.get('lote')

        df = run_query_exp(pv, itemCode)
        if df.empty: # pyright: ignore[reportOptionalMemberAccess]
            return jsonify({'error': 'insira um pv valido'}), 404
        zpl = render_labels(df, template_expedicao, qtd, peso)
        print_(zpl, printerExpedicao)
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500
    
        






        
if __name__ == '__main__':
    app.run(host=host, port=port, debug=True, threaded=True)