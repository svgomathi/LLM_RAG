import gradio as gr
from indexer import index_text, answer_query

# Gradio interface function to handle the RAG system
def rag_system(input_text, query):
    # Index the input text
    vectorstore = index_text(input_text)
    
    # Answer the query based on the indexed text
    answer = answer_query(query, vectorstore)
    
    return answer

# Build the Gradio interface
iface = gr.Interface(
    fn=rag_system, 
    inputs=["text", "text"], 
    outputs="text", 
    title="RAG QA System",
    description="Enter a text and ask questions based on the input text."
)

# Launch the app
iface.launch()