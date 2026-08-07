from chatstate import InterviewState
from llm_manager import coach_agent
from prompt import get_coach_messages

def final_feedbacks(state:InterviewState):
    response = coach_agent.invoke(get_coach_messages(state))
    p=len(state['technical_scores'])
    q=len(state['relevance_scores'])
    r=len(state['confidence_scores'])
    s=len(state['specificity_scores'])
    
    a= sum(state['technical_scores'])/p
    b= sum(state['relevance_scores'])/q
    c= sum(state['confidence_scores'])/r
    d= sum(state['specificity_scores'])/s
    

    return {
        'strong_points': response.strong_points,
        'weak_points': response.weak_points,
        'technical' : a,
        'relevant' : b,
        'confident': c,
        'specificity':d,
        'practice_plan': response.practice_plan,
        'recommendation': response.recommendation,
    }