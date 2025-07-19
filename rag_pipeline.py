import chromadb
from chromadb.config import Settings
from embedder import embed
from prompt_template import format_prompt
from transformers import pipeline

client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory=".chromadb"))
collection = client.get_or_create_collection(name="docs")

llm = pipeline("text-generation", model="meta-llama/Meta-Llama-3-8B", device=0)

def add_documents(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    chunks = content.split('.')
    collection.add(
        documents=chunks,
        embeddings=embed(chunks),
        ids=[str(i) for i in range(len(chunks))]
    )

def generate_answer(query):
    query_embedding = embed([query])[0]
    results = collection.query(query_embeddings=[query_embedding], n_results=3)
    context = " ".join(results['documents'][0])
    prompt = format_prompt(query, context)
    output = llm(prompt, max_new_tokens=300, do_sample=False)[0]['generated_text']
    return output
