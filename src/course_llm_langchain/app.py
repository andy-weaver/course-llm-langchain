0  

messages = [
    SystemMessage("You are a helpful assistant. You answer statistical questions, and assume an expert level of sophistication in the user's understanding of statistics. Your goal is to answer the user's questions as concisely as possible, while still providing a complete answer."),
    HumanMessage("What is the difference between L1 and L2 regularization?"),
]

print(chat.invoke(messages).content)