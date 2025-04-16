from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


prompt = """
    You are a mathematician who is trying to solve a problem. 
 
    Instructions:
    1.  answer the question.
    
    Example:
    
    Input : 5  + 7 
    OutPut : { answer : 12 }
    
    Input : 5  - 7 
    OutPut : { answer : -2 }
    
"""


# 
#   terminal based application for mathematical calculations 
# 
# 

while True: 
    expression = input("enter two numbers for : ")
    
    
    if expression == "break": break
    

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": prompt},
            {
                "role": "user",
                "content": expression,
            }
        ]
    )

    print(" Output => ", response.choices[0].message.content)
    
    print(" to stop the chat enter 'break' ")   
