import os
import openai
from dotenv import load_dotenv, find_dotenv
from langchain_openai import OpenAI

load_dotenv(find_dotenv())

api_key = os.getenv("OPEN_AI_API_KEY")

llm_model = "gpt-3.5-turbo-0125"

llm = OpenAI(
    api_key=api_key,
    temperature=0.7
)

print(llm.invoke("What is the capital of France?"))