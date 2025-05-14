from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from config import MODEL

def initialize_conversational_chain(vectorstore):
    llm = ChatOpenAI(temperature=0.7, model_name=MODEL)
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    retriever = vectorstore.as_retriever()
    chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, memory=memory)
    return chain
