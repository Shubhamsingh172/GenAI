import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key) #client hamara groq hai and 
model = "llama-3.3-70b-versatile" #model hamara llama hai

def llm_ans(prompt):
    message = {
        "role" : "user",
        "content" : prompt
    }
    messages = [message]
    response = client.chat.completions.create(model = model, messages = messages)
    ans = response.choices[0].message.content
    return ans


# bad_prompt = """This is a user complaint : My laptop is not working classify this"""
# print(llm_ans(bad_prompt))
"""
Answer : 
I would classify this complaint as a:

**Technical Issue/ Hardware Problem**

More specifically, it falls under the category of:

* **Computer/ Laptop Malfunction**
* **Device Not Turning On/ Not Functioning** 
"""

good_prompt = """
#ROLE : You are a support assistant at a mobile/laptop comapny
#TASK : You have to classify the issue in a category
#CONSTRAINTS : You have to classify the issue in one of the three categories namely billing, technical, return
#OUTPUT FORMAT : Your answer should be in one word only. The one word should be one of the categories given in constraints.
#EXAMPLE : For instance if a user complain says he wants a refund then category is Return
#FALLBACK : If the issue is unrelated to any of the categories mentioned in constraints, then the answer should be OTHER.
This is a user complaint : My laptop is not working"""
print(llm_ans(good_prompt)) #it will give the answer only in one word like here it is technical and then it will send it to the particular department of the company to resolve the issue.

#Like above for my laptop is not working it will give the output as techincal similarly
#for my wife is not working it will give the output as OTHER
