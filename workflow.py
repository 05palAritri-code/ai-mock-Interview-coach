from chatstate import InterviewState
from langgraph.graph import StateGraph, START, END
from question import generate_question
from evalutor import evaluator_answer,question_type,follow_question,route_evaluation,get_answer
from feedback import final_feedbacks
from langgraph.checkpoint.memory import MemorySaver




graph = StateGraph(InterviewState)

graph.add_node("interviewer", generate_question)
graph.add_node("get_answer", get_answer)
graph.add_node("evaluator", evaluator_answer)
graph.add_node("question_type", question_type)
graph.add_node("followup_question" , follow_question)
graph.add_node("coach", final_feedbacks)

graph.add_edge(START, "interviewer")
graph.add_edge("interviewer", "get_answer")
graph.add_edge("get_answer", "evaluator")

graph.add_conditional_edges('evaluator', route_evaluation, {'next question': 'question_type' , 'finish': 'coach'})

graph.add_edge("question_type", "followup_question")
graph.add_edge("followup_question", "get_answer")
# graph.add_edge("followup_question", END)

graph.add_edge("coach", END)

checkpointer = MemorySaver()
workflowline = graph.compile(checkpointer=checkpointer)