from llm_manager import eval_agent , question_pattern_agent ,follow_question_agent
from chatstate import InterviewState
from prompt import get_evaluate_messages, get_followup_type_messages, get_followup_question_messages
from langgraph.types import interrupt


def get_answer(state: InterviewState):
    answer = interrupt({"question": state["question"]})
    return {"answers": [answer]}

def evaluator_answer(state:InterviewState):

    
    response = eval_agent.invoke(get_evaluate_messages(state))

    # state['technical_scores']=response.technical
    # state['relevance_scores']=response.relevant
    # state['confidence_scores']=response.confident
    # state['specificity_scores']=response.specificity
     
    return {
        'technical':response.technical,
        'relevant':response.relevant,
        'confident':response.confident,
        'specificity':response.specificity,
        'technical_scores': [response.technical],
        'relevance_scores': [response.relevant],
        'confidence_scores': [response.confident],
        'specificity_scores': [response.specificity],
        'strengths':response.strengths,
        'weaknesses':response.weaknesses,
        
        }


def route_evaluation(state: InterviewState):
    return (
        "finish"
        if state["question_count"] + 1 > state["max_count"]
        else "next question"
    )   

def question_type(state:InterviewState):

    state['overall'] = (state['technical']+state['relevant']+state['confident']+state['specificity'])/4

    response = question_pattern_agent.invoke(get_followup_type_messages(state))

    return{'follow_up_question_type': response.follow_up_question_type}

def follow_question(state:InterviewState):

    # overall = (state['technical']+state['relevant']+state['confident']+state['specificity'])/4
    response = follow_question_agent.invoke(get_followup_question_messages(state))
    
    return {
        'question': response.follow_up_question,
        'question_count': state['question_count']+1 ,
        # 'overall_score': overall
    }




