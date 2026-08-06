from chatstate import InterviewState

from langgraph.graph import StateGraph, START, END
from question import generate_question
from evalutor import evaluator_answer,question_type,follow_question,route_evaluation
from feedback import final_feedbacks

graph = StateGraph(InterviewState)

# Nodes
graph.add_node("interviewer", generate_question)
graph.add_node("evaluator", evaluator_answer)
graph.add_node("followup question type", question_type)
graph.add_node("followup question" , follow_question)
graph.add_node("coach", final_feedbacks)

# Initial Edge
graph.add_edge(START, "interviewer")

# Interview Flow
graph.add_edge("interviewer", "evaluator")
graph.add_edge("evaluator", "followup question type")
graph.add_edge("followup question type", "followup question")

# Conditional Routing
graph.add_conditional_edges('evaluator', route_evaluation, {'next question': 'question_type' , 'finish': 'final_feedbacks'})

# End
graph.add_edge("coach", END)

workflowline = graph.compile()