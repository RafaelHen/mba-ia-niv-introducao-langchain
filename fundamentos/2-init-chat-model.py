from langchain.chat_models import init_chat_model
from dotenv import load_dotenv  

load_dotenv()

gemini = init_chat_model("gemini-2.5-flash", model_provider="google_genai", temperature=0.5);
answer_gemini = gemini.invoke("Hello, World!, como resposta, fale em português");
print(answer_gemini);