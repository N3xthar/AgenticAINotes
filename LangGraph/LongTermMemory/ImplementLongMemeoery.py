from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage, HumanMessage 

from langchain_core.runnables import RunnableConfig


# for storing the message in inmeomorry 


# runnable store the configuration like user_id and user_input and also the prompt template and output parser


load_dotenv()

model = GoogleGenerativeAI(model="gemini-2.5-flash-lite")
parser = StrOutputParser()


# visualise the graph \
chain.get_graph().print_ascii()