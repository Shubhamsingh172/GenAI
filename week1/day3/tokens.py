import os 
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

load_dotenv()  # Load environment variables from .env file
myapi_key = os.getenv("GROQ_API_KEY")  # Get the API key from environment variables   
if not myapi_key:
    raise ValueError("GROQ_API_KEY is not set in the environment variables or api error.")

client = Groq(api_key=myapi_key)  # Create a client instance with the API key and client bana diya
model = "llama-3.3-70b-versatile"  # Specify the model to use and model bana diya
role = "user"  # Specify the role for the message and role bana diya
prompt1 = "Hi!"
prompt2 = "Explain time travel in Detail"
prompt3 = "Write a 1000 word essay on Machine Learning."
prompts = [prompt1, prompt2, prompt3]
for prompt in prompts:
    message = {
        "role" : role, 
        "content": prompt
    }
    messages = [message]
    response = client.chat.completions.create(model = model, messages = messages, max_tokens = 50) #max tokens are used to limit the usage of tokens
    usage = response.usage
    print(f"Prompt : {prompt} --> your tokens : {usage.prompt_tokens} completion_tokens : {usage.completion_tokens} total tokens : {usage.total_tokens} Finish Reason : {response.choices[0].finish_reason}") # finish reason ye batata hai ki tokens naturally stop hua hai ya limitation ke wajah se and finish reason tokens ke limit pe depend hoga 
# prompt = "who is padho with pratyush?"  # The message to send to the model and ek prompt likh diya
# message = {"role": role, 
#             "content": prompt}  # Create a message dictionary with role and content and message bana diya
# # Create the message structure list of message means bahto saare message agar ek bhi message bhi poochna hai na toh list bana ke hi poochna padega  
# messages = [message] #agar do message rehta then message1 and message2 ko list me daal ke hi poochna padega similarly for n message.
# response = client.chat.completions.create(model = model, messages = messages)  # Send the message to the model and get the response
# print(response)
# print("---------------------------\n")
# answer =  response.choices[0].message.content
# print(answer)