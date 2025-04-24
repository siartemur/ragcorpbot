from langdetect import detect

def build_prompt(question: str, context_chunks: list[tuple[str, str]]) -> str:
    detected_lang = detect(question)

    formatted_chunks = []
    for content, source in context_chunks:
        formatted_chunks.append(f"[{source}]\n{content}")

    context = "\n\n".join(formatted_chunks)

    if detected_lang == "en":
        prompt = f"""
Answer the user's question in clear and concise English based on the following context.
Mention the sources only once at the end. (e.g., 'Source: ...')

### Context:
{context}

### Question:
{question}

### Answer:"""
    else:
        prompt = f"""
Aşağıdaki bağlamlara göre kullanıcı sorusuna Türkçe, net ve kaynaklı bir yanıt ver.
Cevabın sonunda yalnızca 1 kez kaynakları belirt (örn. 'Kaynak: ...').

### Bağlam:
{context}

### Soru:
{question}

### Cevap:"""

    return prompt.strip()
