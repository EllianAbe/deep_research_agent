import streamlit as st
from llm.agent import create_executor, invoke_agent
from util import show_message, Message
import copy

st.session_state.setdefault('history', [])
MEMORY : list[Message] = st.session_state.history

with st.sidebar:
    model = st.selectbox('model', ["gpt-4o-mini", "gpt-4o", "gpt-4.1-mini"])
    new_key = st.text_input('OpenAI Key')

    if st.button('🔒 update'):
        st.session_state['model'] = model
        st.session_state['key'] = new_key

        st.session_state['agent_executor'] = create_executor(st.session_state.model, 
                                                             st.session_state.key)
        
for msg in MEMORY:
    show_message(msg)


if prompt := st.chat_input('Deep Research Subject Here'):
    executor = st.session_state.get('agent_executor')

    user_msg = Message('user', prompt)
    show_message(user_msg)

    answer = invoke_agent(executor, prompt)
    ai_message = Message('ai', answer)

    show_message(ai_message)

    MEMORY.append(user_msg)
    MEMORY.append(ai_message)

    
