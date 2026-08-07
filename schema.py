from pydantic import BaseModel,Field
from typing import Literal ,Annotated , Literal
import operator

class InterviewQuestion(BaseModel):
    question: str

class FollowUpQuestion(BaseModel):
    follow_up_question: str
    

class Evaluation(BaseModel):
    technical: int = Field(description='score out of 10' ,ge=0, le=10)
    relevant: int = Field(description='score out of 10' ,ge=0, le=10)
    confident: int = Field(description='score out of 10' ,ge=0, le=10)
    specificity: int = Field(description='score out of 10' ,ge=0, le=10)
    

    strengths: list[str]= Field (description='Detailed strength analysis for given answer')
    weaknesses: list[str]=Field (description='Detailed analysis for given answer')
    
class FollowupQuestionType(BaseModel):

    follow_up_question_type: Literal['need to probe deeper' , 'move to next one' , 'calibarate difficulty']

class FinalFeedback(BaseModel):

    strong_points: list[str] = Field(description='describe in bullet patten')
    weak_points: list[str] = Field(description='describe in bullet patten')

    technical_score: float
    relevant_score: float
    confident_score: float
    clarity_score: float

    practice_plan: str

    recommendation: str