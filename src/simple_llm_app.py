from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

model = ChatOllama(
    model="llama3.2:3b-instruct-q8_0",
    base_url="http://a03a-216-147-123-78.ngrok-free.app",
    temperature=0.2,
    num_ctx=16384,
)

messages = [
    SystemMessage(content="Translate the following from English to Italian"),
    HumanMessage(content="Hello, welcome to the new world!"),
]

model.invoke(messages)
