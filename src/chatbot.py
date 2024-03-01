import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
import llm

class StreamlitApp:
    def __init__(self):
        self.title = "Converse com Dados"
        self.side_header = "Variáveis:"
        self.api_key = ''
        self.db_uri = ''
        
    def run(self):
        st.set_page_config(page_title=self.title, page_icon=":)")
        st.title(self.title)
        self.build_sidebar()
        self.create_chat_state()
        self.run_connections()
        self.run_chat()

    def build_sidebar(self):
        with st.sidebar:
            st.header(self.side_header)  
            self.api_key = st.text_input("Open Api Key:")
            self.db_uri = st.text_input("MySql Uri:")  
    def check_keys(self):
        return (self.api_key is None or self.api_key == '') or (self.db_uri is None or self.db_uri == '')     
    
    def create_chat_state(self):
         if "chat_history" not in st.session_state:
            st.session_state.chat_history = [
                AIMessage(content="Olá, pergunte algo para o seus dados, vou tentar meu melhor para transformar em informação!")
            ]
            
    def run_connections(self):
        if self.check_keys(): 
            st.info("Por favor, insira as variáveis!")
        elif "ai" not in st.session_state:
            st.session_state.ai = llm.SQLAi()
            st.session_state.ai.connect(self.api_key, self.db_uri)   
                         
    def run_chat(self):
        if self.check_keys() == False and "ai" in st.session_state:
            user_query = st.chat_input("Insira sua pergunta...")
            # User Input Handler
            if user_query is not None and user_query != "":
                st.session_state.chat_history.append(HumanMessage(content=user_query))
                response = st.session_state.ai.fetch_llm_response(user_query)
                st.session_state.chat_history.append(AIMessage(content=response.content))
            # Conversation Display Handler
            for message in st.session_state.chat_history:
                if isinstance(message, AIMessage):
                    with st.chat_message("AI"):
                        st.write(message.content)
                elif isinstance(message, HumanMessage):
                    with st.chat_message("Human"):
                        st.write(message.content)