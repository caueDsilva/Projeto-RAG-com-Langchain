from langchain_chroma.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
CAMINHO_DB = "db"

prompt_template = """
 Responda a pergunta do usuário:
   {pergunta}
   com base nessas informações a baixo: 
   {base_conhecimento}"""

def perguntar():
    pergunta = input("Escreva sua pergunta: ")

    # carregar o banco de dados
    funcao_embedding = OpenAIEmbeddings()
    db = Chroma(persist_directory=CAMINHO_DB,embedding_function=funcao_embedding)

    #comparar a pergunta do usuario (embedding) com base no banco de dados

    resultados = db._similarity_search_with_relevance_scores(pergunta,k=3)

    if len(resultados) == 0 or resultados[0][1] < 0.7:
        print("Nao encontrou uma informacao relevante")
        return

    textos_resultados = []
    for resultado in resultados:
        texto = resultado[0].page_content
        textos_resultados.append(texto)

    base_conhecimento = "\n\n----\n\n".join(textos_resultados)
    prompt = ChatPromptTemplate.from_template(prompt_template)
    prompt = prompt.invoke({"Pergunta":  pergunta, "base_conhecimento" : base_conhecimento})

    modelo = ChatOpenAI()
    texto_resposta = modelo.invoke(prompt).content
    print("Resposta da IA: ", texto_resposta)
perguntar()