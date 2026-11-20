from dotenv import load_dotenv 
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

response = model.invoke("what do you think the country with the most bright future is it ")
print(response.content)