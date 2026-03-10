from transformers import pipeline
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
# Function to index the input text
def index_text(input_text):
    # Split the input text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_text(input_text)  
    documents = [Document(page_content=chunk) for chunk in splits]

    # Embed the input text chunks
    embeddings = HuggingFaceEmbeddings()
    
    # Replace Chroma with FAISS
    vectorstore = FAISS.from_documents(documents=documents, embedding=embeddings)
    
    return vectorstore
# Function to answer user query based on indexed input text
def answer_query(query, vectorstore):
    retriever = vectorstore.as_retriever()
    search_results = retriever.get_relevant_documents(query)
    
    context = " ".join([doc.page_content for doc in search_results])
    
    generator = pipeline("text2text-generation", model="google/flan-t5-base")

    prompt = f"Based on this text: {context}\nAnswer this question: {query}"
    generated_text = generator(prompt, max_length=100)

    return generated_text[0]['generated_text']