import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

def prepare_chunks(documents):
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(documents)

def create_vector_store(chunks, db_name):
    embeddings = OpenAIEmbeddings()

    if os.path.exists(db_name):
        Chroma(persist_directory=db_name, embedding_function=embeddings).delete_collection()

    vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=db_name)
    return vectorstore, embeddings
