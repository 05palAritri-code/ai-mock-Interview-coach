from typing import TypedDict,Annotated
import operator
from langgraph.graph.message import add_messages
from typing import List, Literal
from pydantic import BaseModel,Field




class InterviewState(TypedDict):
    target_role: str
    job_description: str | None = None
    focus_area: Literal["behavioral", "technical", "case", "mixed"]

    question: str
    answers: Annotated[List[dict],add_messages]

    technical : int
    relevant : int
    confident : int
    specificity : int

    technical_scores: Annotated[list[int], operator.add]
    relevance_scores: Annotated[list[int], operator.add]
    confidence_scores: Annotated[list[int], operator.add]
    specificity_scores: Annotated[list[int], operator.add]

    strengths: Annotated[list[str],add_messages]
    weakness :  Annotated[list[str],add_messages]

    overall_score: float

    follow_up_question_type: Literal['need to probe deeper' , 'move to next one' , 'calibarate difficulty']
    

    decision: Literal['next question','finish']

    question_count: int = 1

    max_count: int = 7
