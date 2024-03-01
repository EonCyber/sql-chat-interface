SQL_CHAIN_TEMPLATE = """
Com base no esquema da tabela abaixo, escreva uma consulta SQL que responda à pergunta do usuário:
Table Schema: {schema}

Question: {question}
SQL Query:
"""

NAT_RESPONSE_TEMPLATE = """"
Com base no esquema da tabela abaixo, na Question, na SQL Query e SQL Response, escreva uma resposta em linguagem natural
Table Schema: {schema}

Question: {question}
SQL Query: {query}
SQL Response: {response}
Answer:
"""