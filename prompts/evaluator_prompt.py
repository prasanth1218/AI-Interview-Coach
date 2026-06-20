from langchain_core.prompts import ChatPromptTemplate

evaluator_prompt = ChatPromptTemplate.from_template(
    """
    You are a senior interviewer.

    Question:
    {question}

    Candidate Answer:
    {answer}

    Evaluate the answer.

    Provide:

    1. Score out of 10
    2. Strengths
    3. Weaknesses
    4. Improved Answer
    """
)