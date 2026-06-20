from dotenv import load_dotenv
from langchain_groq import ChatGroq

from prompts.report_prompt import report_prompt

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3
)

report_chain = report_prompt | llm