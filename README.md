# RAG com Python e LangChain

Este projeto consiste em uma atividade prática de estudos desenvolvida com **Python e LangChain**, com o objetivo de compreender os conceitos fundamentais de **Retrieval-Augmented Generation (RAG)** e explorar como essa arquitetura pode ser utilizada para aprimorar aplicações baseadas em Large Language Models (LLMs).

## Objetivos

- Compreender o funcionamento da arquitetura RAG.
- Explorar a integração entre Python, LangChain e modelos de linguagem (LLMs).
- Aprender conceitos de embeddings e busca semântica.
- Entender como bancos de dados vetoriais armazenam e recuperam informações.
- Implementar um fluxo de recuperação de contexto para gerar respostas mais relevantes.
- Explorar a integração entre documentos externos e modelos de inteligência artificial generativa.

## O que é RAG?

Retrieval-Augmented Generation (RAG) é uma arquitetura que combina mecanismos de recuperação de informações com modelos de linguagem.

Em vez de depender exclusivamente dos conhecimentos adquiridos durante o treinamento, o modelo consulta uma base de conhecimento externa para recuperar informações relevantes e utilizá-las como contexto na geração de respostas.

Essa abordagem permite que aplicações de IA trabalhem com informações específicas, documentos próprios e bases de conhecimento atualizadas.

## Arquitetura do projeto

O fluxo de funcionamento de uma arquitetura RAG pode ser dividido nas seguintes etapas:

1. **Question:** O usuário envia uma pergunta para a aplicação.
2. **Semantic Search:** O LangChain realiza uma busca semântica para encontrar informações relevantes na base de conhecimento.
3. **Contextual Data:** Os documentos recuperados são organizados e enviados como contexto para o LLM, juntamente com a pergunta original.
4. **Response Generation:** O modelo de linguagem processa o contexto recebido e gera uma resposta.
5. **Post Processing:** A resposta pode passar por etapas de processamento antes de ser apresentada ao usuário.

## Tecnologias e conceitos

- **Python:** Linguagem utilizada no desenvolvimento da aplicação.
- **LangChain:** Framework para construção de aplicações baseadas em modelos de linguagem.
- **LLMs:** Modelos de linguagem responsáveis pela interpretação e geração de respostas.
- **Embeddings:** Representações vetoriais utilizadas para transformar textos em dados numéricos.
- **Vector Database:** Banco de dados (Chroma) responsável pelo armazenamento e recuperação de vetores.
- **Semantic Search:** Técnica de busca baseada no significado e na similaridade entre informações.

## Estrutura do projeto

```
.
├── base/             # PDFs que formam a base de conhecimento
├── database/         # Banco vetorial (Chroma), gerado automaticamente
├── criar_db.py       # Lê os PDFs, divide em chunks e gera os embeddings
├── main.py           # Recebe a pergunta, busca no banco e consulta o LLM
├── .env              # Chave da API da OpenAI (não versionar)
└── README.md
```

## Como rodar o projeto

### Pré-requisitos

- Python 3.10 ou superior
- Uma chave de API da OpenAI ([platform.openai.com](https://platform.openai.com/api-keys))

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd <nome-da-pasta>
```

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install pypdf langchain-core langchain-text-splitters langchain-chroma langchain-openai python-dotenv
```

### 4. Configurar a chave da OpenAI

Crie um arquivo `.env` na raiz do projeto com o conteúdo:

```env
OPENAI_API_KEY=sua-chave-aqui
```

### 5. Adicionar os documentos

Coloque os arquivos `.pdf` que serão usados como base de conhecimento dentro da pasta `base/`.

### 6. Criar o banco vetorial

```bash
python criar_db.py
```

Esse comando lê todos os PDFs de `base/`, divide o texto em chunks (2000 caracteres, com sobreposição de 500), gera os embeddings e salva tudo na pasta `database/`.

Rode esta etapa novamente sempre que adicionar ou alterar PDFs na pasta `base/`.

### 7. Fazer perguntas

```bash
python main.py
```

Digite sua pergunta no terminal. O programa busca os 3 trechos mais relevantes no banco, envia ao modelo como contexto e exibe a resposta. Se nenhum trecho tiver relevância mínima (score de 0.7), ele informa que não encontrou uma informação relevante.

> **Atenção:** a pasta do banco vetorial deve ter o mesmo nome nos dois scripts. Confira se `persist_directory` em `criar_db.py` e `CAMINHO_DB` em `main.py` apontam para a mesma pasta (`database`).

## Aprendizados

Este projeto tem caráter educacional e faz parte dos meus estudos sobre Inteligência Artificial Generativa e aplicações com LLMs.

A proposta é desenvolver conhecimentos práticos sobre a construção de pipelines RAG, compreendendo desde a preparação e recuperação de documentos até a integração com modelos de linguagem para geração de respostas contextualizadas.

## Status do projeto

Em desenvolvimento — projeto de estudos e experimentação com RAG, Python e LangChain.