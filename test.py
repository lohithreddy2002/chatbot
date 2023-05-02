from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, select, column 

engine = create_engine("sqlite:////home/lohith/chatbot/test.db")
metadata_obj = MetaData(bind=engine)

table_name = "city_stats"
city_stats_table = Table(
    table_name,
    metadata_obj,
    Column("city_name", String(16), primary_key=True),
    Column("population", Integer),
    Column("country", String(16), nullable=False),
)
metadata_obj.create_all()
from llama_index import GPTSQLStructStoreIndex, SQLDatabase
from sqlalchemy import insert
rows = [
    {"city_name": "Toronto", "population": 2731571, "country": "Canada"},
    {"city_name": "Tokyo", "population": 13929286, "country": "Japan"},
    {"city_name": "Berlin", "population": 600000, "country": "Germany"},
]
# for row in rows:
#     stmt = insert(city_stats_table).values(**row)
#     with engine.connect() as connection:
#         cursor = connection.execute(stmt)

from llama_index import SQLDatabase

sql_database = SQLDatabase(engine, include_tables=["city_stats"])

index = GPTSQLStructStoreIndex(
    [],
    sql_database=sql_database, 
    table_name="city_stats",
)

query_engine = index.as_query_engine()
response = query_engine.query("Which city has the highest population?")
print(response)

