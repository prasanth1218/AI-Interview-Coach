from langchain_core.prompts import ChatPromptTemplate

interviewer_prompt = ChatPromptTemplate.from_template(
"""
You are a senior technical interviewer.

Topic:
{topic}

Difficulty:
{difficulty}

Generate ONE interview question.

Rules:

Beginner:
- Fundamental concepts
- Easy understanding

Intermediate:
- Practical concepts
- Real-world scenarios

Advanced:
- System design
- Architecture
- Production-level concepts

Return only the question.
"""
)