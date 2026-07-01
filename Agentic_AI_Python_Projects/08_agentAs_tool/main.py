#Agents as a Tool
#“Agents as a tool” means you let one agent call another agent like a function—without giving away control of the conversation. It’s perfect when you want a main agent 🧑‍💼 to stay in charge while specialist agents do small, focused jobs (translate this, extract dates, summarize, etc.).

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
    ModelSettings                    # ⚙️ Model configuration settings (if needed
)

# 🌿 Load environment variables from .env file
load_dotenv(find_dotenv())


# 🔑 Set OpenAI API key from environment variable (if needed by other parts of the code)
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")

# 🔐 Setup Gemini client
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY, 
    base_url=BASE_URL
    )
# 🧠 Initialize the model with the Gemini client
llm_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash", 
    openai_client=external_client
)
special_model=OpenAIChatCompletionsModel(
    model="gemini-2.5-pro", 
    openai_client=external_client
)
# make this client the default for any agents that don't explicitly get a model
set_default_openai_client(external_client)

# 🧠 2) Model Initialization (optional – you can also pass this model directly when running)
model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",        # ⚡ Fast Gemini model
    openai_client=external_client
)


spanish_agent = Agent(
    name="Spanish agent",
    instructions="Translate the user's message to Spanish."
)

french_agent = Agent(
    name="French agent",
    instructions="Translate the user's message to French."
)

orchestrator = Agent(
    name="Translator Orchestrator",
    instructions=(
        "You are a translation helper. If the user asks for Spanish, "
        "call translate_to_spanish. If French, call translate_to_french. "
        "Otherwise, ask which language they want."
    ),
    tools=[
        spanish_agent.as_tool(
            tool_name="translate_to_spanish",
            tool_description="Translate the user's message to Spanish."
        ),
        french_agent.as_tool(
            tool_name="translate_to_french",
            tool_description="Translate the user's message to French."
        ),
    ],
)
from agents import Runner
import asyncio

async def main():
    result = await Runner.run(orchestrator, "Please say 'Good morning' in Spanish.")
    print(result.final_output)

asyncio.run(main())
