
from math import pi
from typing import Union
from typing import List

from langchain.tools import BaseTool
from math import pi
from typing import Union
import re   
from langchain.agents import Tool

class GraperTool(BaseTool):
    name = "Graph calculator"
    description = "use this tool when you need to calculate a circumference using the radius of a circle"

    def _run(self, radius: Union[int, float]):
        return float(radius)*2.0*pi

    def _arun(self, radius: int):
        raise NotImplementedError("This tool does not support async")
    
