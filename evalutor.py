from llm_manager import eval_agent , question_pattern_agent ,question_agent
from chatstate import InterviewState
from prompt import get_evaluate_messages, get_followup_type_messages, get_followup_question_messages

def evaluator_answer(state:InterviewState):

    
    response = eval_agent.invoke(get_evaluate_messages(state))

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
    return 'finish' if state['question_count'] >= state['max_count'] else 'next question'

    # count = state['question_count']
    # if count==state['max_count']:
    #     return 'final_feedbacks'
    # else:
    #     return 'question_type'
    

def question_type(state:InterviewState):

    response = question_pattern_agent.invoke(get_followup_type_messages(state))

    return{'follow_up_question_type': response.follow_up_question_type}

def follow_question(state:InterviewState):

    overall = (state['technical']+state['relevant']+state['confident']+state['specificity'])/4
    response = question_agent.invoke(get_followup_question_messages(state))

    return {
        'question': response.question,
        'question_count': state['question_count'] + 1,
        'overall_score': overall
    }




