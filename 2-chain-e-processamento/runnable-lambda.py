from langchain_core.runnables import RunnableLambda

def parse_number(text: str) -> int:
    return int(text.strip());

parse_number_lambda = RunnableLambda(parse_number);

result = parse_number_lambda.invoke(" 42 ");
print(result.content);