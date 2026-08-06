from typing import TypedDict,Annotated
import operator

from typing import List, Literal
from pydantic import BaseModel,Field




class InterviewState(TypedDict):
    target_role: str
    job_description: str | None = None
    focus_area: Literal["behavioral", "technical", "case", "mixed"]

    conversation: Annotated[List[dict],operator.add]

    technical : int
    relevant : int
    confident : int
    specificity : int

    technical_scores: Annotated[list[int], operator.add]
    relevance_scores: Annotated[list[int], operator.add]
    confidence_scores: Annotated[list[int], operator.add]
    specificity_scores: Annotated[list[int], operator.add]

    strengths: Annotated[list[str],operator.add]
    weakness :  Annotated[list[str],operator.add]

    overall_score: float
    

    evaluate_history: Annotated[list[str], operator.add]

    decision: Literal['interview_question','finish']

    question_count: int = 0
    followup_count: int = 0
    max_count: int = 7
