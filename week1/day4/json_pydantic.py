import os 
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

load_dotenv()  
myapi_key = os.getenv("GROQ_API_KEY")  
if not myapi_key:
    raise ValueError("GROQ_API_KEY is not set in the environment variables or api error.")

client = Groq(api_key=myapi_key)  
model = "llama-3.3-70b-versatile"  
role = "user"  

#structure output ke liye 
from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    email:str
    issue:str

schema = Ticket.model_json_schema()

response_format = {
    "type" : "json_object"
}

system_prompt = f"""Extract the personal information from the ticket strictly based on this schema{schema} and give me a json output"""
message_system = {
    "role" : "system",
    "content" : system_prompt
}

text = "My name is Shubham Singh. I have and iphone which is not working at all. I am from Nashik. My email id is abc@gmail.com. My contact nubmer is 702036"

prompt = f"""This is a customer ticket Please extract the personal information from this. {text}"""

message = {"role": role, 
            "content": prompt}  

messages = [message_system, message] 
response = client.chat.completions.create(model = model, messages = messages , response_format = response_format) #yaha temperature hamne isiliye badhaya hai like default one rehta hai but yaaha temperature = 2 likha alag output dekhne ke liye  
answer =  response.choices[0].message.content
print(answer)
#niche wale output me address nhi aaya hai because hamne json format ke liye jo class banaya tha waha pe address ke liye kuch nhi banaya hai
'''
{
  "name": "Shubham",
   "email": "abc@gmail.com",
   "issue": "Iphone not working"
}
'''

#ab hum jo baat kar rahe the na aage wala code padhta kaisa hai
import json
raw_json = answer
data_file = json.loads(raw_json)
ticket = Ticket(**data_file)
print(ticket.name)
print(ticket.email)
print(ticket.issue)

#isi ka use karke hum log llm ke output ko kaise structured banate hai wo hamne sikha so that complex na ho agle wale code ke liye to fetch the information, hame ye niche wala ticket.name, issue ye wala bhi output bhej sakte hai next llm ko nhi toh json format bhi bhej sakte hai

#Homework

#take resume in pdf or word
# have hr give you list of things like skill, experience, projects
#extract htese from resume 
#match against the hr list
#generate a percentage of matching or not