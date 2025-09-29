from typing import List
from model import item
from database import itemDAO
import streamlit as st

class itemController:
    dao = itemDAO()
    
    @staticmethod
    @st.cache_data #
    def get_all_itens() -> List[item]:
        return itemController.dao.fetch_all_itens()
    @staticmethod
    def add_new_item(descricao: str, quantidade: int):
        new_item = item(0,descricao=descricao, quantidade=quantidade)
        itemController.dao.add_item(new_item)
        st.cache_data.clear()