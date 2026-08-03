import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from time import sleep

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Where is API brother")

client = Groq(api_key = my_api_key)

model = "llama-3.3-70b-versatile"
prompt = "Explain how internet works."
message = {
    "role" : "user", 
    "content" : prompt
}

messages = [message]
#bina streaming ke answer like jab streaming true nhi hai toh because by default stream = false hota hai 
# response1 = client.chat.completions.create(model = model, messages = messages)
#print(response1)
# answer = response1.choices[0].message.content
# print(answer)

stream = client.chat.completions.create(model = model, messages = messages, stream = True)

for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end = "", flush = True)

# Jabh bhi ham koi bhi cah build karenge then at that time streaming ka functionality dalna bahto effective hoga ek better experience provide karne ke liye.