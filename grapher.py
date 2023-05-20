"""Toolkit for interacting with a SQL database."""
from typing import List

from pydantic import Field

from langchain.agents.agent_toolkits.base import BaseToolkit
from langchain.base_language import BaseLanguageModel
from langchain.sql_database import SQLDatabase
from langchain.tools import BaseTool
from langchain.tools.sql_database.tool import (
    InfoSQLDatabaseTool,
    ListSQLDatabaseTool,
    QueryCheckerTool,
    QuerySQLDataBaseTool,
)

from langchain.tools import BaseTool
from math import pi
from typing import Union
import matplotlib.pyplot as plt
import re
import numpy as np

class GraperTool(BaseTool):
    name = "Graph calculator"
    description = "This tool can be used when you need to draw graphs and charts based on the data"

    def _run(self, data: list):
        data  = re.findall(r"\w+",data)
        x = []
        y = []
        for i in range(len(data)):
            if i%2==0:
                x.append(data[i])
            else:
                y.append(data[i])
        a = np.arange(len(x))
        plt.xticks(a,x)
        plt.plot(a,y)
        plt.show()
        return "done"

    def _arun(self, radius: int):
        raise NotImplementedError("This tool does not support async")
    


class SQLDatabaseToolkit(BaseToolkit):
    """Toolkit for interacting with SQL databases."""

    db: SQLDatabase = Field(exclude=True)
    llm: BaseLanguageModel = Field(exclude=True)

    @property
    def dialect(self) -> str:
        """Return string representation of dialect to use."""
        return self.db.dialect

    class Config:
        """Configuration for this pydantic object."""

        arbitrary_types_allowed = True

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        return [
            QuerySQLDataBaseTool(db=self.db),
            InfoSQLDatabaseTool(db=self.db),
            ListSQLDatabaseTool(db=self.db),
            QueryCheckerTool(db=self.db, llm=self.llm),
            GraperTool()
        ]
