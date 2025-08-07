import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()
os.environ.get("OPENAI_API_KEY")

model = init_chat_model("gpt-4o", model_provider="openai")
res = model.invoke("do you know from where i am interacting with you? web or api key")
print(res.pretty_print())
