from chatstate import InterviewState

from langgraph.graph import StateGraph, START, END

graph = StateGraph(InterviewState)

# Nodes
graph.add_node("interviewer", interviewer_agent)
graph.add_node("evaluator", evaluator_agent)
graph.add_node("memory", memory_agent)
graph.add_node("coach", coach_agent)

# Initial Edge
graph.add_edge(START, "interviewer")

# Interview Flow
graph.add_edge("interviewer", "evaluator")
graph.add_edge("evaluator", "memory")

# Conditional Routing
graph.add_conditional_edges(
    "memory",
    interview_decision,
    {
        "continue": "interviewer",
        "finish": "coach",
    },
)

# End
graph.add_edge("coach", END)

graph.compile()