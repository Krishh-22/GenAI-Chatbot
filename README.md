# 🤖 GenAI Chatbot with RAG

A fully functional GenAI chatbot powered by Retrieval-Augmented Generation (RAG), LLaMA 3, and Streamlit — capable of answering user questions from uploaded documents.

---

## 🚀 Features

- 🧠 **RAG Pipeline** – Retrieve relevant chunks before generation  
- 🔍 **Embedding Search** using `sentence-transformers` + ChromaDB  
- 💬 **LLM Response** using LLaMA 3 via HuggingFace Transformers  
- 🧾 **Prompt Engineering** with context-aware templates  
- 📄 **Custom Knowledge Base** – Upload `.txt` files as source docs  
- 🖥️ **Streamlit UI** for interactive chat  
- 📊 **Ready for Arize AI** (trace/evaluate chatbot answers)

---

## 📁 Project Structure
genai-chatbot/
├── app.py                 # Main Streamlit interface
├── rag_pipeline.py        # RAG workflow: retrieval + LLM response
├── embedder.py            # Embedding function using SentenceTransformers
├── prompt_template.py     # Builds prompt using retrieved context
├── utils.py               # Utility functions (e.g., text cleanup)
├── requirements.txt       # Python dependencies
├── docs/                  # Uploaded .txt files (used as knowledge base)
├── .gitignore             # Optional: ignores venv, cache, etc.
└── README.md              # Project description and usage guide

