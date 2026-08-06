from chatstate import InterviewState
from llm_manager import coach_agent
from prompt import get_coach_messages

def final_feedbacks(state:InterviewState):
    response = coach_agent.invoke(get_coach_messages(state))
    a= sum(state['technical_scores'])/len(state['technical_scores'])
    b= sum(state['relevance_scores'])/len(state['relevance_scores'])
    c= sum(state['confidence_scores'])/len(state['confidence_scores'])
    d= sum(state['specificity_scores'])/len(state['specificity_scores'])
    

    return {
        'strong_points': response.strong_points,
        'weak_points': response.weak_point,
        'technical' : a,
        'relevant' : b,
        'confident':c,
        'specificity':d,
        'practice_plan': response.practice_plan,
        'recommendation': response.recommendation,
    }