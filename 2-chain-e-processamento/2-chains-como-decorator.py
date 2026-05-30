from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.runnables import chain

load_dotenv()

@chain
def square(input_dict: dict) -> dict:
    x = input_dict["x"];
    return {"square_result": x * x}

question_template2 = PromptTemplate(
    input_variables=["square_result"], 
    template="Tell me about the number {square_result}");

model = ChatOpenAI(model="gpt-5.4-nano", temperature=0.5);

chain2 = square | question_template2 | model; 

result = chain2.invoke({"x": 5});
print(result.content);