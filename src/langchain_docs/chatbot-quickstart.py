from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

chat = ChatOpenAI(
    model="gpt-4o",
    temperature=0.2
)

chat.invoke(
    HumanMessage(
        content="Translate this sentence from English to French: 'Hello, how are you?'"
    )
)