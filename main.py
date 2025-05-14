from implementation.load_documents import load_all_documents
from implementation.vector_store import prepare_chunks, create_vector_store
from implementation.chat_engine import initialize_conversational_chain
from implementation.gardio_interface import start_gradio_interface
from implementation.config import DB_NAME

def main():
    documents = load_all_documents()
    print(f"Document types: {set(doc.metadata['doc_type'] for doc in documents)}")

    chunks = prepare_chunks(documents)
    print(f"Total number of chunks: {len(chunks)}")

    vectorstore, _ = create_vector_store(chunks, DB_NAME)
    print(f"Vectorstore created with {vectorstore._collection.count()} documents")

    conversation_chain = initialize_conversational_chain(vectorstore)
    start_gradio_interface(conversation_chain)

if __name__ == "__main__":
    main()
