
import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv(usecwd=True))


ollama_model = LiteLlm(model="ollama_chat/deepseek-r1:latest")




root_agent = Agent(
    
    name = "greet_agent",
    model = ollama_model,
    description="Greeting agent",
    instruction = """
    You are helpful assisstant that greets the user.
    and you help user by guiding as coach whatever he feels hard to do
    """,
)

