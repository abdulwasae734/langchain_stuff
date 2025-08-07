import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage,HumanMessage

load_dotenv()
os.environ.get("OPENAI_API_KEY")

model = init_chat_model("gpt-4o-mini", model_provider="openai")

messages = [
    SystemMessage("You are a translator. translate from english to arabic"),
    HumanMessage("yo whats up bro")
]

print(model.invoke(messages).pretty_print())