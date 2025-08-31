from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI LLM
llm = OpenAI(model="gpt-3.5-turbo-instruct")

# Ask a question
result = llm.invoke("What is the capital of India?")
print(result)
