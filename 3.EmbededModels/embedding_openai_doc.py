from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimmension=32)
documents = ["Delhi is the capital of India",
             "Mumbai is the financial capital of India"
             "Kolata is the capital of West Bengal"]
result=embedding.embed_documents(documents)

print(str(result))