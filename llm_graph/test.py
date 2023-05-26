from langchain.callbacks.stdout import StdOutCallbackHandler
from langchain.chat_models.openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from test_sql import MyCustomChain
from prompt import PROMPT



chain = MyCustomChain(
    prompt=PROMPT,
    llm=ChatOpenAI()
)

chain.run({'question': 'graph it'}, callbacks=[StdOutCallbackHandler()])