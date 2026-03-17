from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from tools import tools

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatOpenAI(model="gpt-3.5-turbo")

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a research assistant. Use tools when needed.",
    response_format=ResearchResponse,
)

query = input("What can I help you research? ")
raw_response = agent.invoke(
    {"messages": [{"role": "user", "content": query}]}
)

print(raw_response["structured_response"])