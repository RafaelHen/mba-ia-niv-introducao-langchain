from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory

load_dotenv();

# Meu chat vai carregar todo o prompt do sistema, mais o histórico de mensagens, e depois a mensagem do usuário.
# O modelo vai processar tudo isso e gerar uma resposta.
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")]);

chat_model = ChatOpenAI(model="gpt-5.4-nano", temperature=0.5);

#            --->
chain = prompt | chat_model;

# Implementar um gerenciador de sessão de chat, que armazena o histórico de mensagens e o contexto da conversa.
# Esse gerenciador pode ser um REDIS ou um banco de dados, ou até mesmo um arquivo local, dependendo do caso de uso e da escala da aplicação.

session_store: dict[str, InMemoryChatMessageHistory] = {};

def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory();
    return session_store[session_id];


conversational_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

config = {"configurable": {"session_id": "demo-session"}};

# Interactions
response = conversational_chain.invoke({"input": "Hello, my name is Rafael. how are you?"}, config=config);
print("Assistant:", response.content);
print("-" * 30);

response2 = conversational_chain.invoke({"input": "Can you repeat my name?"}, config=config);
print("Assistant:", response2.content);
print("-" * 30);

response3 = conversational_chain.invoke({"input": "Can you repeat my name in a motivational phrase?"}, config=config);
print("Assistant:", response3.content);
print("-" * 30);
