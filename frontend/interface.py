import streamlit as st

st.set_page_config(page_title="Etiquetas", page_icon="🏭", layout="centered")

def load_css():
  with open("style/style.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
load_css()  
st.title("Impressão de Etiquetas")
st.write("Escolha o tipo de etiqueta que deseja imprimir:")

if st.button("🚚 Transporte", use_container_width=True):
    st.switch_page("pages/transporte.py")

st.write("")
if st.button("📦 Expedição", use_container_width=True):
    st.switch_page("pages/expedicao.py")

st.write("")
if st.button("🏷️ Estoque", use_container_width=True):
    st.switch_page("pages/estoque.py")

st.write("")
if st.button("DEXCO", use_container_width=True):
    st.switch_page("pages/dexco.py")

st.write("")
st.write("")
st.caption("Versão de testes ainda")
st.write("")
