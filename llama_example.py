from llama_index.indices.struct_store import SQLContextContainerBuilder
from sqlalchemy import create_engine, MetaData
from llama_index.indices.struct_store import  GPTSQLStructStoreIndex
from constants import DEFAULT_VEHICLE_ENTRY_TABLE_DESCRP
engine = create_engine("sqlite:////home/lohith/chatbot/test.db")
metadata_obj = MetaData(bind=engine)
from llama_index import SQLDatabase

sql_database = SQLDatabase(engine, include_tables=["vehicle_entries"])

city_stats_text = (
    "This table gives information regarding the population, country and when the it was established of a given city.\n"
    "The user will query with codewords, where 'foo' corresponds to population and 'bar'"
    "corresponds to city."
)



table_context_dict={"vehicle_entries": DEFAULT_VEHICLE_ENTRY_TABLE_DESCRP}
context_builder = SQLContextContainerBuilder(sql_database, context_dict=table_context_dict)
context_container = context_builder.build_context_container()

# building the index
index = GPTSQLStructStoreIndex.from_documents(
    [], 
    sql_database=sql_database, 
    table_name="city_stats",
    sql_context_container = context_container
)

query_engine = index.as_query_engine()
while True:
    query = input(">>")
    response = query_engine.query(query)
    print(response.extra_info["sql_query"])
    print(response)