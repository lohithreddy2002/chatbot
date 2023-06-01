# agent.py
from langchain import OpenAI
from langchain.agents import create_pandas_dataframe_agent
import pandas as pd
# from lang_original import agent_executor
# Setting up the api key
import os

from lang_original import agent_executor


def create_agent():
    """
    Create an agent that can access and use a large language model (LLM).

    Args:
        filename: The path to the CSV file that contains the data.

    Returns:
        An agent that can access and use the LLM.
    """

    # Create an OpenAI object.


    # Read the CSV file into a Pandas DataFrame.


    # Create a Pandas DataFrame agent.
    return agent_executor


def query_agent(agent, query):
    """
    Query an agent and return the response as a string.

    Args:
        agent: The agent to query.
        query: The query to ask the agent.

    Returns:
        The response from the agent as a string.
    """

    prompt = (
        """
            For the following query, if it requires drawing a table, reply as follows:
            {"table": {"columns": ["column1", "column2", ...], "data": [[column1 value, column1 value, ...], [column2 value,column2 value, ...], ...]}}

            If the query requires creating a bar chart, reply as follows:
            {"bar": {"columns": ["A", "B", "C", ...], "data": [[column1 value, column1 value, ...], [column2 value,column2 value, ...], ...]}}
            Example:
            {"bar": {"columns": ["number plate", "time spent"], "data": [["AP03AB8638","KA03WE2345"],[25, 24]]}}


            If the query requires creating a line chart, reply as follows:
            {"line": {"columns": ["A", "B", "C", ...],  "data": [[12,12,12,12],[25, 24, 10, ...]}}

            There can only be two types of chart, "bar" and "line".

            If it is just asking a question that requires neither, reply as follows:
            {"answer": "answer"}
            Example:
            {"answer": "The car with the highest time spent is 'AP03AB8638'"}

            If you do not know the answer, reply as follows:
            {"answer": "I do not know."}

            Return all output as a string.

            All strings in "columns" list and data list, should be in double quotes,

            For example: {"columns": ["number plate", "time spent"], "data": [["AP03AB8638", 361], ["KA03WE2345", 5164]]}

            Lets think step by step.

            Below is the query.
            Query: 
            """
        + query
    )

    # Run the prompt through the agent.
    response = agent.run(prompt)

    # Convert the response to a string.
    return response.__str__()

import streamlit as st
import pandas as pd
import json


def decode_response(response: str) -> dict:
    """This function converts the string response from the model to a dictionary object.

    Args:
        response (str): response from the model

    Returns:
        dict: dictionary with response data
    """
    print(response)
    return json.loads(response)

def write_response(response_dict: dict):
    """
    Write a response from an agent to a Streamlit app.

    Args:
        response_dict: The response from the agent.

    Returns:
        None.
    """

    # Check if the response is an answer.
    if "answer" in response_dict:
        st.write(response_dict["answer"])

    # Check if the response is a bar chart.
    if "bar" in response_dict:
        data = response_dict["bar"]
        x = []
        y = []
        for i in data["data"]:
            x.append(i[0])
            y.append(i[1])
        conv_data = {
            data["columns"][0]:x,
            data["columns"][1]:y
        }
        df = pd.DataFrame(conv_data)
        # df.set_index("columns", inplace=True)
        st.bar_chart(df,x=data["columns"][0],y=data["columns"][1])

    # Check if the response is a line chart.
    if "line" in response_dict:
        data = response_dict["line"]
        x = []
        y = []
        for i in data["data"]:
            x.append(i[0])
            y.append(i[1])
        conv_data = {
            data["columns"][0]:x,
            data["columns"][1]:y
        }
        df = pd.DataFrame(conv_data)
        st.line_chart(df,x=data["columns"][0],y=data["columns"][1])

    # Check if the response is a table.
    if "table" in response_dict:
        data = response_dict["table"]
        df = pd.DataFrame(data["data"], columns=data["columns"])
        st.table(df)

st.title("👨‍💻 Chat with your CSV")

st.write("Please upload your CSV file below.")



query = st.text_area("Insert your query")

if st.button("Submit Query", type="primary"):
    # Create an agent from the CSV file.
    agent = create_agent()

    # Query the agent.
    response = query_agent(agent=agent, query=query)

    # Decode the response.
    decoded_response = decode_response(response)

    # Write the response to the Streamlit app.
    write_response(decoded_response)
