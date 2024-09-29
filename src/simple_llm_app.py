from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

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

result = model.invoke(messages)

parser = StrOutputParser()

parser.invoke(result)

chain = model | parser

chain.invoke(messages)
