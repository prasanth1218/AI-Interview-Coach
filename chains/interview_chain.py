from dotenv import load_dotenv
from langchain_groq import ChatGroq

from prompts.interviewer_prompt import interviewer_prompt

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7
)

question_chain = interviewer_prompt | llm