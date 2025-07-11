import streamlit as st
from typing import Literal
from dataclasses import dataclass


@dataclass
class Message():
    id: Literal['ai', 'user']
    msg: str

def show_message(msg: Message):
    if msg.id == 'user':
        _, col = st.columns([0.4, 0.6])

        with col.chat_message('user'):
            st.write(msg.msg)

    elif msg.id == 'ai':
        col, _ = st.columns([0.6, 0.4])

        with col.chat_message('ai'):
            st.write(msg.msg)