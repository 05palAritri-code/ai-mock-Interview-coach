from chatstate import InterviewState
from langgraph.graph import StateGraph, START, END
from question import generate_question
from evalutor import evaluator_answer,question_type,follow_question,route_evaluation
from feedback import final_feedbacks

opening_graph = StateGraph(InterviewState)

opening_graph.add_node("interviewer", generate_question)
opening_graph.add_edge(START, "interviewer")
opening_graph.add_edge("interviewer", END)

opening_flow = opening_graph.compile()

turn_graph = StateGraph(InterviewState)

turn_graph.add_node("evaluator", evaluator_answer)
turn_graph.add_node("followup question type", question_type)
turn_graph.add_node("followup question" , follow_question)
turn_graph.add_node("coach", final_feedbacks)


turn_graph.add_edge(START, "evaluator")

turn_graph.add_conditional_edges('evaluator', route_evaluation, {'next question': 'followup question type' , 'finish': 'coach'})

turn_graph.add_edge("followup question type", "followup question")
turn_graph.add_edge("follow_question", END)

turn_graph.add_edge("coach", END)

workflowline = turn_graph.compile()