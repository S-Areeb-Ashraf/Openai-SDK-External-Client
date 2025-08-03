import os
import asyncio
import chainlit as cl
from openai.types.responses import ResponseTextDeltaEvent
from agents import Agent, Runner, RunConfig, OpenAIChatCompletionsModel
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

agent1=Agent(
    instructions="You are the sales support agent and answer questions about the product.",
    name="Sales Support Agent",
)

@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history",[])
    await cl.Message(content="Hello, I am your assistant. How can I help you?").send()

@cl.on_message
async def main(message: cl.Message):
    history=cl.user_session.get("history")
    msg=cl.Message(content="")
    await msg.send()

    history.append({"role":"user","content":message.content})
    result=Runner.run_streamed(
        agent1,
        input=history,
        run_config=run_config,
    )

    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            await msg.stream_token(event.data.delta)

    history.append({"role":"assistant","content":result.final_output})
    cl.user_session.set("history",history)
