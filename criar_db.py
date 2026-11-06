from pathlib import Path
from pypdf import PdfReader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

PASTA_BASE = 'base'

def criar_db():
    documentos = carregar_documentos()
    chunks = dividir_chuncks(documentos)
    vetorizar_chunks(chunks)

def carregar_documentos():
    documentos = []
    for caminho in Path(PASTA_BASE).glob("*.pdf"):
        leitor = PdfReader(caminho)
        for i, pagina in enumerate(leitor.pages):
            texto = pagina.extract_text() or ""
            documentos.append(
                Document(
                    page_content=texto,
                    metadata={"source": str(caminho), "page": i},
                )
            )
    return documentos

def dividir_chuncks(documentos):
    separador_documentos = RecursiveCharacterTextSplitter(
        chunk_size= 2000, # define o tamanho de informaçao é extraido da base de conhecimento
        chunk_overlap = 500, # permite um sobreposiçao de chunks
        length_function = len,
        add_start_index=True
    )
    chunks = separador_documentos.split_documents(documentos)
    return chunks

def vetorizar_chunks(chunks):
    db = Chroma.from_documents(chunks, OpenAIEmbeddings(), persist_directory="database")

if __name__ == "__main__":
    criar_db()