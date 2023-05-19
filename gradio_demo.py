from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
# from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.agents import AgentExecutor
from constants import DEFAULT_VEHICLE_ENTRY_TABLE_DESCRP
import gradio as gr
import os
from llama_index import SQLDatabase
from lang_llama import initialize_chain,initialize_index

from llama_index.indices.struct_store import SQLContextContainerBuilder
from sqlalchemy import create_engine
from llama_index.indices.struct_store import  GPTSQLStructStoreIndex
from constants import DEFAULT_VEHICLE_ENTRY_TABLE_DESCRP


def lang():
    db = SQLDatabase.from_uri("sqlite:////home/lohith/chatbot/test.db",include_tables=["vehicle_entries"],custom_table_info={"vehicle_entries":DEFAULT_VEHICLE_ENTRY_TABLE_DESCRP})
    llm = OpenAI(temperature=0)
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    memory = ConversationBufferMemory(memory_key="chat_history")
    agent_executor = create_sql_agent(llm, toolkit=toolkit, verbose=True,memory=memory)
    return agent_executor


def lang_llama():
    llm_name = "text-davinci-003"
    model_temperature = 0
    use_table_descrp = True
    lc_descrp = "this tool is used to run sql queries over data and get the output. reformat the output in a human readable form without any mention of the actual sql query"
    api_key = os.environ.get("OPENAI_API_KEY")


    table_context_dict = {"vehicle_entries": DEFAULT_VEHICLE_ENTRY_TABLE_DESCRP}


    llama_index = initialize_index(
        llm_name,
        model_temperature,
        table_context_dict if use_table_descrp else None,
        api_key,
    )
    agent = initialize_chain(llm_name, model_temperature, lc_descrp, api_key, llama_index)

    return agent

def llama():
    engine = create_engine("sqlite:////home/lohith/chatbot/test.db")
    sql_database = SQLDatabase(engine, include_tables=["vehicle_entries"])
    table_context_dict={"vehicle_entries": DEFAULT_VEHICLE_ENTRY_TABLE_DESCRP}
    context_builder = SQLContextContainerBuilder(sql_database, context_dict=table_context_dict)
    context_container = context_builder.build_context_container()

    # building the index
    index = GPTSQLStructStoreIndex.from_documents(
        [], 
        sql_database=sql_database, 
        table_name="vehicle_entries",
        sql_context_container = context_container
    )

    query_engine = index.as_query_engine()

    return query_engine



with gr.Blocks() as demo:
    lang_llama_agent = lang_llama()
    lang_agent = lang()
    llama_agent = llama()
    dropdown = gr.Dropdown(["lang_lama", "lang", "llama"], label="LLM Model")
    chatbot = gr.Chatbot([], label="AllGoBot",elem_id="chatbot").style(height=400)
    with gr.Row():
        with gr.Column(scale=0.85):
            msg = gr.Textbox(
                show_label=False,
                placeholder="Enter text and press enter, or upload an image",
            ).style(container=False)
        with gr.Column(scale=0.15, min_width=0):
            clear = gr.Button("Clear")
    def clear_bot():
        chatbot.value = []
        return []
    dropdown.change(clear_bot)

    def respond(message,dropdown, chat_history):
        if dropdown == "lang_lama":
            response= lang_llama_agent.run(message)
            chat_history.append((message, response))
        elif dropdown == "llama":
            response = llama_agent.query(message)
            chat_history.append((message, str(response)))
        elif dropdown == "lang":
            response = lang_agent.run(message)
            chat_history.append((message, response))
        else:
            pass
        return "",chat_history
    dropdown.change(lambda:None,None,chatbot)
    msg.submit(respond, [msg,dropdown,chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, dropdown, queue=False)

if __name__ == "__main__":
    demo.launch()