import os 
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from schema import Evaluation ,InterviewQuestion,FinalFeedback,QuestionType

load_dotenv()


llm=ChatOpenAI(
    model='google/gemma-4-31b-it:free',
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
question_agent = llm.with_structured_output(InterviewQuestion)
eval_agent = llm.with_structured_output(Evaluation)
question_pattern_agent = llm.with_structured_output(QuestionType)
coach_agent = llm1.with_structured_output(FinalFeedback)