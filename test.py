from sqlalchemy import create_engine, MetaData
from llama_index import SQLDatabase, SimpleDirectoryReader, WikipediaReader, Document
from llama_index.indices.struct_store import (
    SQLContextContainerBuilder,
    GPTSQLStructStoreIndex,
)
from constants import DEFAULT_VEHICLE_ENTRY_TABLE_DESCRP
from llama_index.logger import LlamaLogger
from llama_index import ServiceContext


engine = create_engine("sqlite:////home/lohith/chatbot/test.db")
metadata_obj = MetaData(bind=engine)
sql_database = SQLDatabase(engine, include_tables=["vehicle_entries"])
table_context_dict = {"vehicle_entries": DEFAULT_VEHICLE_ENTRY_TABLE_DESCRP}
context_builder = SQLContextContainerBuilder(sql_database, table_context_dict)
context_container = context_builder.build_context_container()
llama_logger = LlamaLogger()
service_context = ServiceContext.from_defaults(llama_logger=llama_logger)
index = GPTSQLStructStoreIndex.from_documents(
    [],
    sql_database=sql_database,
    table_name=["vehicle_entries"],
    sql_context_container=context_container,
    service_context=service_context
)
query_engine = index
while True:
    query = input(">>")
    response = query_engine.query(query)
    sql = response.extra_info["sql_query"]
    print("\033[1;31m [DEBUG] ",sql+" \033[00m")
    print(response)

