from pydantic import BaseModel, Field


class InterviewEvaluation(BaseModel):

    score: int = Field(
        description="Score out of 10"
    )

    strengths: str

    weaknesses: str

    improved_answer: str