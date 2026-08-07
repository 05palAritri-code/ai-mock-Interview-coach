import uuid
from workflow import workflowline
from langgraph.types import Command

if __name__ == "__main__":
    print("AI Mock Interview Coach\n")
    target_role = input("Target role: ")
    job_description = input("Job description (optional, press enter to skip): ")
    focus_area = input("Focus area [behavioral/technical/case/mixed]: ")

    state = {
        "target_role": target_role,
        "job_description": job_description or None,
        "focus_area": focus_area,
        "answers": [],
        "strengths": [],
        "weaknesses": [],
        "technical_scores": [],
        "relevance_scores": [],
        "confidence_scores": [],
        "specificity_scores": [],
        "question_count": 1,
        "max_count": 2,
    }
    config = {"configurable": {"thread_id": str(uuid.uuid4())}}
    result = workflowline.invoke(state, config=config)

    while "__interrupt__" in result:
        question = result["__interrupt__"][0].value["question"]
        print(f"\nQ{state['question_count']}: {question}")
        answer = input("Your answer: ")
        result = workflowline.invoke(Command(resume=answer), config=config)
        state["question_count"] = result.get("question_count", state["question_count"])

    print("\n=== Final Feedback ===")
    print(f"Strengths:\n{result['strong_points']}")
    print(f"\nWeaknesses:\n{result['weak_point']}")
    print(f"\nPractice plan:\n{result['practice_plan']}")
    print(f"\nRecommendation:\n{result['recommendation']}")