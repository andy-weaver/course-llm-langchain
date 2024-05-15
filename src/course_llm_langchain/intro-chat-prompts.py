import os
import openai
from dotenv import load_dotenv, find_dotenv
from langchain_openai import OpenAI
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


load_dotenv(find_dotenv())

OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")
OPEN_AI_LLM="gpt-4o"


chat = ChatOpenAI(
    api_key=OPEN_AI_API_KEY,
    model=OPEN_AI_LLM,
    temperature=0.7
)


