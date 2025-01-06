# -*- coding:utf-8 -*-
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
import time, os, re
import api_key as api
import common_tools as common_tools
import requests

api_key = api.ai302_api_key()
base_url= 'https://api.302.ai/v1'
model_name='gemini-2.0-flash-exp'

@tool
def get_exchange_rate_from_api(currency_from: str, currency_to: str) -> str:
    """
    Return the exchange rate between currencies
    Args:
        currency_from: str
        currency_to: str
    """
    url = f"https://api.frankfurter.app/latest?from={currency_from}&to={currency_to}"
    api_response = requests.get(url)
    return api_response.text

langchain_tools = [
    get_exchange_rate_from_api
]

model = ChatOpenAI(
    base_url=base_url,
    api_key=api_key,
    model_name=model_name
)
output_parser = StrOutputParser()
chain = model | output_parser

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        ("human", "{input}"),
        # Placeholders fill up a **list** of messages
        ("placeholder", "{agent_scratchpad}"),
    ]
)

def test():
    # output = chain.invoke("What is the current exchange rate for USD vs EUR ?")
    # output = get_exchange_rate_from_api({'currency_from': 'USD', 'currency_to': 'EUR'})
    agent = create_tool_calling_agent(model, langchain_tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=langchain_tools)
    output = agent_executor.invoke({
        "input": "What is the current exchange rate for USD vs EUR ?"
    })
    print(output)

if __name__ == '__main__':
    start_time = time.time()
    print('waiting...\n')
    test()
    end_time = time.time()
    print('Time Used: ' + str((end_time - start_time)/60) + 'min')