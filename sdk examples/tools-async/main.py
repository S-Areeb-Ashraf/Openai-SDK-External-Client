import os
import asyncio
from openai.types.responses import ResponseTextDeltaEvent
from agents import Agent, Runner, RunConfig, OpenAIChatCompletionsModel, set_default_openai_client
from openai import AsyncOpenAI
from agents.tool import function_tool
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

gemini_api_key = os.getenv("gemini_api_key")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model=OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=provider,
)

run_config=RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True,    
)

set_default_openai_client(provider)

@function_tool("get_current_weather")
def get_current_weather(location: str, unit: str = "celsius") -> str:
    """Get the current weather in a given location"""
    return f"The current weather in {location} is 20 degrees {unit}."

async def main():
    agent=Agent(
        name="Support Agent",
        instructions="You only answer questions",
        tools=[get_current_weather],
        model=model,
    )
    result=await Runner.run(agent,
        input="What is the current weather of Karachi, Paksitan in celcius?",
    run_config=run_config,)
    print(result.final_output)

asyncio.run(main())
