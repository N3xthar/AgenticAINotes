# chat node is the interuput node that take  the users input 


from langchain_google_genai import  GoogleGenerativeAI
from typing import TypedDict
from langgraph.graph import StateGraph , END , START



from dotenv import load_dotenv

load_dotenv()


llm = GoogleGenerativeAI(model="gemini-2.5-flash-lite")


# making a chat node for ineterpreting from teh user 

def chatNode(state:)