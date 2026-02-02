from langchain_groq import ChatGroq # <--- CAMBIO AQUÍ
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile", 
    temperature=0,
    max_retries=2,
    stop_sequences=None 
)