from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
from langchain.prompts.prompt import PromptTemplate
from langchain.agents import Tool
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory,ConversationBufferWindowMemory
from langchain import OpenAI
from langchain.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent
from langchain.agents import Tool, AgentExecutor, BaseSingleActionAgent
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
from langchain.chains import SQLDatabaseSequentialChain
from grapher import GraperTool

from constants import DEFAULT_VEHICLE_ENTRY_TABLE_DESCRP
db = SQLDatabase.from_uri("sqlite:////home/lohith/chatbot/test.db",include_tables=["vehicle_entries"])
llm = OpenAI(temperature=0)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

print(len(toolkit.get_tools()))


tools = [
    Tool(
        name = "SQL",
        func=db_chain.run,
        description="this tool is used to run sql queries over data and get the output. reformat the output in a human readable form without any mention of the actual sql query",
    ),
    GraperTool()
]

memory = ConversationBufferMemory(memory_key="chat_history")

agent_chain = initialize_agent(tools, llm, verbose=True)


while True:
    query = input(">>")
    response = agent_chain.run(query)
    print("answer = ",response)
