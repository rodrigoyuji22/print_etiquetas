import requests
import streamlit as st
from interface import load_css

api_url = st.secrets["api"]["url"]

load_css()

with st.form("forms_transporte"):
    st.title("Etiqueta de Transporte")
    nf = st.text_input("Número da NF:")
    vol = st.text_input("Quantidade de Volumes:")
    
    submitted = st.form_submit_button("Imprimir Etiqueta")
    if submitted:
        if not nf:
            st.warning("Insira uma NF")
        else:
            if not vol:
                vol = 1
            data = {'nf': nf, 'vol': vol}
            try:
                response = requests.post(f"{api_url}/print/transporte", json=data)
                if response.status_code == 200:
                    st.success("✅ Etiquetas inseridas na fila!")
            except Exception as e:
                st.error("NF inválida")

if st.button("Voltar", key="key1", use_container_width=False):
    st.switch_page("interface.py")





