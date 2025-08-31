from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-2", max_retries=3, temperature=0)
response = model.predict("Write a haiku about recursion in programming.")

print(response.content)