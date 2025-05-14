import os
import glob
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.schema import Document

def add_metadata(doc, doc_type):
    doc.metadata["doc_type"] = doc_type
    return doc

def load_all_documents(base_path="knowledge-base"):
    folders = glob.glob(f"{base_path}/*")
    documents = []
    text_loader_kwargs = {'encoding': 'utf-8'}

    for folder in folders:
        doc_type = os.path.basename(folder)
        loader = DirectoryLoader(folder, glob="**/*.md", loader_cls=TextLoader, loader_kwargs=text_loader_kwargs)
        folder_docs = loader.load()
        documents.extend([add_metadata(doc, doc_type) for doc in folder_docs])

    return documents
