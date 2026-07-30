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
prompt = "who is padho with pratyush?"  # The message to send to the model and ek prompt likh diya
message = {"role": role, 
            "content": prompt}  # Create a message dictionary with role and content and message bana diya
# Create the message structure list of message means bahto saare message agar ek bhi message bhi poochna hai na toh list bana ke hi poochna padega  
messages = [message] #agar do message rehta then message1 and message2 ko list me daal ke hi poochna padega similarly for n message.
response = client.chat.completions.create(model = model, messages = messages)  # Send the message to the model and get the response
print(response)
print("---------------------------\n")
answer =  response.choices[0].message.content
print(answer)