import pandas as pd
import streamlit as st
from controler import itemController
st.set_page_config(page_title="Itens MVC", layout="centered")
st.title("Gerenciador de itens")

st.header("Inserir Item")
with st.form(key="new_item_form", clear_on_submit=True):
    desc = st.text_area("Descrição")
    quant = st.text_input("Quantidade")
    submit_button = st.form_submit_button(label="Adicionar")


if submit_button:
    itemController.add_new_item(desc, quant)
    st.rerun()

st.markdown("---")

st.header("itens Recentes")


all_items = itemController.get_all_itens()

if not all_items:
    st.info("Ainda não há itens na lista.")
else:
    data = [{"id":i.get_id(),"descricao": i.get_descricao(), "quantidade": i.get_quantidade()} for i in all_items]
    df = pd.DataFrame(data)
    st.table(df)