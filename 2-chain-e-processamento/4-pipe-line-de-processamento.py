from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
load_dotenv();

template_translate = PromptTemplate(
    input_variables=["text"], 
    template="Translate the following text to Portuguese: {text}");

template_summarize = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text: {text}");

llm = chat = ChatOpenAI(model="gpt-5.4-nano", temperature=0);

translate = template_translate | llm | StrOutputParser();
pipeline = {"text": translate} | template_summarize | llm | StrOutputParser();

result = pipeline.invoke({"text": "LangChain is a powerful framework for building applications with language models."});
print(result);