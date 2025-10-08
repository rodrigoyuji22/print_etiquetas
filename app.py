from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from pathlib import Path
import os

from services.query_service import *
from services.print_service import print_
from services.label_service import *

load_dotenv()
app = Flask(__name__)

printerTransporte, printerExpedicao, printerGalpao = os.getenv("PRINTER_TRA"), os.getenv("PRINTER_EXPEDICAO"), os.getenv("PRINTER_GALPAO2")
template_transporte, template_expedicao, template_estoque = Path("zpl/transito.zpl"), Path("zpl/expedicao.zpl"), Path("zpl/estoque.zpl")
host, port = os.getenv("HOST_API"), int(os.getenv("PORT_API", 1234))




@app.route('/')
def home():
    return render_template("index.html")

@app.route('/estoque')
def estoque_page():
    return render_template("estoque.html")

@app.route('/expedicao')
def expedica_page():
    return render_template("expedicao.html")

@app.route('/transporte')
def transporte_page():
    return render_template("transporte.html")

@app.route('/print/transporte', methods=['POST'])
def print_transporte():
    try:
        data = request.get_json()
        nf = data.get('nf')
        vol = int(data.get('vol',1))

        if nf:
            nf = nf.strip().upper()
            if not nf.startswith("NF "):
                if nf.startswith("NF") and not nf.startswith("NF "):
                    nf = nf.replace("NF", "NF ")
                else:
                    nf = f"NF {nf}"

        df = run_query_tra(nf)
        if df.empty: # type: ignore
            return jsonify({'error': 'NF não encontrada'}), 404
    
        for i in range(1, vol+1):
            vol_str = f"{i:02d}/{vol:02d}"
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
        printer_choice = data.get('printer')
        n = data.get('n', 1)

        if not itemCode:
            return jsonify({'error': 'Campo Código do item obrigatório'}), 400
        if not lote:
            return jsonify({'erro no lote'})
        printer = printerGalpao if printer_choice == 'galpao' else printerExpedicao
        df = run_query_est(itemCode)
        zpl = render_labels(df, template_estoque, qtd=qtd, peso=peso, lote=lote)
        for i in range(0, n):
            print_(zpl, printer)
        return jsonify({
            'status': 'success', 
            'message': 'Etiqueta inserida na fila de impressao'
        }), 201

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500
    
@app.route('/print/expedicao', methods=['POST']) # type: ignore
def print_expedicao():
    try:
        data = request.get_json()
        pv = data.get('pv')
        itemCode = data.get('itemCode')
        qtd = data.get('qtd')
        peso = data.get('peso')
        lote = data.get('lote')
        printer_choice = data.get('printer')
        n = data.get('n')

        df = run_query_exp(pv)
        if df.empty: # pyright: ignore[reportOptionalMemberAccess]
            return jsonify({'error': 'insira um pv valido'}), 404

        if not itemCode:
            return jsonify({'error': 'Selecione um item para impressão'}), 400

        normalized_item = str(itemCode).strip()
        filtered_df = df[df["item_code"].astype(str).str.strip() == normalized_item]
        if filtered_df.empty:
            return jsonify({'error': 'Item selecionado não pertence ao PV informado'}), 404

        selected_row = filtered_df.iloc[0]
        printer = printerGalpao if printer_choice == 'galpao' else printerExpedicao
        zpl = render_labels(selected_row, template_expedicao, qtd=qtd, peso=peso, lote=lote)
        total_labels = int(n) if n else 1
        for _ in range(total_labels):
            print_(zpl, printer)
        return jsonify({
            'status': 'success',
            'message': 'Etiqueta enviada para impressão com sucesso!'
        }), 201
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500
    
@app.route('/consulta/expedicao', methods=['POST'])
def consulta_expedicao():
    try:
        data = request.get_json()
        pv = data.get('pv')

        if not pv:
            return jsonify({'error': 'Pedido de venda invalido'})
        df = run_query_exp(pv)
        if df.empty: # type: ignore
            return jsonify({'error': 'Pedido de venda vazio'})
        return df.to_dict(orient = 'records') # type: ignore
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500
        
@app.route('/consulta/estoque', methods=['POST'])
def consulta_estoque():
    try:
        data = request.get_json()
        itemCode = data.get('itemCode', '').strip()

        if not itemCode:
            return jsonify({'error': 'Digite parte do código ou nome do item'}), 400

        df = run_query_est(itemCode)
        if df.empty: # type: ignore
            return jsonify({'error': 'Nenhum item encontrado'}), 404

        return df.to_dict(orient='records') # type: ignore

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

        
if __name__ == '__main__':
    app.run(host=host, port=port, debug=False, threaded=True)