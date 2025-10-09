import streamlit as st

st.set_page_config(page_title="Etiquetas", page_icon="🏭", layout="centered")

st.markdown("""
<style>
/* Box central */
.block-container {
  background: #282B2E;
  border: 1px solid #2b2d30;
  border-radius: 16px;
  box-shadow: 0 12px 40px rgba(0,0,0,.45);
  padding: 48px 56px;
  max-width: 720px;
  margin-top: 60px;
  text-align: center;
}

/* ======== Titulo e subtitulo  ======== */
h1 {
  text-align: center !important;
  font-size: 2.4rem !important;
  font-weight: 1200 !important;
  color: #ffffff !important;
  margin-bottom: 10px;
}

p {
  text-align: center !important;
  font-size: 1.2rem !important;
  color: #d0d0d0 !important;
}

/* ======== BOTÕES ======== */
div.stButton > button {
  background-color: #2c2f33;
  color: #fff;
  border-radius: 8px;
  height: 4em;
  font-weight: 600;
  border: 1px solid #2b2d30;
  transition: 0.2s;
}
div.stButton > button > div > p {
  font-size: 26px !important;
  font-weight: bold;
}
div.stButton > button:hover {
  background-color: #4c8bf5;
  transform: scale(1.02);
}
</style>
""", unsafe_allow_html=True)

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
