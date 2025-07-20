import streamlit as st
from rag_pipeline import generate_answer, add_documents

st.set_page_config(page_title="GenAI Chatbot with RAG", layout="centered")

st.title("🤖 GenAI Chatbot")
st.subheader("Powered by RAG + LLaMA 3")

uploaded_file = st.file_uploader("Upload a .txt file as your knowledge base", type="txt")

if uploaded_file:
    with open(f"docs/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.getbuffer())
    add_documents(f"docs/{uploaded_file.name}")
    st.success("Document indexed!")

query = st.text_input("Ask your question:")

if query:
    with st.spinner("Thinking..."):
        response = generate_answer(query)
    st.markdown("### Answer:")
    st.write(response)
