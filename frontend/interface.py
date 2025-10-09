import streamlit as st

API_URL = "http://192.168.1.90:7000"

st.set_page_config(
    page_title="Etiquetas",
    page_icon="🏭",
    layout="centered"
)

st.markdown("""
<style>
div.stButton > button {
    background-color: #2c2f33;
    color: white;
    border-radius: 8px;
    height: 3em;
    font-weight: 600;
    border: 1px solid #2b2d30;
    transition: 0.2s;
}
div.stButton > button:hover {
    background-color: #5b96ff;
    transform: scale(1.02);
}
</style>
""", unsafe_allow_html = True)

st.title("Impressão de etiquetas!")
st.markdown('### Selecione abaixo o tipo de etiqueta que deseja gerar:')
st.write("---")

if st.button("🚚 Transporte", use_container_width=True):  # use_container_width eh pra ocupar o botao inteiro
        st.switch_page("pages/transporte.py")
st.markdown("")
if st.button("📦 Expedição", use_container_width=True):  # use_container_width eh pra ocupar o botao inteiro
        st.switch_page("pages/expedicao.py")
st.markdown("")

if st.button("🏷️ Estoque", use_container_width=True):  # use_container_width eh pra ocupar o botao inteiro
    st.switch_page("pages/estoque.py")
