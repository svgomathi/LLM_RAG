# 🧠  Retrieval-Augmented Generation

![Python](https://img.shields.io/badge/Python-3.10+-blue) ![Gradio](https://img.shields.io/badge/Gradio-3.50.2-orange) ![HuggingFace](https://img.shields.io/badge/Hugging%20Face-Spaces-purple)

A simple **Retrieval-Augmented Generation (RAG)** app built with Python, FAISS, and FLAN-T5. Ask questions from any text (like resumes) and get **context-aware answers** instantly! ⚡  

---

## ✨ Features

- 📝 Index input text and split into chunks for accurate retrieval  
- 🧮 Generate vector embeddings using **sentence transformers**  
- ⚡ Fast similarity search with **FAISS vectorstore**  
- 🤖 Contextual answer generation using **FLAN-T5**  
- 🌐 Interactive **Gradio interface** for web-based Q&A  
- 🆓 Easy hosting on **Hugging Face Spaces**  

---

## 💻 Installation

1. **Clone the repository**  

```bash
git clone https://github.com/your-username/llm-rag-agent.git
cd llm-rag-agent
```
2. **Create and activate a virtual environment**

```bash
python3 -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```
3.**Install dependencies**
```bash
pip install -r requirements.txt
```
---

## 🛠 Usage
1. **Run the app locally**
```bash
python app.py
```
2.**Open the local Gradio URL in your browser:**
```bash
http://127.0.0.1:7860/
```
3. **Steps to use:**

- Paste your text (resume, document, etc.)
- Type a question about the text
- Click Submit and get your answer ✅
---

## 🔍 How It Works

1. **Indexing**

- Split input text into chunks
- Generate embeddings using HuggingFaceEmbeddings
- Store in FAISS vectorstore

2. **Query Answering**

- Retrieve relevant chunks from FAISS
- Construct a prompt with context
- Generate answers using FLAN-T5
## Reference

https://medium.com/@ksubash.ai/your-first-rag-app-build-and-host-it-on-hugging-face-spaces-3f60ac03ab3e
