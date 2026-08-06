
from chatstate import InterviewState
from prompt import get_interview_messages
from llm_manager import question_agent

def generate_question(state: InterviewState):

    response = question_agent.invoke(get_interview_messages(state))

    # return response
    return {'question': response.question}