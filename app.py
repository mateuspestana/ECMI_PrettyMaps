import streamlit as st
import pandas as pd
import numpy as np
import os
from functions import desenha_mapa

st.set_page_config(page_title="Pretty Mapp", page_icon="📐", layout="centered")


def main():
    with st.form(key="mapa"):
        coluna1, coluna2 = st.columns([2, 1])
        endereco = coluna1.text_input("Digite o endereço")
        estilo = coluna2.selectbox("Escolha o estilo", ["Auburn", "Peach", "Citrus", "Flannel"])
        radius = coluna1.slider("Escolha o raio", 100, 2000, 1000)
        retangular = coluna2.checkbox("Retangular?", value=False)
        botao = st.form_submit_button(label="Criar mapa")

    if botao:
        with st.spinner("Criando mapa..."):
            fig = desenha_mapa(endereco, radius, estilo, retangular)
            st.pyplot(fig)
            st.write("Mapa criado com sucesso!")

if __name__ == '__main__':
    main()
