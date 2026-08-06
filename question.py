
from workflow import workflowline
from chatstate import InterviewState
from prompt import interview_messages
from llm_manager import llm

def generate_question(state: InterviewState):

    # prompt
    messages = interview_messages

    # send generator_llm
    response = llm.invoke(messages).content

    # return response
    return {'question': response}