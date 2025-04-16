from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

# Create a completion

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a asistant for coding"}, 
        {"role": "user", "content": "Write a python code to palindrome the number"}
    ]
)


print(" Output => ", response.choices[0].message.content)

