from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-base",   # ✅ works with text-generation
    task="text-generation",
    huggingfacehub_api_token="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")

# Directly invoke the LLM
result = llm.invoke("Write a haiku about recursion in programming.")
print(result)