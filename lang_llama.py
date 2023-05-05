import os

from sqlalchemy import create_engine

from langchain.agents import Tool, initialize_agent
from langchain.chains.conversation.memory import ConversationBufferMemory

from llama_index import GPTSQLStructStoreIndex, LLMPredictor, ServiceContext
from llama_index import SQLDatabase as llama_SQLDatabase
from llama_index.indices.struct_store import SQLContextContainerBuilder
import os

from constants import (
    DEFAULT_SQL_PATH,
    DEFAULT_ENTRY_TABLE_DESCRP,
    DEFAULT_VEHICLES_TABLE_DESCRP,
    DEFAULT_VEHICLE_ENTRY_TABLE_DESCRP,
)
import os
from langchain import OpenAI
from langchain.chat_models import ChatOpenAI


def get_sql_index_tool(sql_index, table_context_dict):
    table_context_str = "\n".join(table_context_dict.values())

    def run_sql_index_query(query_text):
        try:
            response = sql_index.query(query_text)
        except Exception as e:
            return f"Error running SQL {e}.\nNot able to retrieve answer."
        text = str(response)
        print(response.extra_info)
        sql = response.extra_info["sql_query"]
        # return f"Here are the details on the SQL table: {table_context_str}\nSQL Query Used: {sql}\nSQL Result: {text}\n"
        return f"SQL Query Used: {sql}\nSQL Result: {text}\n"
        # return text

    return run_sql_index_query


def get_llm(llm_name, model_temperature, api_key):
    os.environ["OPENAI_API_KEY"] = api_key
    if llm_name == "text-davinci-003":
        return OpenAI(temperature=model_temperature, model_name=llm_name)
    else:
        return ChatOpenAI(temperature=model_temperature, model_name=llm_name)


def initialize_index(
    llm_name, model_temperature, table_context_dict, api_key, sql_path=DEFAULT_SQL_PATH
):
    """Create the GPTSQLStructStoreIndex object."""
    llm = get_llm(llm_name, model_temperature, api_key)

    engine = create_engine(sql_path)
    sql_database = llama_SQLDatabase(engine, include_tables=["vehicle_entries"])

    context_container = None
    if table_context_dict is not None:
        context_builder = SQLContextContainerBuilder(
            sql_database, context_dict=table_context_dict
        )
        context_container = context_builder.build_context_container()

    service_context = ServiceContext.from_defaults(llm_predictor=LLMPredictor(llm=llm))
    index = GPTSQLStructStoreIndex(
        [],
        sql_database=sql_database,
        sql_context_container=context_container,
        service_context=service_context,
    )

    return index


def initialize_chain(llm_name, model_temperature, lc_descrp, api_key, _sql_index):
    """Create a (rather hacky) custom agent and sql_index tool."""
    sql_tool = Tool(
        name="SQL Index",
        func=get_sql_index_tool(
            _sql_index, _sql_index.sql_context_container.context_dict
        ),
        description=lc_descrp,
    )

    llm = get_llm(llm_name, model_temperature, api_key=api_key)

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # agent_chain = initialize_agent([sql_tool], llm, agent="chat-conversational-react-description", verbose=True, memory=memory)
    agent_chain = initialize_agent([sql_tool], llm, verbose=True, memory=memory)

    return agent_chain


llm_name = "text-davinci-003"
model_temperature = 0
use_table_descrp = True
lc_descrp = ""
api_key = os.environ.get("OPENAI_API_KEY")


table_context_dict = {"vehicle_entries": DEFAULT_VEHICLE_ENTRY_TABLE_DESCRP}


llama_index = initialize_index(
    llm_name,
    model_temperature,
    table_context_dict if use_table_descrp else None,
    api_key,
)
agent = initialize_chain(llm_name, model_temperature, lc_descrp, api_key, llama_index)

while True:
    query = input(">>")
    response = agent.run(input=query)
    # print(response)
