from pydantic import BaseModel,Field
from typing import Literal


class InterviewQuestion(BaseModel):
    question: str


class Evaluation(BaseModel):
    technical: int = Field(description='score out of 10' ,ge=0, le=10)
    relevant: int = Field(description='score out of 10' ,ge=0, le=10)
    confident: int = Field(description='score out of 10' ,ge=0, le=10)
    specificity: int = Field(description='score out of 10' ,ge=0, le=10)
    

    strengths: list[str] = Field (description='Detailed strength analysis for given answer')
    weaknesses: list[str] = Field (description='Detailed analysis for given answer')
    
class FollowupQuestionType(BaseModel):

    follow_up_question_type: Literal['need to probe deeper' , 'move to next one' , 'calibarate difficulty']

class FinalFeedback(BaseModel):

    strong_points : str = Field(description='describe in bullet patten')
    weak_points : str = Field(description='describe in bullet patten')

    technical: int
    relevant : int
    confident : int
    specificity : int

    practice_plan: list[str]

    recommendation: str