import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from time import sleep, time

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client = Groq(api_key=my_api_key)  # client hamara groq hai and
model = "llama-3.3-70b-versatile" 

JD = """
We are hiring a Backend Python Developer

Requirements:
- Strong Python
- FastAPI or Django
- PostgreSQL
- Docker
- AWS
- REST APIs
- 2+ years of experience
"""

RESUME = """
Name = Shubham Singh

Experience : 
0 years as a Software Engineer/Developer.

Skills:
CORE Python, CPP, MYSQL, C, CORE JAVA, HTML, CSS

Projects:
Built a Search Image Engine using Unsplash API and HTML, CSS.

Deployed applications using Github.
"""

def ask_llm(system_prompt, user_prompt):
    sys_msg = {
        "role" : "system",
        "content" : system_prompt
    }
    user_msg = {
        "role" : "user",
        "content" : user_prompt
    }
    messages = [sys_msg, user_msg]
    response = client.chat.completions.create(model=model, messages=messages)
    answer = response.choices[0].message.content
    return answer

def step1_res_extract():
    #extract skills from resume
    system_prompt = """
    You are a professional resume HR assistant. Extract the skills from the candidates resume provided.
    Only return the skills no other information. Do not invent ay skillsby yourself.
    Output Format:
    Skills should be separated by commas. Just return comma separated skills do not return any other filler information.
    """
    user_prompt = f"""
    Extract the skills from this resume {RESUME}
    """
    return ask_llm(system_prompt, user_prompt)

def step2_JD_extract():
    #extract skills from Job Description
    system_prompt = """
    You are a professional resume HR assistant. Extract the skills from the Job description provided.
    Only return the skills no other information. Do not invent ay skillsby yourself.
    Output Format:
    Skills should be separated by commas. Just return comma separated skills do not return any other filler information.
    """
    user_prompt = f"""
    Extract the skills from this Job Description {JD}
    """
    return ask_llm(system_prompt, user_prompt)

def step3_match(candidate, jd):
    #match the skills from resume and JD
    system_prompt = """You are a professional HR assistant. compare the skills of candidate and the skills required in the JD and produce a final score between 1 and 100, also produce a short vedict whether the candidate is a good fit for the role."""
    user_prompt = f"""
    comapre and match the skills
    JD:{jd}
    Candidate:{candidate}
    """
    return ask_llm(system_prompt, user_prompt)

candidate = step1_res_extract()
print("Candidate Skills:\n", candidate)
sleep(2)
jd = step2_JD_extract()
print("JD Skills:\n", jd)
sleep(2)
score = step3_match(candidate, jd)
print("Final Score and Verdict:\n", score)
