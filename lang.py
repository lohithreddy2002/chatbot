from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor

db = SQLDatabase.from_uri("sqlite:////home/lohith/chatbot/test.db")
llm = OpenAI(temperature=0)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

agent_executor = create_sql_agent(llm, toolkit=toolkit, verbose=True)

while True:
    query = input(">>")
    agent_executor.run(query)
