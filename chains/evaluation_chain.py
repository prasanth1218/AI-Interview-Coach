from dotenv import load_dotenv
from langchain_groq import ChatGroq

from prompts.evaluator_prompt import evaluation_prompt
from utils.parser import InterviewEvaluation

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

structured_llm = llm.with_structured_output(
    InterviewEvaluation
)

evaluation_chain = (
    evaluation_prompt
    | structured_llm
)