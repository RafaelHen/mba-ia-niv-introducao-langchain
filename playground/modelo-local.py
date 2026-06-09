from langchain.tools import tool
from langchain.agents import create_agent
from langchain_ollama import ChatOllama

from dotenv import load_dotenv

load_dotenv()

@tool("calculator")
def calculator(expression: str) -> str:
    """Evaluate a simple mathematical expression and return the result as a string."""
    try:
        result = eval(expression)  # cuidado: apenas para exemplo didático
    except Exception as e:
        return f"Error: {e}"
    return str(result)

@tool("web_search_mock")
def web_search_mock(query: str) -> str:
    """Return the capital of a given country if it exists in the mock data."""
    data = {
        "Brazil": "Brasília",
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "United States": "Washington, D.C."
    }
    for country, capital in data.items():
        if country.lower() in query.lower():
            return f"The capital of {country} is {capital}."
    return "I don't know the capital of that country."

tools = [calculator, web_search_mock]

model = ChatOllama(
    model="qwen2.5:3b-instruct-q4_K_M",
    temperature=0,
    base_url="http://localhost:11434")


system_prompt=(
    "You must obey these rules exactly:\n"
    "1. Never answer from your own knowledge.\n"
    "2. If the available tools do not contain the answer, reply exactly with: I don't know.\n"
    "3. For country capitals, always call web_search_mock first.\n"
    "4. For math expressions, always call calculator first.\n"
    "5. After a tool returns a result, repeat only the tool result, with no extra explanation.\n"
)

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=system_prompt,
)

result1 = agent.invoke({
    "messages": [
        {"role": "user", "content": "What is the capital of Iran?"}
    ]
})

result2 = agent.invoke({
    "messages": [
        {"role": "user", "content": "How much is 10 + 10?"}
    ]
})

print(result1["messages"][-1].content)
print(result2["messages"][-1].content)