# 📦 Import Required Libraries
import os
from dotenv import load_dotenv, find_dotenv  # 📂 Load environment variables from .env file

from agents import (
    Agent,                           # 🤖 Core agent class
    Runner,                          # 🏃 Runs the agent
    AsyncOpenAI,                     # 🌐 OpenAI-compatible async client
    OpenAIChatCompletionsModel,      # 🧠 Chat model interface
    function_tool,                   # 🛠️ Decorator to turn Python functions into tools
    set_default_openai_client,       # ⚙️ (Optional) Set default OpenAI client
    set_tracing_disabled,            # 🚫 Disable internal tracing/logging
    ModelSettings                    # ⚙️ Model configuration settings (if needed
)
from tavily import TavilyClient  # 🌐 Tavily client for Gemini (if needed for advanced features)

# 🌿 Load environment variables from .env file
load_dotenv(find_dotenv())

# 🚫 Disable tracing for clean output (optional for beginners)
set_tracing_disabled(disabled=True)

# 🔐 1) Environment & Client Setup
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # 🔑 Get your API key from environment
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")  # 🔑 (Optional) Tavily API key if using advanced features
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"  # 🌐 Gemini-compatible base URL (set this in .env file)


# 🌐 Optional: Initialize Tavily client for advanced Gemini features
tavily_client: TavilyClient = TavilyClient(    
    api_key=TAVILY_API_KEY        
    )  
response = tavily_client.search("who is messy?")

# 🌐 Initialize the AsyncOpenAI-compatible client with Gemini details
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=BASE_URL,
)

# 🧠 2) Model Initialization
model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",        # ⚡ Fast Gemini model
    openai_client=external_client
)

# 🛠️ 3) Define tools (functions wrapped for tool calling)
@function_tool
def search(query: str) -> str:
    """🔍 Search tool (use this for general knowledge questions)."""
    print("Tool for searching called with query:", query)
    response = tavily_client.search(query)
    return response


# 🤖 4) Create agent and register tools
base_agent: Agent = Agent(
    name="Search Agent",                    # 🧑‍🏫 Agent's identity
    model=model,
    tools=[search],                         # 🛠️ Register tools here
    model_settings=ModelSettings(           # ⚙️ Optional model settings
        temperature=0.5, 
        max_tokens=100
        )  
)
# 🤖 4) Create agent clones
math_agent: Agent = base_agent.clone(
    name="Math_Assistant ",                 # 🧑‍🏫 Agent's identity
    model=model,
    tools=[search],                         # 🛠️ Register tools here
    model_settings=ModelSettings(           # ⚙️ Optional model settings
        temperature=0.2, 
        max_tokens=100
        )  
    
)

# 📝 5) Define a prompt for the agent
prompt = "what is linear algebra?"


result_base = Runner.run_sync(base_agent, prompt)
result_friendly = Runner.run_sync(math_agent, prompt)

# print the results
print("Base Agent Result:\n", result_base.final_output)
print("Math Agent Result:\n", result_friendly.final_output)    

from dataclasses import dataclass, field, replace
from typing import List

@dataclass
class Agent:
    name: str
    instructions: str
    tools: List[str] = field(default_factory=list)

agent1 = Agent(name="Original", instructions="Follow the plan", tools=["Hammer", "Wrench"])
agent2 = replace(agent1, name="Cloned")  # Shallow copy

print(agent1)  # Agent(name='Original', instructions='Follow the plan', tools=['Hammer', 'Wrench'])
print(agent1.tools is agent2.tools)  # True → same list obje

agent2.tools.append("Screwdriver")
print("Agent1 tools:", agent1.tools)  # Uh-oh, also changed!
print("Agent2 tools:", agent2.tools)  # Both agents now have the same tools list

print("\n\n--- Deep Copy Example ---")
import copy

agent4 = copy.deepcopy(agent1)
agent4.tools.append("Drill")

print("Agent1 tools:", agent1.tools)  # unchanged
print("Agent4 tools:", agent4.tools)  # ['Hammer', 'Wrench', 'Drill'] - new tool added only to agent4

print("\n\n--- Custom Clone Method Example ---")

@dataclass
class Agent:
    name: str
    instructions: str
    tools: List[str] = field(default_factory=list)

    def clone(self, **changes):
        return replace(self, **changes)

# Example usage
a = Agent("A", "Test", ["tool1"])
b = a.clone(name="B", tools=a.tools.copy())

print(a.tools is b.tools)  # False → different lists   

