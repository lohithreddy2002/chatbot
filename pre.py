# import json

# file = open("data.txt", "r")

# data = file.readlines()

# for i in data:
#     d = json.loads(i)
#     print(
#         '("%s","%s",%d,%d,%d)'
#         % (d["entry_time"], d["exit_time"], 0, d["entry_gate"], d["exit_gate"])
#     )

import matplotlib.pyplot as plt
import re
# data = [('KA19EQ1316', 12567004), ('MP15NC9738', 418282), ('HR26DQ5551', 282252), ('TN37EF4902', 96282), ('UP67AA3601', -26780)]"
# data = re.findall(r"\w+",data)
 
import pandas as pd
from pandasai import PandasAI

df = pd.read_csv("data.csv")

from pandasai.llm.openai import OpenAI
llm = OpenAI(api_token="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")

pandas_ai = PandasAI(llm, conversational=False)
pandas_ai.run(df, prompt='get the cars which entered yesterday')