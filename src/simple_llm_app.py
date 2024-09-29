from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

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

system_template = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

result = prompt_template.invoke({"language": "italian", "text": "hi"})

result.to_messages()

chain = prompt_template | model | parser

chain.invoke({"language": "italian", "text": "hi"})
chain.invoke({"language": "spanish", "text": "Im so hungry I could eat a horse!"})
