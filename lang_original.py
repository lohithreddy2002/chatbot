from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import create_python_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.agents import AgentExecutor
from constants import DEFAULT_VEHICLE_ENTRY_TABLE_DESCRP
import gradio as gr
from grapher import SQLDatabaseToolkit
from langchain.tools.python.tool import PythonREPLTool



db = SQLDatabase.from_uri("sqlite:////home/lohith/chatbot/test.db",include_tables=["vehicle_entries"],custom_table_info={"vehicle_entries":DEFAULT_VEHICLE_ENTRY_TABLE_DESCRP})
llm = OpenAI(temperature=0)
sql_toolkit = SQLDatabaseToolkit(db=db, llm=llm)
python_toolkit = PythonREPLTool()

agent_executor = create_sql_agent(llm, toolkit=sql_toolkit, verbose=True)



while (True):
    query = input(">>")
    response = agent_executor.run(query)
    print(response)


# with gr.Blocks() as demo:
#     chatbot = gr.Chatbot(label="AllGoBot")
#     msg = gr.Textbox()
#     clear = gr.Button("Clear")

#     def respond(message, chat_history):
#         bot_message = run(message)
#         chat_history.append((message, bot_message))
#         return "", chat_history
    
#     msg.submit(respond, [msg, chatbot], [msg, chatbot])
#     clear.click(lambda: None, None, chatbot, queue=False)

# if __name__=="__main__":
#     demo.launch()