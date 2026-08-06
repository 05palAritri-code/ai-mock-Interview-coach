from chatstate import InterviewState
from llm_manager import coach_agent
from prompt import get_coach_messages

def final_feedbacks(state:InterviewState):
    response = coach_agent.invoke(get_coach_messages(state))
    return {
        'strong_points': response.strong_points,
        'weak_point': response.weak_point,
        'practice_plan': response.practice_plan,
        'recommendation': response.recommendation,
    }