# AI Mock Interview Coach

Multi-agent AI interview system built for an AI Engineer Internship Assignment.

## Features

- Multi-agent architecture
- Adaptive interview flow
- Candidate evaluation
- Structured coaching feedback

## Tech Stack

- Python
- LangGraph

```mermid
graph TD;
        __start__([<p>__start__</p>]):::first
        interviewer(interviewer)
        get_answer(get_answer)
        evaluator(evaluator)
        question_type(question_type)
        followup_question(followup_question)
        coach(coach)
        __end__([<p>__end__</p>]):::last
        __start__ --> interviewer;
        evaluator -. &nbsp;finish&nbsp; .-> coach;
        evaluator -. &nbsp;next question&nbsp; .-> question_type;
        followup_question --> get_answer;
        get_answer --> evaluator;
        interviewer --> get_answer;
        question_type --> followup_question;
        coach --> __end__;
        classDef default fill:#f2f0ff,line-height:1.2
        classDef first fill-opacity:0
        classDef last fill:#bfb6fc

```
