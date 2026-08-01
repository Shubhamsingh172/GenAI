import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from time import sleep
import re 

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key) #client hamara groq hai and 
model = "llama-3.3-70b-versatile" #model hamara

def get_product_price(product):
    if product == "iphone 17":
        return 1000
    elif product == "iPhone 15":
        return 500
    else:
        return 0

def calculator(expression):
    try:
        return eval(expression)
    except:
        return "calc error!"

tools = {
    "get_product_price": get_product_price,
    "calculator": calculator
}

system_prompt = """
You are a shopping assistant.

You have these tools:

get product price(product) : This tool takes a product name as input and returns its current price.
calculator(expression) : This tool takes a mathematical expression as input and returns the calculated result.
IMPORTANT:
Call tools exactly like these examples:

Action: get_product_price("iphone 17")
Action: calculator("5000 - 1000")

Never write:
calculator(expression = "5000 - 1000")
Follow these rules:

1.Decide what you need to don next.
2.Call Only one tool at a time.
3.After writing an Action, Stop immediately.
4.Never guess or invent a tool result.
5.Wait until you receive an Observation.
6.Then decide your next action.
7.When the task is complete give the Final Answer.

Format:

Thought: What you need to do
Action: tool_name(argument)

When finished:

Final Answer: your answer

"""

def run_agent(question):

    messages = [
        {"role": "system", 
         "content": system_prompt
        },

        {"role": "user", 
         "content": question}
    ]

    for step in range(5):
        print("\n----------------------------------------------")
        print(f"Step {step + 1}:")
        print("----------------------------------------------")

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature = 0
        )

        answer = response.choices[0].message.content
        print("LLM Response:\n", answer)

        #Agent has finished
        if "Final Answer:" in answer:
            break

        #Find the Action 
        match = re.search(r"Action:\s*(\w+)\((.*)\)", answer)
        if match:
            tool_name = match.group(1)

            tool_input = match.group(2)

            tool_input = tool_input.strip()

            tool_input = tool_input.strip('"')

            #Run the tool
            if tool_name in tools:
                tool = tools[tool_name]
                observation = tool(tool_input)
            else:
                observation = f"Tool {tool_name} not found."

            print("Observation:\n", observation)

            #Add LLM response to memory
            messages.append({"role": "user",
                             "content" : 
                                "Observation: " + str(observation)})
            sleep(5)


prompt = """
I have 5000 rupees. What is the price of an iphone 17? and how many money will I have left?"""
run_agent(prompt)