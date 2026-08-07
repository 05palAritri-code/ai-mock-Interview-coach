from typing import TypedDict,Annotated,List,Literal,Optional
import operator
from typing import List, Literal
from pydantic import BaseModel,Field


class InterviewState(TypedDict ,total=False):
    target_role: str
    job_description: Optional[str]
    focus_area: Literal["behavioral", "technical", "case", "mixed"]

    question: str
    answers: Annotated[List[dict],operator.add]

    technical : float
    relevant : float
    confident : float
    specificity : float

    technical_scores: Annotated[list[int], operator.add]
    relevance_scores: Annotated[list[int], operator.add]
    confidence_scores: Annotated[list[int], operator.add]
    specificity_scores: Annotated[list[int], operator.add]

    strengths: Annotated[list[str],operator.add]
    weaknesses :  Annotated[list[str],operator.add]

    overall_score: float

    follow_up_question_type: Literal['need to probe deeper' , 'move to next one' , 'calibrate difficulty']

    max_count: int 
    question_count: int 

    strong_points: str
    weak_points: str
    practice_plan: List[str]
    recommendation: str

    
