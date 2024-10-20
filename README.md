# Chat With Your MySQL Database

This prototype creates a Streamlit Chatbot that you can use to Chat in natural language with the data from your MySql database and receive a natural language answer.

## How does it Work

After connecting to OpenAi and your Database Instance, the interface captures user input and then passes it to Langchain wich runs a SQL Chain that will turn the Input into a SQL QUERY with the help of "gpt-3.5-turbo".

Then it runs the query against the Database, the answer is captured and passed to a Conversation Chain that translates the tables into natural language information providing the output to the user.

This way you can query your database through conversation and make inferences and discover information about your data without the need of writing any query yourself.

# Installing Requirments 

- Python3 Installed
- Open Ai Api Key 
- A MySql Database Instance

Install Dependencies
```
# Create a new Virtual Environment
python -m venv venv

# Activate Environment
.\venv\Scripts\activate  

# Install Requirements
pip install -r requirements.txt
```
# Using it

Run the app:
```

streamlit run src/app.py

```

Set Variables: 
Insert your OPENAI API KEY in the proper input and then a MySQL connection uri with the format: 
```
mysql+mysqlconnector://<MYSQL_USER>:<MYSQL_USER_PASSWORD>@<DATABASE_IP>:<DATABASE_PORT>/<MYSQL_DATABASE_NAME>
```
Ex: mysql+mysqlconnector://root:mypass@localhost:3306/nicedb

Start Chatting with your DATA!

# Considerations

This is just a prototype for study purpose, theres much tuning and handling to do to perfect it. And it can be much more useful if tweaked for especific user cases.

*Feel free to reach me for any sugestions* 

*The prompts and messages are in Brazillian Portuguese*

*Thank you*
