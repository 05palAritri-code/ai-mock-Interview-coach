from pydantic import BaseModel,Field
from typing import Literal


class InterviewQuestion(BaseModel):
    question: str


class Evaluation(BaseModel):
    technical_accuracy: int = Field(description='score out of 10' ,ge=0, le=10)
    relevance_score: int = Field(description='score out of 10' ,ge=0, le=10)
    confidence_score: int = Field(description='score out of 10' ,ge=0, le=10)
    specificity_score: int = Field(description='score out of 10' ,ge=0, le=10)
    

    strengths: list[str] = Field (description='Detailed strength analysis for given answer')
    weaknesses: list[str] = Field (description='Detailed analysis for given answer')
    
class FollowupQuestionType(BaseModel):

    follow_up_question_type: Literal['need to probe deeper' , 'move to next one' , 'calibarate difficulty']

class FinalFeedback(BaseModel):

    strong_points : str = Field(description='describe in bullet patten')
    weak_point : str = Field(description='describe in bullet patten')

    technical_score: float
    relevance_score : float
    confidence_score : float
    clarity_score: float

    practice_plan: list[str]

    recommendation: str