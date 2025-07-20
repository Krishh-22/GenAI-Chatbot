def format_prompt(question, context):
    return f"""\nYou are an intelligent assistant. Use the following context to answer the question clearly and concisely.\n\nContext:\n{context}\n\nQuestion:\n{question}\n\nAnswer:\n"""
