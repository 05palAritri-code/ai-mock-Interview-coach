from pydantic import BaseModel,Field
from typing import List, Literal




class InterviewQuestion(BaseModel):
    question: str


class Evaluation(BaseModel):
    technical_accuracy: int = Field(description='score out of 10' ,ge=0, le=10)
    relevance_score: int = Field(description='score out of 10' ,ge=0, le=10)
    confidence_score: int = Field(description='score out of 10' ,ge=0, le=10)
    specificity: int = Field(description='score out of 10' ,ge=0, le=10)
    

    strengths: list[str] = Field (description='Detailed strength analysis for given answer')
    weaknesses: list[str] = Field (description='Detailed analysis for given answer')


class QuestionType(BaseModel):

    follow_up_question_type: Literal['need to probe deeper' , 'move to next one' , 'calibarate difficulty']


class FinalFeedback(BaseModel):
    overall_score: float

    strengths: list[str]

    weaknesses: list[str]

    practice_plan: list[str]

    recommendation: str