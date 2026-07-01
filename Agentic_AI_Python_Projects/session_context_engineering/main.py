import os
import asyncio

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine

from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.extensions.memory.sqlalchemy_session import SQLAlchemySession

load_dotenv()

def setup_gemini_model():
    """Configure Gemini model using OpenAI-compatible API."""
    api_key = os.getenv("GEMINI_API_KEY")

    external_client = AsyncOpenAI(
        api_key=api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )
    
    return OpenAIChatCompletionsModel(
        model="gemini-2.5-flash",
        openai_client=external_client
    )

async def main():
    # In your application, you would use your existing engine
    # Get DB URL from NEON Postgres DB
    engine = create_async_engine("postgresql://neondb_owner:npg_QTaW5Pv4GgAt@ep-still-wave-aplt6sjf.c-7.us-east-1.aws.neon.tech/neondb?sslmode=require")

    llm_model = setup_gemini_model()

    agent = Agent("Assistant", model=llm_model)
    session = SQLAlchemySession(
        "AQKhan",
        engine=engine,
        create_tables=True,  # Auto-create tables for the demo
    )

    result = await Runner.run(agent, "What did I just ask?", session=session)
    print(result.final_output)

    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(main())