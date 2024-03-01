from langchain_core.prompts import ChatPromptTemplate
from langchain_community.utilities import SQLDatabase
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
import llm_templates

class SQLAi:
    def __init__(self):
        self.llm = None
        self.db = None
        self.sql_prompt = ChatPromptTemplate.from_template(llm_templates.SQL_CHAIN_TEMPLATE)
        self.nat_prompt = ChatPromptTemplate.from_template(llm_templates.NAT_RESPONSE_TEMPLATE)
        
    def connect(self, api_key, db_uri):
        if api_key is None:
            raise Exception("Desculpe, API_KEY inválida.")
        if db_uri is None:
            raise Exception("Desculpe, DB_URI inválida.")
        try:
            self.llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0, api_key=api_key)
            self.db = SQLDatabase.from_uri(db_uri)
        except Exception as e:
            raise Exception("Erro: ", e)
        finally:
            print("[+] AI API & DB Connected")
        
    def sql_chain(self, runnable, prompt, llm):
        return ( # This chain turns the user input into SQL Query
            RunnablePassthrough.assign(schema=runnable) | prompt | llm.bind(stop="\nSQL Query:") | StrOutputParser()
        )
        
    def full_chain(self, sql_chain, runnable, prompt, llm):
        return ( # This chain runs the sql_chain and the result is passed to the llm to generate natural response
            RunnablePassthrough.assign(query=sql_chain).assign(schema=runnable, response= lambda variables: runnable(variables)) | prompt | llm
        )
        
    def fetch_llm_response(self, user_query):
        # Lambda used as a runnable to fetch the DB Schema Information
        fetch_schema = lambda _: self.db.get_table_info() 
        # Instance of the SQL Chain
        sql_chain = self.sql_chain(fetch_schema, self.sql_prompt, self.llm)
        # Lambda used as runnable to run the SQL Query against the Database
        run_sql_query_on_db = lambda query_obj: self.db.run(query_obj["query"])
        # full_chain instance to be invoked for input questions                                                       
        full_chain = self.full_chain(sql_chain, run_sql_query_on_db, self.nat_prompt, self.llm)
        
        return full_chain.invoke({"question": user_query})