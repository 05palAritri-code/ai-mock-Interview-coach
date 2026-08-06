from llm_manager import eval_agent , question_pattern_agent ,question_agent
from workflow import workflowline
from chatstate import InterviewState
from prompt import evaluate_message,followup_question_type,followup_question
from feedback import final_feedbacks
def evaluator_answer(state:InterviewState):

    message = evaluate_message
    
    response = eval_agent.invoke(message)

    state['technical_scores']=response.technical
    state['relevance_scores']=response.relevant
    state['confidence_scores']=response.confident
    state['specificity_scores']=response.specificity
     
    return {
        'technical':response.technical,
        'relevant':response.relevant,
        'confident':response.confident,
        'specificity':response.specificity,
        'strengths':response.strengths,
        'weakness':response.weakness,
        
        }

def route_evaluation(state:InterviewState):
    count = state['question_count']
    if count==state['max_count']:
        return 'final_feedbacks'
    else:
        return 'question_type'
    

def question_type(state:InterviewState):

    message = followup_question_type

    response = question_pattern_agent(message)

    return{'follow_up_question_type': response.follow_up_question_type}

def follow_question(state:InterviewState):

    state['overall_score'] = (state['technical']+state['relevant']+state['confident']+state['specificity'])/4

    message = followup_question

    response = question_agent.invoke(message)

    state['question_count'] =+1
    return




