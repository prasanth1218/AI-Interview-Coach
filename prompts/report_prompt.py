from langchain_core.prompts import ChatPromptTemplate

report_prompt = ChatPromptTemplate.from_template(
    """
    You are an expert interview coach.

    Interview History:

    {history}

    Generate:

    1. Overall Performance
    2. Strong Areas
    3. Weak Areas
    4. Learning Recommendations
    5. Interview Readiness Score

    Be detailed.
    """
)