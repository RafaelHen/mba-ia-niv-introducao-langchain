from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_classic.chains.summarize import load_summarize_chain
load_dotenv();

text = """O relógio na parede marca o tempo devagar,
cada segundo alongado como um suspiro no ar.
A xícara de café esfria na mesa vazia,
enquanto a mente viaja por onde o dia não guia.

Na janela, a chuva desenha caminhos no vidro,
caminhos que levam a lugares que não vislumbro, mas antevisto.
Lembro de risos antigos, de conversas sem fim,
de noites em claro buscando respostas que não vieram pra mim.

O silêncio da sala é peso, é abrigo, é espelho,
mostra o que eu tenho, o que falta, o queelho.
Mas no fundo do peito, há um fogo que não se apaga,
uma chama teimosa que frente à espera não se margina, não se flagra.

Porque esperar não é parar, é caminhar em silêncio,
é construir no invisível, é plantar no terreno.
E quando o tempo finalmente se abrir e chegar,
o que eu plantei na espera vai florir sem parar."""; 

# raramente quebra uma palavra ao meio, sempre para um ponto de quebra natural, como um parágrafo ou frase.
splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=0);

#chunk_size -> é o tamanho máximo de cada chunk. O texto será dividido em pedaços que não excedam esse tamanho. Isso é útil para garantir que os chunks sejam gerenciáveis e possam ser processados eficientemente.
#chunk_overlap -> é a quantidade de texto que se sobrepõe entre os chunks. Isso pode ser útil para garantir que o contexto seja mantido entre os chunks, especialmente se eles forem processados separadamente.

parts = splitter.create_documents([text]);

# for part in parts:
#     print(part.page_content);
#     print("-" * 30)

llm = ChatOpenAI(model="gpt-5.4-nano", temperature=0);

chain_summarize = load_summarize_chain(llm, chain_type="stuff", verbose=False);

result = chain_summarize.invoke({"input_documents": parts});
print(result);