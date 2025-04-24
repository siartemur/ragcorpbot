def build_prompt(question: str, context_chunks: list[tuple[str, str]]) -> str:
    """
    context_chunks: List of tuples (chunk_content, source_info)
    Example: ("Greetings from page 2.", "example2.pdf – Page 2")
    """
    formatted_chunks = []
    for content, source in context_chunks:
        formatted_chunks.append(f"[{source}]\n{content}")

    context = "\n\n".join(formatted_chunks)

    prompt = f"""
Based on the context below, provide a clear and concise answer in Turkish.
At the end of your response, include the sources only once (e.g., 'Source: ...').

### Context:
{context}

### Question:
{question}

### Answer:"""
    return prompt.strip()
