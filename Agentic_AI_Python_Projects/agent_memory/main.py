# Temporary Agent Memory Example

import os
from dotenv import load_dotenv, find_dotenv
from agents import Agent, Runner, SQLiteSession, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled

# 🌿 Load environment variables
load_dotenv(find_dotenv())
set_tracing_disabled(True)  # Disable tracing for cleaner output
# 🔐 Setup Gemini client
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY, 
    base_url=BASE_URL
    )

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash", 
    openai_client=external_client
    )

# Create agent
agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant. Be friendly and remember our conversation.",
    model=model
)

# Create session memory
# Temporary memory (lost when program ends)
session = SQLiteSession("my_first_conversation")

print("=== First Conversation with Memory ===")

# Using the while loop to simulate a conversation with multiple turns. The agent should remember the context of the conversation within this session, but once the program ends, the memory will be lost.   
while True:
    user_input = input("Enter your message (type 'exit' to end): ")
    if user_input.lower() in ["exit", "quit"]:
        print("Ending conversation. Memory will be lost.")
        break
    result1 = Runner.run_sync(
    agent,
    user_input,
    session=session
)
    print("Agent:", result1.final_output)



