import os
import asyncio
from openai.types.responses import ResponseTextDeltaEvent
from agents import Agent, Runner, RunConfig, OpenAIChatCompletionsModel, set_default_openai_client
from openai import AsyncOpenAI
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

async def main():
    agent=Agent(
        instructions="You are the sales support agent and answer questions about the product.",
        name="Sales Support Agent",
        model=model,
    )
    result=Runner.run_streamed(agent,
        input="Tell me 4 facts about apple vision pro",
    run_config=run_config,)
    
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)

asyncio.run(main())
