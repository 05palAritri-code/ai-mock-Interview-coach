from workflow import opening_flow,workflowline 
from datetime import datetime

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
        "max_count": 7,
    }
    result = opening_flow.invoke(state)
    state.update(result)

    while True:
        print(f"\nQ{state['question_count']}: {state['question']}")
        answer = input("Your answer: ")
        if answer.lower().strip() in {"exit", "quit"}:
            break

        state["answers"] = state.get("answers", []) + [answer]
        result = workflowline.invoke(state)
        state.update(result)

        from datetime import datetime

        if "strong_points" in result:

            print("\n" + "=" * 50)
            print("  INTERVIEW COMPLETE — FEEDBACK REPORT")
            print("=" * 50)
            print(f"\nRole: {state['target_role']} | Focus: {state['focus_area']}")
            print(f"Questions answered: {state['question_count']}")

            avg_technical = sum(state['technical_scores']) / len(state['technical_scores'])
            avg_relevance = sum(state['relevance_scores']) / len(state['relevance_scores'])
            avg_confidence = sum(state['confidence_scores']) / len(state['confidence_scores'])
            avg_specificity = sum(state['specificity_scores']) / len(state['specificity_scores'])

            print(f"\nAverage Scores (out of 10):")
            print(f"  Technical:   {avg_technical:.1f}")
            print(f"  Relevance:   {avg_relevance:.1f}")
            print(f"  Confidence:  {avg_confidence:.1f}")
            print(f"  Specificity: {avg_specificity:.1f}")

            print(f"\nStrengths:\n{result['strong_points']}")
            print(f"\nAreas to improve:\n{result['weak_point']}")

            print(f"\nPractice plan:")
            for i, item in enumerate(result['practice_plan'], 1):
                print(f"  {i}. {item}")

            print(f"\nRecommendation:\n{result['recommendation']}")
            print("\n" + "=" * 50)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"transcript_{timestamp}.md"
            with open(filename, "w") as f:
                f.write(f"# Interview Transcript\n\n")
                f.write(f"**Role:** {state['target_role']} | **Focus:** {state['focus_area']}\n\n")
                f.write(f"## Q&A\n\n")
                for i, ans in enumerate(state['answers'], 1):
                    f.write(f"**Q{i}:** (question {i})\n\n**A{i}:** {ans}\n\n")
                f.write(f"## Feedback\n\n")
                f.write(f"**Strengths:**\n{result['strong_points']}\n\n")
                f.write(f"**Weaknesses:**\n{result['weak_point']}\n\n")
                f.write(f"**Practice Plan:**\n")
                for item in result['practice_plan']:
                    f.write(f"- {item}\n")
                f.write(f"\n**Recommendation:** {result['recommendation']}\n")

            print(f"\nTranscript saved to {filename}")
        break
