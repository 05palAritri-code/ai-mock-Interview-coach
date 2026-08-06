from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.graph import state

interview_messages = [
        SystemMessage(content=f"""you are mock interview coach help student/employee/workingprofessinoal,
you conduct profficient interview session of roughly 5–7 turns with intelligent follow-ups (not just a
fixed question list) and one after one ."""),
        HumanMessage(content=f"""
conduct a interview based on , job description : "{state['job_description']}"
- my Job role is "{state['target_role']}" and interview type should be "{state['focous_area']}"
""")
    ]


evaluate_message = [
        SystemMessage(content=f"""you are interview answer evaluator, you evaluate answer based on technicality , relevancy , confidence and 
        specificity and give number out of 10"""),
        HumanMessage(content=f"""evaluate the answer "{state['answers[-1]']}"
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

    strength : explain the streangth factor for given answer in 2 3 lines
    weakness : explain the weakness factor for given number
    take decision based on wheather "{state['question_count']}" hit "{state['max_count']}"
    -decision: "next question" or "finish"


""")
    ]

followup_question_type = [
        SystemMessage(content=f"""you are a type indicator for follow-up questuion """),
        HumanMessage(content=f"""determine the follow-up question type based on the following factors 
        -technical_score : "{state['technical']}" scores for "{state['question_count']}"
        -relevance_score : "{state['relevant']}" scores for "{state['question_count']}"
        -confidence_score : "{state['confident']}" scores for "{state['question_count']}"
        -specificity_score : "{state['specificity']}" scores for "{state['question_count']}"
        and 
        -strenghth_area : "{state['strengths[-1]']}"
        -weakness_area : "{state['weekness[-1]']}"
        

        ### Respond ONLY in structured format:
    -follow_up_question_type: 'need to probe deeper' or 'move to next one' or 'calibarate difficulty'

""")
    ]

followup_question = [
    SystemMessage(content=f"""you generate follow-up question for interview session"""),
    HumanMessage(content=f"""genarate the next question based on 

    ##keep in mind##
    -candidate's job role : "{state['target_role']}"
    -interview type : "{state['job_description']}"

    ## the instruction needed to follow ##
    -instruction : "{state['follow_up_question_type']}" , and 

    ## the following feedbacks and scores ##
    -strenghths : "{state['strengths[-1]']}"
    -weakness : "{state['weakness[-1]']}
    -overall_scores : "{state['overall_score']}"
     
    
    """)
]

coach_message = [
    SystemMessage(content=f"""you are a interview coach, you generate overall feedback for the candidate performance"""),
    HumanMessage(content=f"""genarate interview session feedback in multiple dimensions, not just good or bad

    ##keep in mind##
    -candidate's job role : "{state['target_role']}"
    -interview type : "{state['job_description']}"

    
    ## the following feedbacks and scores ##
    -strenghths : "{state['strengths']}"
    -weakness : "{state['weakness']}

    -technical_score : "{state['technical']}" for total "{state['question_count']}"
    -relevance_score : "{state['relevant']}" for total "{state['question_count']}"
    -confidence_score : "{state['confident']}" for total "{state['question_count']}"
    -specificity_score : "{state['specificity']}" for total "{state['question_count']}"

    ### Respond ONLY in structured format:
    -strong_points : describe in bullet patten
    -weak_point : describe in bullet patten
    -practice_plan: structured way
    -recommendation: improvement area
    """)
]



