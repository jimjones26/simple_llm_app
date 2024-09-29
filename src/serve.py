from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langserve import add_routes

# ------------------------------------------------------------------
# Create prompt template
# ------------------------------------------------------------------
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

# ------------------------------------------------------------------
# Create model
# ------------------------------------------------------------------
model = ChatOllama(
    model="llama3.2:3b-instruct-q8_0",
    base_url="http://a03a-216-147-123-78.ngrok-free.app",
    temperature=0.2,
    num_ctx=16384,
)

# ------------------------------------------------------------------
# Create parser
# ------------------------------------------------------------------
parser = StrOutputParser()

# ------------------------------------------------------------------
# Create chain
# ------------------------------------------------------------------
chain = prompt_template | model | parser

# ------------------------------------------------------------------
# App definition
# ------------------------------------------------------------------
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces",
)

# ------------------------------------------------------------------
# Add chain route
# ------------------------------------------------------------------
add_routes(app, chain, path="/chain")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
