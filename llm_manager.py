import os 
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from schema import Evaluation ,InterviewQuestion,FinalFeedback,FollowupQuestionType,FollowUpQuestion

load_dotenv()


llm=ChatOpenAI(
    model='google/gemma-4-31b-it:free',
    # model ="inclusionai/ling-3.0-tiny:free"
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0.1,
    timeout=60,
    max_retries=2,
)
llm1 = ChatOpenAI(
    model="gemma-3-27b-it",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0,      
    timeout=15,         
    max_retries=2
)

question_agent = llm.with_structured_output(InterviewQuestion,method="json_mode")

follow_question_agent = llm1.with_structured_output(FollowUpQuestion)

eval_agent = llm.with_structured_output(Evaluation,method="json_mode")
coach_agent = llm.with_structured_output(FinalFeedback,method="json_mode")

question_pattern_agent = llm1.with_structured_output(FollowupQuestionType,method="json_mode")
