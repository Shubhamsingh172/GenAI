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
# prompt = "I Love you babes?"  # The message to send to the model and ek prompt likh diya
# message_system = {
#     "role" : "system",
#     "content" : "You are my strict office colleague who is also my manager"
# }
prompt = "Suggest me a name for my grocery application and send me only one word"  # The message to send to the model and ek prompt likh diya
message_system = {
    "role" : "system",
    "content" : "You are a brand manager who suggests name for my grocery application, name should be in one word"
}
message = {"role": role, 
            "content": prompt}  # Create a message dictionary with role and content and message bana diya
# Create the message structure list of message means bahto saare message agar ek bhi message bhi poochna hai na toh list bana ke hi poochna padega  
messages = [message_system, message] #agar do message rehta then message1 and message2 ko list me daal ke hi poochna padega similarly for n message.
# response = client.chat.completions.create(model = model, messages = messages)  # Send the message to the model and get the response
'''
when the temperature is default 0

I'd be happy to help. Here are a few one-word name suggestions for your food company:

1. **Tasteo**: A combination of "taste" and "company" that sounds modern and catchy.
2. **Foodix**: A mix of "food" and the suffix "-ix," which suggests a unique and innovative approach to cuisine.
3. **Biteza**: A playful name that references the act of taking a bite, with a fun and approachable tone.
4. **Savora**: A name that evokes the idea of savoring delicious food, with a sophisticated and upscale feel.
5. **Nouria**: A word that conveys the idea of nourishment and wholesome food, with a warm and inviting tone.

Of these options, my top recommendation would be **Tasteo**. It's a simple, memorable name that immediately communicates the focus of your company: great taste and delicious food.

What do you think? Would you like me to suggest more options or elaborate on any of these names?'''
response = client.chat.completions.create(model = model, messages = messages, temperature = 2)  # Send the message to the model and get the response
'''
at temp = 1
How about "Tastio"? It's a unique and catchy name that conveys a sense of delicious food. Alternatively, you could also consider these other options:

* Flavora
* Foodza
* Delizo
* Biteo
* Cravio

But if I had to choose just one, I'd suggest "Tastio". It's easy to remember, easy to spell, and has a nice ring to it. Plus, it immediately communicates that your company is all about great taste!
'''
#the maximum temperature we can set is from 0 to 2
# print(response)
print("---------------------------\n")
answer =  response.choices[0].message.content
print(answer)