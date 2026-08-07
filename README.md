# AI Mock Interview Coach

Multi-agent AI interview system built for an AI Engineer Internship Assignment.
##The Graph flow diagram is attached 
# Features
Multi-agent architecture
Adaptive follow-up questioning
Technical & behavioral interview support
Structured evaluation
Final interview report
LangGraph workflow orchestration
Modular prompt engineering

# Tech Stack
Python
LangGraph
LangChain
Groq/OpenAI Compatible LLM
Pydantic
TypedDict

#SteUp
git clone <repo>

cd AI-Mock-Interview-Coach

python -m venv myenv

myenv\Scripts\activate

pip install -r requirements.txt

# Run
python app.py

# Example output
Target role: qa engineer
Job description (optional, press enter to skip): 
Focus area [behavioral/technical/case/mixed]: technical

Q1: To start off, could you explain your approach to designing a test strategy for a new feature? Specifically, how do you decide which test cases should be automated and which should remain manual?
Your answer: i consider unit testing to check output of each module


Q2: You mentioned that unit testing is used to check module output; could you walk me through the specific process you follow to implement a unit test, including how you determine the test cases and why this approach ensures the reliability of the module?
Your answer: i didnt remember currently


Q3: Since you couldn't recall the specific details earlier, let's approach this from a practical scenario: if you were tasked with designing a test suite for a complex feature today, what specific tools, frameworks, or methodologies would you implement to ensure comprehensive coverage, and why?
Your answer: i use c++ .............

# Agent Responsibilities

## 1. Interviewer Agent

**Purpose**

Generates the initial interview question based on the candidate's selected role, optional job description, and interview focus area.

**Input**

- Target Role
- Job Description (optional)
- Focus Area

**Output**

- Context-aware interview question

---

## 2. Evaluation Agent

**Purpose**

Evaluates each candidate response across multiple dimensions.

### Evaluation Criteria

- Technical Correctness
- Relevance
- Confidence
- Specificity

### Output

- Individual scores
- Strengths
- Weaknesses

This structured evaluation becomes the basis for adaptive follow-up questioning and final feedback.

---

## 3. Follow-up Decision Agent

**Purpose**

Determines how the interview should continue after evaluating the candidate's response.

Possible decisions include:

- Need to probe deeper
- Move to the next topic
- Calibrate difficulty

The decision is based on evaluation scores, strengths, weaknesses, and the candidate's overall performance.

---

## 4. Follow-up Question Agent

**Purpose**

Generates an adaptive follow-up question tailored to the candidate's previous answer.

The agent considers:

- Previous question
- Candidate answer
- Evaluation scores
- Strengths
- Weaknesses
- Decision from the Follow-up Decision Agent

This enables a more realistic and dynamic interview experience.

---

## 5. Feedback Agent

**Purpose**

Produces a comprehensive interview report after the interview concludes.

The report includes:

- Overall technical performance
- Strong areas
- Weak areas
- Overall evaluation scores
- Personalized practice plan
- Final recommendation

---
## Agent Orchestration

The system is orchestrated using **LangGraph**, where each agent is represented as an independent node in a stateful workflow. A shared `InterviewState` object carries the interview context, candidate responses, evaluation results, and intermediate data between agents.

The execution flow is as follows:

1. **Interviewer Agent**
   - Generates the initial interview question based on the target role, optional job description, and selected interview focus area.

2. **Answer Collection**
   - The candidate submits an answer, which is stored in the shared interview state.

3. **Evaluation Agent**
   - Evaluates the candidate's response across four dimensions:
     - Technical correctness
     - Relevance
     - Confidence
     - Specificity
   - It also identifies key strengths and weaknesses.

4. **Follow-up Decision Agent**
   - Analyzes the evaluation results and decides whether to:
     - Probe deeper into the current topic,
     - Move to the next topic, or
     - Adjust the interview difficulty.

5. **Follow-up Question Agent**
   - Generates an adaptive follow-up question based on the previous answer, evaluation scores, strengths, weaknesses, and the decision made by the Follow-up Decision Agent.

6. **Loop Controller**
   - The workflow repeats the Answer → Evaluation → Decision → Follow-up cycle until the configured maximum number of interview questions is reached.

7. **Feedback Agent**
   - After the interview is complete, this agent aggregates the evaluation scores from all responses and generates a comprehensive feedback report, including strengths, areas for improvement, an overall assessment, a personalized practice plan, and a recommendation.

By separating responsibilities across specialized agents and coordinating them through a shared state, the system remains modular, maintainable, and easy to extend with additional capabilities such as resume-based RAG, web search, or voice interaction.