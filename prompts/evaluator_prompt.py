from langchain_core.prompts import ChatPromptTemplate
from utils.parser import parser

evaluator_prompt = ChatPromptTemplate.from_template(
    """
    You are a senior interviewer.

    Question:
    {question}

    Candidate Answer:
    {answer}

    Evaluate the answer.

    {format_instructions}
    """
).partial(
    format_instructions=parser.get_format_instructions()
)