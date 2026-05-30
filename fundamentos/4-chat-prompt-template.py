from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

system = ("system", "you are an assistant that answers questions in a {style} style");
human = ("user", "{question}");

chat_prompt = ChatPromptTemplate.from_messages([system, human])
messages = chat_prompt.format_messages(style="funny", question="What is the capital of France?")

for msg in messages:
    print(f"{msg.type}: {msg.content}");


model = ChatOpenAI(model="gpt-5.4-nano", temperature=0.5);
result = model.invoke(messages);
print(result.content);