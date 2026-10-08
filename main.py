import os
from dotenv import load_dotenv, find_dotenv
from agents import (
    Agent,
    Runner,
    OpenAIChatCompletionsModel,
    AsyncOpenAI,
    set_tracing_disabled,
)

load_dotenv(find_dotenv())
set_tracing_disabled(disabled=True)

external_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

llm_model = OpenAIChatCompletionsModel(
    model="gemini-3.5-flash-lite",
    openai_client=external_client,
)

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    model=llm_model,
)

result = Runner.run_sync(agent, "Welcome and motivate me to learn Agentic AI.")
print("AGENT RESPONSE:", result.final_output)