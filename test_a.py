from langchain.agents import create_pandas_dataframe_agent

import pandas as pd
import os
from pandasai import PandasAI
df = pd.read_csv("test_a.csv")

from pandasai.llm.openai import OpenAI
llm = OpenAI(api_token=os.environ.get("OPENAI_API_KEY"))

pandas_ai = PandasAI(llm, conversational=False)
# response  = pandas_ai(df, prompt='Plot the histogram of companies in Bulgaria showing for each number of employees, using different colors for each bar')
# print(response)
from lang_original import llm
agent = create_pandas_dataframe_agent(llm,df,verbose=True)

# agent.run("Plot the histogram of companies in Bulgaria showing for each number of employees, using different colors for each bar")

df['Number of employees'].hist(color='blue')