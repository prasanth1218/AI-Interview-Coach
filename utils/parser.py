from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser


class InterviewEvaluation(BaseModel):

    score: int = Field(
        description="Score out of 10"
    )

    strengths: str

    weaknesses: str

    improved_answer: str


parser = PydanticOutputParser(
    pydantic_object=InterviewEvaluation
)