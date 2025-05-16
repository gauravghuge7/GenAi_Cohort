from dotenv import load_dotenv
from openai import OpenAI
from langchain.document_loaders import PyPDFLoader


load_dotenv()
client = OpenAI()


loader = PyPDFLoader()