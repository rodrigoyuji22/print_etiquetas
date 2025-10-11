import streamlit as st
import requests
from interface import load_css

api_url = st.secrets["api"]["url"]

load_css()

with st.form("form expedicao"):
    st.title("Etiqueta de Expedição")
    pv = st.text_input("PV:")
    n_etiquetas = st.text_input("Nº de Etiquetas")
    qtd = st.text_input("Quantidade de peças:")
    printer = st.radio("Impressora:", ['Impressora Expedição', 'Impressora Galpão'])
    submitted = st.form_submit_button("Buscar")

    if submitted:
        if not pv:
            st.warning("Insira um PV")
        if not qtd:
            st.warning("Insira a Quantidade de Peças")
        if not n_etiquetas:
            n_etiquetas = 1

        try:
            response = requests.post(f"{api_url}/consulta/expedicao", json='pv')
            if response:
                pass
        except Exception as e:
            st.error("Código de PV Inválido")

    

if st.button("Voltar", key="key1", use_container_width=False):
    st.switch_page("interface.py")        

