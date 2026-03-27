from groq import Groq
import streamlit as st
from huggingface_hub import InferenceClient

tab1, tab2 = st.tabs(["GROQ", "Hugging Face"])
with tab1:
    if 'context_tab1' not in st.session_state:
        st.session_state['context_tab1'] = [{"role": "system", "content": "What can I help you with?"}]
    chat_bot = Groq(api_key=st.secrets["api_GROQ"])
    st.header("Chatbot using GROQ")
    for message in st.session_state["context_tab1"]:
        if message["role"] == "system":
            with st.chat_message("ai"):
                st.write(message["content"])
        else:
            with st.chat_message("user"):
                st.write(message["content"])
    space_for_query = st.container()
    query_input = st.container()
    col1, col2 = query_input.columns([12, 1])
    with col1:
        inp = st.empty()
        query = inp.chat_input("Enter query: ", key="tab1")
    with col2:
        but = st.empty()
        if but.button("⛔️", help="Clear chat", key="5"):
            st.session_state['context_tab1'] = [{"role": "system", "content": "What can I help you with?"}]
            st.rerun()
    if query:
        inp.empty()
        but.empty()
        col1, col2 = query_input.columns([12, 1])
        with col1:
            st.chat_input("Enter query: ", key="3", disabled=True)
        with col2:
            st.button("⛔️", key="9")
        with space_for_query.chat_message("user"):
            st.write(query)
        st.session_state['context_tab1'].append({"role": "user", "content": f"{query}"})
        output = chat_bot.chat.completions.create(messages=st.session_state['context_tab1'], model="meta-llama/llama-4-scout-17b-16e-instruct", ).choices[0].message.content
        st.session_state['context_tab1'].append({"role": "system", "content": output})
        with space_for_query.chat_message("ai"):
            st.write(output)
        query_input.empty()
        st.rerun()


with tab2:
    if 'history_tab2' not in st.session_state:
        st.session_state['history_tab2'] = []
    if 'context_tab2' not in st.session_state:
        st.session_state['context_tab2'] = []
    if 'chat_bot' not in st.session_state:
        st.session_state['chat_bot'] = InferenceClient(provider="auto", api_key=st.secrets["api_Hugging_Face"])
    st.header("Chatbot using Hugging Face")

    def refresh():
        st.session_state['history_tab2'] = []
        st.session_state['context_tab2'] = []

    models = ["openai/gpt-oss-120b:fastest", "meta-llama/Llama-4-Maverick-17B-128E-Instruct:fastest",
              "mistralai/Mistral-7B-Instruct-v0.2:featherless-ai", "deepseek-ai/DeepSeek-V3.1",
              "google/DiarizationLM-13b-Fisher-v1:fastest", "Qwen/Qwen3-Coder-480B-A35B-Instruct"]

    model = st.selectbox("Which model to use for Chatbot ?", options=models, index=0, on_change=refresh)

    with st.chat_message("ai"):
        st.write("What can I help you with?")
    for message in st.session_state["history_tab2"]:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    space_for_query = st.container()
    query_input = st.container()
    col1, col2 = query_input.columns([12, 1])
    with col1:
        inp = st.empty()
        query = inp.chat_input("Enter query: ", key="tab2")
    with col2:
        but = st.empty()
        if but.button("⛔️", help="Clear chat", key="4"):
            refresh()
            st.rerun()
    if query:
        inp.empty()
        but.empty()
        col1, col2 = query_input.columns([12, 1])
        with col1:
            st.chat_input("Enter query: ", key="2", disabled=True)
        with col2:
            st.button("⛔️", key="7", disabled=True)
        with space_for_query.chat_message("user"):
            st.write(query)
        st.session_state['history_tab2'].append({"role": "user", "content": f"{query}"})
        st.session_state['context_tab2'].append({"role": "user", "content": f"{query}"})
        with space_for_query:
            with st.spinner("Generating response..."):
                response = st.session_state['chat_bot'].chat.completions.create(model=model, messages=st.session_state['context_tab2']).choices[0].message.content
        st.session_state['history_tab2'].append({"role": "assistant", "content": response})
        st.session_state['context_tab2'].append({"role": "assistant", "content": response})
        with space_for_query.chat_message("ai"):
            st.write(response)
        query_input.empty()
        st.rerun()

