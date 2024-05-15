import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai.chat_models import ChatOpenAI

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

load_dotenv(find_dotenv())

OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")
OPEN_AI_LLM="gpt-4o"


llm = ChatOpenAI(
    api_key=OPEN_AI_API_KEY,
    model=OPEN_AI_LLM,
    temperature=0.6
)

memory = ConversationBufferMemory()
chain = ConversationChain(llm=llm, memory=memory, verbose=True)

chain.invoke(input="Hi I am Andy")
chain.invoke(input="How are you?")
chain.invoke(input="Why is the sky blue?")
chain.invoke(input="What would happen if the Rayleigh scattering was different?")
chain.invoke(input="What is the Rayleigh scattering?")
chain.invoke(input="What is my name?")

print(chain.memory)