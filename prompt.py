from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.graph import state


def get_interview_messages(state):
    return [
        SystemMessage(content=f"""you are mock interview coach conducting profficient interview session of roughly 5–7 turns with intelligent follow-ups (not just a
fixed question list) and one after one .
Always respond with valid JSON only, matching the required schema exactly."""),
        HumanMessage(content=f"""
conduct a interview based on , job description : "{state['job_description']}"
- my Job role is "{state['target_role']}" and interview type should be "{state['focus_area']}"
Ask only the first interview question. No commentary, no answer.
""")
    ]



def get_evaluate_messages(state):
    last_answer = state["answers"][-1] if state.get('answers') else ""
    return [
        SystemMessage(content=f"""you are interview answer evaluator, you evaluate answer based on technicality , relevancy , confidence and 
        specificity and give number out of 10
        Always respond with valid JSON only, matching the required schema exactly.
        - 'technical' : give score out of 10
        - 'relevant' : give score out of 10
        - 'confident' : give score out of 10
        - 'specificity' : give score out of 10
        """),

        HumanMessage(content=f"""evaluate the answer "{last_answer}" and Question asked: "{state['question']}"

        Use the criteria below to evaluate the answer :
        -how technically correct
        -relevency to the question
        -confidence level of the answer
        -how specific and clear the answer is 

        ### Respond ONLY in structured format:
    -technical : give score out of 10
    -relevant : give score out of 10
    -confident : give score out of 10
    -specificity : give score out of 10

    "strengths": [
    "point 1",
    "point 2"
  ],
  "weaknesses": [
    "point 1",
    "point 2"
  ]
    


""")
    ]

def get_followup_type_messages(state):
    a=state["strengths"][-1]
    b=state["weaknesses"][-1]
    return [
        SystemMessage(content=f"""you are a type indicator for follow-up questuion ,Always respond with valid JSON only, matching the required schema exactly."""),
        HumanMessage(content=f"""determine the follow-up question type based on the following factors 
        -technical : "{state['technical']}" scores for "{state['question_count']}"
        -relevant : "{state['relevant']}" scores for "{state['question_count']}"
        -confident : "{state['confident']}" scores for "{state['question_count']}"
        -specificity : "{state['specificity']}" scores for "{state['question_count']}"
        and 
        - strengths "{a}"
        - weaknesses "{b}"
        

        ### Respond ONLY in structured format:
    - follow_up_question_type : 'need to probe deeper' or 'move to next one' or 'calibarate difficulty'

""")
    ]


def get_followup_question_messages(state):
    x=state["strengths"][-1]
    y=state["weaknesses"][-1]
    # z=state['overall_score']
    return [
    SystemMessage(content=f"""you generate follow-up question for interview session,Always respond with valid JSON only, matching the required schema exactly."""),
    HumanMessage(content=f"""genarate the next question based on 

    ##keep in mind##
    -candidate's job role : "{state['target_role']}"
    -Job description: "{state.get('job_description', 'Not provided')}"
    -interview type : "{state['focus_area']}"

    ## the instruction needed to follow ##
    -instruction : "{state['follow_up_question_type']}" , and 

    ## the following feedbacks and scores ##
    -strenghths : "{x}"
    -weaknesses : "{y}"
    **respond only in structured manner**
    follow_up_question: give a fllowup question 
     
    
    """)
]

def get_coach_messages(state):
    return [
    SystemMessage(content=f"""you are a interview coach, you generate overall feedback for the candidate performance,Always respond with valid JSON only, matching the required schema exactly."""),
    HumanMessage(content=f"""genarate interview session feedback in multiple dimensions, not just good or bad

    ##keep in mind##
    -candidate's job role : "{state['target_role']}"
    -interview type : "{state['job_description']}"

    
    ## the following feedbacks and scores ##
    -strenghths : "{state['strengths']}"
    -weaknesses : "{state['weaknesses']}"

    - technical : "{state['technical']}" for total "{state['question_count']}"
    - relevant : "{state['relevant']}" for total "{state['question_count']}"
    - confident : "{state['confident']}" for total "{state['question_count']}"
    - specificity : "{state['specificity']}" for total "{state['question_count']}"

    ### Respond ONLY in structured format:
    - strong_points : ["<list of strengths>"]
    - weak_points : ["<list of weaknesses>"]
    - technical_score: float
    - relevant_score : float
    - confident_score : float
    - clarity_score: float
    - practice_plan: expkain well
    - recommendation: describe in 3 4 line 
    """)
]



