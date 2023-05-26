
from langchain.agents.agent_toolkits import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.agents import AgentExecutor
from constants import DEFAULT_VEHICLE_ENTRY_TABLE_DESCRP
import gradio as gr
from langchain.agents import AgentType
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.tools.python.tool import PythonREPLTool


db = SQLDatabase.from_uri("sqlite:////home/lohith/chatbot/test.db",include_tables=["vehicle_entries"],custom_table_info={"vehicle_entries":DEFAULT_VEHICLE_ENTRY_TABLE_DESCRP})
llm = OpenAI(temperature=0)
sql_toolkit = SQLDatabaseToolkit(db=db, llm=llm)
python_toolkit = PythonREPLTool()
memory = ConversationBufferMemory(memory_key="chat_history")
agent_executor = create_sql_agent(llm, toolkit=sql_toolkit, verbose=True,agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,memory=memory)



# while (True):
#     query = input(">>")
#     response = agent_executor.run(query)
#     print(response)

