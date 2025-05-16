
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


system_prompt = """
    You are a Assistant for the Generating the Piping and Instrument Diagrams for the chemical process pump like ethanol tanks like this 
    
    Instructions: 
"""