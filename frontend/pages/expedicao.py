import streamlit as st
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
