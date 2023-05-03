from sqlalchemy import create_engine, MetaData
from llama_index import  SQLDatabase, SimpleDirectoryReader, WikipediaReader, Document
from llama_index.indices.struct_store import SQLContextContainerBuilder,GPTSQLStructStoreIndex


engine = create_engine("sqlite:////home/lohith/chatbot/test.db")
metadata_obj = MetaData(bind=engine)
sql_database = SQLDatabase(engine, include_tables=["vehicles","entries"])
entries_table_text = (
    "This table gives information regarding the vehicles which entred the parking lot.\n"
    "This table stores the entry time, exit time, entry gate and exit gate."
)
table_context_dict={"entries": entries_table_text}
context_builder = SQLContextContainerBuilder(sql_database,table_context_dict)
context_container = context_builder.build_context_container()
index = GPTSQLStructStoreIndex.from_documents(
    [],
    sql_database=sql_database, 
    table_name=["vehicles","entries"],
    sql_context_container=context_container
)
query_engine = index
# while True:
    query = input()
    response = query_engine.query(query,q)
    print(response.extra_info["sql_query"])
    print(response)
