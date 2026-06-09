from langchain.tools import tool
from langchain.agents import create_agent
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

agent = create_agent(
    model="openai:gpt-5-mini",
    tools=tools,
    system_prompt=(
        "Answer the user's question as best you can using only the available tools. "
        "Only use information returned by the tools, even if you know the answer. "
        "If the information is not provided by the tools, say you don't know. "
        "Never search the internet. Only use the tools provided."
    ),
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